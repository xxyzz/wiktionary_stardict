import MathJax from "mathjax";
await MathJax.init({
  loader: {
    load: ["input/tex", "output/svg"],
  },
  svg: {
    fontCache: "none",
    postFilters: [
      ({data}) => {
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
              const value = fixed(Number(match[1]) * pxPerEm / 1000);
              adaptor.setAttribute(svg, "style", `vertical-align: ${value}px`);
            }
          }
        }
      }
    ]
  },
});

async function tex2svg(input: string): Promise<string> {
  const node = await MathJax.tex2svgPromise(
    input,
    { display: true, em: 36, ex: 18 },
  );
  return MathJax.startup.adaptor.serializeXML(node);
}

const server = Deno.serve(
  { hostname: "127.0.0.1", port: 8080 },
  async (req) => {
    const pathname = new URL(req.url).pathname;
    if (req.method === "POST" && pathname === "/tex2svg") {
      const svg = await tex2svg(await req.text());
      return new Response(svg);
    } else if (req.method === "GET" && pathname === "/shutdown") {
      MathJax.done();
      setTimeout(() => {
        server.shutdown();
      }, 0);
      return new Response("bye");
    }
  },
);
