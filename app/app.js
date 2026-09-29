const repo="Neurogma/neurotech-roadmaps";
const base="https://github.com/"+repo+"/blob/main/";
const data={
 roadmaps:[
  ["learn-bci","Learn BCI","Neuroscience + Python + signals","BCI","A capability-first path from foundations to practical brain-computer interface work."],
  ["neuroprosthetics","Neuroprosthetics","Physiology + engineering + control","Neuroprosthetics","A route into the engineering and biological concepts behind neuroprosthetic systems."],
  ["neuroethics","Neuroethics","Neuroscience + evidence appraisal","Ethics","Understand ethical questions around neural data, agency, privacy and emerging neurotechnology."],
  ["neural-interfaces","Neural Interfaces","Biosignals + control + embedded systems","Interfaces","Build the conceptual and engineering stack behind neural interfaces."],
  ["computational-neuroscience","Computational Neuroscience","Math + physiology + Python","Computation","Connect mathematical models, neural dynamics and computational experiments."],
  ["eeg","EEG","Measurement + signal processing","EEG","Learn the measurement chain, signal processing and interpretation of EEG."],
  ["neural-signal-processing","Neural Signal Processing","Math + probability + signals","Signals","Develop the signal-processing toolkit for neural data."],
  ["neuroimaging","Neuroimaging","Statistics + data organization","Imaging","Navigate neuroimaging concepts, data organization and quantitative analysis."],
  ["neural-data-science","Neural Data Science","Python + statistics","Data","Build a reproducible workflow for working with neural datasets."],
  ["neuromodulation","Neuromodulation","Physiology + experimental design","Modulation","Study the evidence and systems thinking around neuromodulation."],
 ],
 projects:[
  ["beginner","Signal visualization","Explore and communicate biosignal structure through a small, reproducible analysis."],
  ["beginner","PSD analysis","Estimate and interpret power spectral density from signal data."],
  ["beginner","Computational neuron simulation","Implement a compact neuron model and inspect its dynamics."],
  ["intermediate","EEG preprocessing","Build a defensible preprocessing pipeline and document its choices."],
  ["intermediate","Motor imagery pipeline","Create a signal-to-decoding workflow using public data."],
  ["intermediate","P300 analysis","Analyze event-related responses in a controlled public-data workflow."],
  ["intermediate","SSVEP analysis","Explore frequency-tagged neural responses and evaluation."],
  ["intermediate","Spike-train analysis","Quantify and visualize spiking activity."],
  ["intermediate","Simple neural decoding","Build a baseline decoder with transparent evaluation."],
  ["intermediate","Neuroimaging comparison","Compare modalities by signal, resolution, constraints and use cases."],
  ["intermediate","Closed-loop control simulation","Connect inference to a simulated control loop."],
  ["intermediate","Biosignal acquisition simulation","Model an acquisition chain without human-subject hardware."],
  ["intermediate","Artifact analysis","Identify and reason about common signal artifacts."],
  ["intermediate","Experiment protocol review","Critically review an experimental protocol for evidence and design."],
  ["advanced","Deep learning neural decoding","Explore representation learning for neural decoding with careful validation."],
  ["advanced","Neural interface software simulation","Architect a simulated end-to-end neural interface."],
  ["advanced","Neuroprosthetic control simulation","Connect decoding, control and evaluation in simulation."],
  ["research","Neural data science analysis","Run a research-style, reproducible analysis with explicit uncertainty."],
  ["research","Neuroethics policy brief","Synthesize evidence into a structured policy-facing argument."],
  ["research","Neuromodulation evidence review","Critically review a body of evidence and its limitations."]
 ],
 papers:[
  ["BCI2000","BCI2000","BCI systems and the software architecture around them."],
  ["BIDS","Brain Imaging Data Structure","Data organization, interoperability and reproducibility."],
  ["EEG-BIDS","EEG-BIDS","A focused guide to structuring EEG datasets."],
  ["Higashi / Tanaka CSTFP","Higashi & Tanaka — CSTFP","A paper guide connected to neural signal analysis."],
  ["Hodgkin–Huxley","Hodgkin–Huxley","A foundational computational model of neuronal dynamics."],
  ["MOABB 2018","MOABB 2018","Benchmarking and reproducible evaluation for BCI research."],
  ["P300 speller","P300 speller","A classic event-related BCI paradigm."],
  ["Speech neuroprosthesis","Speech neuroprosthesis","Neural decoding for speech-related communication."],
  ["Wolpaw BCI","Wolpaw BCI","A foundational perspective on brain-computer interfaces."]
 ],
 families:[
  ["Foundations","Math, probability, statistics, neuroscience and physiology.","foundations"],
  ["Signals","Signal processing, biosignals and EEG.","eeg"],
  ["BCI","BCI methods, paradigms and decoding.","bci"],
  ["Interfaces","Neural interfaces, embedded systems and control.","neural-interfaces"],
  ["Computation","Computational neuroscience and machine learning.","computational-neuroscience"],
  ["Data","Neural data science, organization and reproducibility.","neural-data-science"],
  ["Ethics","Neuroethics, evidence appraisal and policy.","ethics"],
  ["Modulation","Neuromodulation and evidence review.","neuromodulation"],
  ["Neuroprosthetics","Control and neuroprosthetic systems.","neuroprosthetics"]
 ]
};
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const progress=JSON.parse(localStorage.getItem("neurotech-progress")||"{}");
function esc(s){return String(s).replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[m]))}
function slug(s){return s.toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/(^-|-$)/g,"")}
function repoFile(path){return base+path}
function roadmapCard(r){return `<article class="roadmap-card"><div class="card-top"><span class="eyebrow">${esc(r[3])}</span><span class="pill">ROADMAP</span></div><h3>${esc(r[1])}</h3><p>${esc(r[4])}</p><div class="card-top"><span class="pill">${esc(r[2])}</span><a class="card-link" target="_blank" rel="noreferrer" href="${repoFile("roadmaps/"+r[0]+".md")}">Open source →</a></div></article>`}
function renderStats(){const totalNodes=13;$("#stats").innerHTML=[["10","goal roadmaps"],[totalNodes,"capability domains"],["20","evidence projects"],["9","paper guides"]].map(x=>`<div class="stat"><b>${x[0]}</b><span>${x[1]}</span></div>`).join("")}
function renderRoadmaps(list=data.roadmaps){$("#allRoadmaps").innerHTML=list.map(roadmapCard).join("")}
function renderFeatured(){ $("#featuredRoadmaps").innerHTML=data.roadmaps.slice(0,6).map(roadmapCard).join("")}
function renderProjects(filter="all"){let list=data.projects.filter(x=>filter==="all"||x[0]===filter);$("#projectGrid").innerHTML=list.map((x,i)=>`<article class="project-card"><span class="level">${x[0].toUpperCase()}</span><h3>${esc(x[1])}</h3><p>${esc(x[2])}</p><button class="card-link" data-project="${esc(x[1])}" data-project-level="${x[0]}">Inspect brief →</button></article>`).join("")}
function renderPapers(){$("#paperList").innerHTML=data.papers.map(x=>`<article class="paper-card"><div><h3>${esc(x[1])}</h3><div class="paper-meta">${esc(x[2])}</div></div><a class="card-link" target="_blank" rel="noreferrer" href="${repoFile("papers/paper-guides/paper-"+slug(x[0])+".yml")}">Guide →</a></article>`).join("")}
function renderLibrary(){$("#libraryGrid").innerHTML=[
 ["Roadmaps","Canonical goal-driven paths. Markdown is generated; YAML is the source of truth.","roadmaps/"],
 ["Nodes","Reusable capabilities and prerequisite relationships that form the learning graph.","nodes/"],
 ["Projects","Evidence-producing specifications, grouped by beginner, intermediate, advanced and research.","projects/"],
 ["Resources","Curated resource catalog with provenance, review state and maintenance intervals.","resources/catalog.yml"],
 ["Paper guides","Structured reading guides that connect primary literature to learning goals.","papers/paper-guides/"],
 ["Methodology","Data model, quality rules, provenance and how relationships are maintained.","docs/methodology.md"],
 ["Safety","Boundaries for clinical, invasive, stimulation and human-subject work.","docs/safety.md"],
 ["Reproducibility","Principles for making analysis and learning artifacts inspectable.","docs/reproducibility.md"]
].map(x=>`<article class="library-card"><span class="eyebrow">SOURCE LAYER</span><h3>${esc(x[0])}</h3><p>${esc(x[1])}</p><a target="_blank" rel="noreferrer" href="${repoFile(x[2])}">Open in GitHub ↗</a></article>`).join("")}
function renderGraph(){const box=$("#graph");box.innerHTML='<div class="graph-center">NEUROTECH<br><span style="font-size:9px;color:#8f96a8">CAPABILITY SYSTEM</span></div>';const pos=[[10,15],[39,9],[68,17],[78,43],[65,72],[36,79],[9,66],[20,40],[46,47]];data.families.forEach((f,i)=>{const n=document.createElement("button");n.className="graph-node";n.textContent=f[0];n.style.left=pos[i][0]+"%";n.style.top=pos[i][1]+"%";n.dataset.family=i;n.onclick=()=>showFamily(i);box.appendChild(n)});$("#skillTags").innerHTML=data.families.map((f,i)=>`<button class="tag" data-family="${i}">${esc(f[0])}</button>`).join("");$$("[data-family]").forEach(b=>b.onclick=()=>showFamily(+b.dataset.family))}
function showFamily(i){const f=data.families[i];$("#skillDetail").innerHTML=`<span class="eyebrow accent">CAPABILITY FAMILY</span><h2>${esc(f[0])}</h2><p>${esc(f[1])}</p><div class="tag-cloud"><span class="tag">Reusable node family</span><span class="tag">Prerequisites</span><span class="tag">Roadmap-connected</span></div><a class="card-link" target="_blank" rel="noreferrer" href="${repoFile("nodes/"+f[2]+"/")}">Explore source →</a>`}
function toast(msg){const t=$("#toast");t.textContent=msg;t.classList.add("show");setTimeout(()=>t.classList.remove("show"),1800)}
function showView(view){$$(".view").forEach(v=>v.classList.toggle("active",v.id==="view-"+view));$$(".nav-item").forEach(b=>b.classList.toggle("active",b.dataset.view===view));$("#crumb").textContent="Atlas / "+view[0].toUpperCase()+view.slice(1);history.replaceState(null,"","#"+view)}
function initNav(){$$("#nav .nav-item").forEach(b=>b.onclick=()=>{showView(b.dataset.view);$(".sidebar").classList.remove("open")});$$("[data-go]").forEach(b=>b.onclick=()=>showView(b.dataset.go));$("#mobileMenu").onclick=()=>$(".sidebar").classList.toggle("open");$("#focusSearch").onclick=()=>{showView("roadmaps");setTimeout(()=>$("#roadmapSearch").focus(),50)}}
$("#roadmapSearch").addEventListener("input",e=>{const q=e.target.value.toLowerCase();renderRoadmaps(data.roadmaps.filter(r=>r.join(" ").toLowerCase().includes(q)))});
$("#projectFilters").innerHTML=["all","beginner","intermediate","advanced","research"].map(x=>`<button class="filter ${x==="all"?"active":""}" data-filter="${x}">${x}</button>`).join("");
$$(".filter").forEach(b=>b.onclick=()=>{$$(".filter").forEach(x=>x.classList.remove("active"));b.classList.add("active");renderProjects(b.dataset.filter)});
$("#projectGrid").addEventListener("click",e=>{const b=e.target.closest("[data-project]");if(!b)return;$("#modalContent").innerHTML=`<span class="eyebrow accent">${b.dataset.projectLevel.toUpperCase()} PROJECT</span><h2>${esc(b.dataset.project)}</h2><p>This MVP exposes the project as an evidence-producing unit. The canonical specification, learning objectives, inputs, outputs and evaluation criteria remain in the repository.</p><a class="card-link" target="_blank" rel="noreferrer" href="${repoFile("projects/"+b.dataset.projectLevel+"/"+slug(b.dataset.project)+".yml")}">Open canonical specification →</a>`;$("dialog").showModal()});
$("#closeModal").onclick=()=>$("#modal").close();$("#modal").addEventListener("click",e=>{if(e.target===$("#modal"))$("#modal").close()});
$("#resetProgress").onclick=()=>{localStorage.removeItem("neurotech-progress");toast("Local progress reset")};
function init(){renderStats();renderFeatured();renderRoadmaps();renderProjects();renderPapers();renderLibrary();renderGraph();initNav();const h=location.hash.slice(1);if(["overview","roadmaps","skills","projects","papers","library"].includes(h))showView(h)}
init();