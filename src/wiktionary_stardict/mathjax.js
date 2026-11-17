import { createServer } from "node:http";
import MathJax from "mathjax";

await MathJax.init({
  loader: {
    load: ["input/tex", "output/svg"],
  },
  svg: {
    fontCache: "none",
  }
});

async function tex2svg(data) {
  const node = await MathJax.tex2svgPromise(
    data.body,
    { display: data.display },
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
        const svg = await tex2svg(JSON.parse(body));
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
  } else if (req.method === "GET" && req.url === "/health") {
    res.end();
  }
}).listen(8080, "127.0.0.1");
