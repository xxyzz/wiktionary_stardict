import Chart from "https://cdn.jsdelivr.net/npm/chart.js/auto/+esm";

document.getElementById("edition").addEventListener(
  "change",
  (event) => {
    document.querySelectorAll(".files").forEach((p) => {
      const edition = event.target.value;
      if (p.id == edition + "-options") {
        p.hidden = false;
        const lemma_code = edition == "simple" ? "en" : edition;
        p.querySelector("select").value = lemma_code;
        load_chart(lemma_code);
      } else {
        p.hidden = true;
      }
    });
  },
);
document.querySelectorAll(".language-options").forEach((label) => {
  label.addEventListener(
    "change",
    (event) => load_chart(event.target.value.replace(/-select$/, "")),
  );
});

const tag = document.querySelector("#date").textContent;
const cacheName = `wiktionary_stardict_${tag}`;

async function load_data(gloss_code) {
  const cacheStorage = await caches.open(cacheName);
  let response = await cacheStorage.match(gloss_code);
  if (!response || !response.ok) {
    response = await fetch(`./${gloss_code}.gz`);
    await cacheStorage.put(gloss_code, response.clone());
  }
  const decompressedStream = response.body.pipeThrough(
    new DecompressionStream("gzip"),
  );
  return JSON.parse(await new Response(decompressedStream).text());
}

let chart;

function calculateChange(list) {
  return list.map((value, index) => {
    if (index == 0) {
      return 0;
    }
    const preValue = list[index - 1];
    return Math.floor(((value - preValue) / preValue) * 100);
  });
}

async function load_chart(lemma_code) {
  const gloss_code = document.getElementById("edition").value;
  const edition_data = await load_data(gloss_code);
  const lemma_data = edition_data[lemma_code];
  const chartData = {
    labels: lemma_data.map((d) => d["date"]),
    datasets: [
      {
        label: "Entries",
        data: calculateChange(lemma_data.map((d) => d["wordcount"])),
        originData: lemma_data.map((d) => d["wordcount"]),
      },
      {
        label: "Forms",
        data: calculateChange(lemma_data.map((d) => d["synwordcount"])),
        originData: lemma_data.map((d) => d["synwordcount"]),
      },
      {
        label: "File size(KB)",
        data: calculateChange(lemma_data.map((d) => Math.floor(d["filesize"] / 1000))),
        originData: lemma_data.map((d) => Math.floor(d["filesize"] / 1000)),
      },
    ],
  };

  if (chart) {
    chart.data = chartData;
    chart.update();
  } else {
    chart = new Chart(
      document.getElementById("chart"),
      {
        type: "line",
        data: chartData,
        options: {
          scales: {
            y: {
              title: {
                display: true,
                text: "Percentage change",
              },
              ticks: {
                callback: (value) => `${value}%`,
              },
            },
          },
          plugins: {
            tooltip: {
              callbacks: {
                label: (context) => {
                  const dataset = context.dataset;
                  const index = context.dataIndex;
                  return [
                    `Change: ${Math.floor(dataset.data[index])}%`,
                    `${dataset.label}: ${dataset.originData[index]}`,
                  ];
                },
              },
            },
          },
        },
      },
    );
  }
}

const cacheNames = await caches.keys();
await Promise.all(
  cacheNames
    .filter((name) => name !== cacheName)
    .map((name) => caches.delete(name)),
);
await load_chart("en");
