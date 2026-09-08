import MathJax from "mathjax";
await MathJax.init({
  loader: {
    load: ["input/tex", "output/svg"],
  },
  svg: {
    fontCache: "none",
  },
});

async function tex2svg(input: string): Promise<string> {
  const node = await MathJax.tex2svgPromise(
    input,
    { display: true },
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
