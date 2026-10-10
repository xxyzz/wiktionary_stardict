import { createServer } from "node:http";
import MathJax from "mathjax";

await MathJax.init({
  loader: {
    load: ["input/tex", "output/svg"],
  },
  svg: {
    fontCache: "none",
    postFilters: [
      ({ data }) => {
        // MuPDF default font size for SVG is too small:
        // https://bugs.ghostscript.com/show_bug.cgi?id=709705
        const adaptor = MathJax.startup.adaptor;
        const outputJax = MathJax.startup.document.outputJax;

        const svg = adaptor.tags(data, "svg")[0];
        if (svg) {
          const pxPerEm = outputJax.pxPerEm;
          const fixed = outputJax.fixed;

          const viewBox = adaptor.getAttribute(svg, "viewBox");
          if (viewBox) {
            const [, , w, h] = viewBox.trim().split(/\s+/).map(Number);

            adaptor.setAttribute(svg, "width", `${fixed(w * pxPerEm / 1000)}px`);
            adaptor.setAttribute(svg, "height", `${fixed(h * pxPerEm / 1000)}px`);
          }

          const style = adaptor.getAttribute(svg, "style");
          if (style) {
            const match = style.match(/(-?\d+(?:\.\d+)?)ex/);
            if (match) {
              const value = fixed(Number(match[1]) * 18);
              adaptor.setAttribute(svg, "style", `vertical-align: ${value}px`);
            }
          }
        }
      },
    ],
  },
});

async function tex2svg(input) {
  const node = await MathJax.tex2svgPromise(
    input,
    { display: true, em: 36, ex: 18 },
  );
  return MathJax.startup.adaptor.serializeXML(node);
}

const server = createServer(async (req, res) => {
  if (req.method === "POST" && req.url === "/tex2svg") {
    let body = [];
    req
      .on("data", chunk => {
        body.push(chunk);
      })
      .on("end", async () => {
        body = Buffer.concat(body).toString();
        const svg = await tex2svg(body);
        res.on("error", err => {
          console.error(err);
        });
        res.end(svg);
      });
  } else if (req.method === "GET" && req.url === "/shutdown") {
    MathJax.done();
    res.end("bye", () => {
      server.close();
    });
  }
}).listen(8080, "127.0.0.1");
