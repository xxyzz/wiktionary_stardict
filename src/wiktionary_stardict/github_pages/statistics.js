import Chart from "https://cdn.jsdelivr.net/npm/chart.js/auto/+esm";

window.addEventListener("pageshow", () => {
    document.querySelector("#edition").value = "en";
    document.querySelector("#en-select").value = "en";
});

document.getElementById("edition").addEventListener(
    "change",
    (event) => {
        document.querySelectorAll(".files").forEach(p => {
            const edition = event.target.value;
            if (p.id == edition + "-options") {
                p.classList.add("active-option");
                const lemma_code = edition == "simple" ? "en" : edition;
                p.querySelector("select").value = lemma_code;
                load_chart(lemma_code);
            } else {
                p.classList.remove("active-option");
            }
        });
    }
);
document.querySelectorAll(".language-options").forEach(label => {
    label.addEventListener(
        "change", (event) => load_chart(event.target.value.replace(/-select$/, ""))
    )
})

const tag = document.querySelector("#date").textContent;
const cacheName = `wiktionary_stardict_${tag}`

async function load_data(lemma_code, gloss_code) {
    const cacheStorage = await caches.open(cacheName);
    let response = await cacheStorage.match(gloss_code);
    if (!response || !response.ok) {
        response = await fetch(`./${gloss_code}.gz`);
        await cacheStorage.put(gloss_code, response.clone());
    }
    const decompressedStream = response.body.pipeThrough(
        new DecompressionStream("gzip")
    );
    return JSON.parse(await new Response(decompressedStream).text());
}

let chart;

async function load_chart(lemma_code) {
    const gloss_code = document.getElementById("edition").value;
    const edition_data = await load_data(lemma_code, gloss_code);
    const lemma_data = edition_data[lemma_code];
    const chartData = {
        labels: lemma_data.map(d => d["date"]),
        datasets: [
            {
                label: "Entry count",
                data: lemma_data.map(d => d["wordcount"]),
                yAxisID: "yWords"
            },
            {
                label: "Syn count",
                data: lemma_data.map(d => d["synwordcount"]),
                yAxisID: "yWords"
            },
            {
                label: "File size",
                data: lemma_data.map(d => Math.floor(d["filesize"] / 1000)),
                yAxisID: "ySize"
            }
        ]
    };

    if (chart) {
        chart.data = chartData;
        chart.update()
    } else {
        chart = new Chart(
            document.getElementById("chart"),
            {
                type: "line",
                data: chartData,
                options: {
                    scales: {
                        yWords: {
                            position: "left",
                            title: {
                                display: true,
                                text: "Entry count"
                            },
                            grace: "10%"
                        },
                        ySize: {
                            position: "right",
                            title: {
                                display: true,
                                text: "File size(KB)"
                            },
                            grace: "10%"
                        }
                    }
                }
            }
        );
    }
}

const cacheNames = await caches.keys();
await Promise.all(
    cacheNames
        .filter(name => name !== cacheName)
        .map(name => caches.delete(name))
);
await load_chart("en");
