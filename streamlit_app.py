import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Review → Prediksi Bintang (Prototype)", page_icon="⭐", layout="wide")

HTML = r"""
<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Review → Prediksi Bintang (Prototype)</title>
  <style>
    :root{
      --bg:#0b1220; --card:#111a2e; --muted:#8ea0c7; --text:#e9efff;
      --accent:#7aa2ff; --accent2:#67e8f9; --danger:#ff6b6b; --ok:#34d399;
      --border: rgba(255,255,255,.08);
      --shadow: 0 18px 60px rgba(0,0,0,.35);
      --radius: 18px;
      --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      --sans: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji";
    }
    *{box-sizing:border-box}
    body{
      margin:0; font-family:var(--sans); color:var(--text); background:
        radial-gradient(1200px 600px at 20% 0%, rgba(122,162,255,.25), transparent 55%),
        radial-gradient(900px 500px at 100% 10%, rgba(103,232,249,.20), transparent 55%),
        radial-gradient(700px 400px at 40% 100%, rgba(52,211,153,.12), transparent 60%),
        var(--bg);
      min-height:100vh;
      display:flex; align-items:center; justify-content:center;
      padding:26px;
    }
    .wrap{width:min(1100px, 100%)}
    header{
      display:flex; align-items:flex-start; justify-content:space-between; gap:16px;
      margin-bottom:18px;
    }
    .title{
      display:flex; flex-direction:column; gap:6px;
    }
    h1{margin:0; font-size:22px; letter-spacing:.2px}
    .subtitle{color:var(--muted); font-size:13px; line-height:1.4}
    .badge{
      font-family:var(--mono); font-size:12px; color:rgba(255,255,255,.85);
      background:rgba(255,255,255,.06); border:1px solid var(--border);
      padding:8px 10px; border-radius:999px;
      display:flex; gap:8px; align-items:center;
      white-space:nowrap;
    }
    .grid{
      display:grid;
      grid-template-columns: 1.2fr .8fr;
      gap:16px;
    }
    @media (max-width: 900px){
      .grid{grid-template-columns:1fr}
    }
    .card{
      background: linear-gradient(180deg, rgba(255,255,255,.04), rgba(255,255,255,.02));
      border:1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding:16px;
    }
    .card h2{
      margin:0 0 10px 0;
      font-size:14px; font-weight:650; letter-spacing:.2px;
    }
    textarea{
      width:100%;
      min-height:200px;
      resize:vertical;
      padding:12px 12px;
      font-family:var(--sans);
      color:var(--text);
      background:rgba(0,0,0,.25);
      border:1px solid var(--border);
      border-radius:14px;
      outline:none;
      line-height:1.45;
    }
    textarea:focus{border-color:rgba(122,162,255,.45); box-shadow:0 0 0 4px rgba(122,162,255,.10)}
    .row{display:flex; gap:10px; flex-wrap:wrap; margin-top:12px}
    .field{
      flex:1;
      min-width:160px;
      display:flex; flex-direction:column; gap:6px;
    }
    .label{color:var(--muted); font-size:12px}
    input[type="number"], input[type="datetime-local"]{
      width:100%;
      padding:10px 10px;
      color:var(--text);
      background:rgba(0,0,0,.25);
      border:1px solid var(--border);
      border-radius:12px;
      outline:none;
    }
    input:focus{border-color:rgba(122,162,255,.45); box-shadow:0 0 0 4px rgba(122,162,255,.10)}
    .btns{display:flex; gap:10px; margin-top:14px; flex-wrap:wrap}
    button{
      border:none; cursor:pointer;
      padding:11px 14px;
      border-radius:14px;
      font-weight:650;
      color:var(--text);
      background: rgba(122,162,255,.25);
      border:1px solid rgba(122,162,255,.35);
      transition: transform .08s ease, background .2s ease, border-color .2s ease;
    }
    button:hover{background: rgba(122,162,255,.32); border-color: rgba(122,162,255,.55)}
    button:active{transform: translateY(1px)}
    .secondary{
      background: rgba(255,255,255,.06);
      border:1px solid var(--border);
      color: rgba(255,255,255,.9);
    }
    .secondary:hover{background: rgba(255,255,255,.08)}
    .status{
      margin-top:10px;
      font-size:12px; color:var(--muted);
      display:flex; gap:8px; align-items:center;
      min-height:18px;
    }
    .dot{
      width:8px; height:8px; border-radius:999px;
      background: rgba(255,255,255,.25);
    }
    .dot.ok{background: var(--ok)}
    .dot.bad{background: var(--danger)}
    .dot.work{
      background: var(--accent2);
      box-shadow: 0 0 0 0 rgba(103,232,249,.5);
      animation: pulse 1.2s infinite;
    }
    @keyframes pulse{
      0%{box-shadow:0 0 0 0 rgba(103,232,249,.45)}
      70%{box-shadow:0 0 0 10px rgba(103,232,249,0)}
      100%{box-shadow:0 0 0 0 rgba(103,232,249,0)}
    }
    .resultTop{
      display:flex; align-items:center; justify-content:space-between; gap:12px;
      margin-bottom:10px;
    }
    .stars{
      display:flex; gap:6px; align-items:center;
      font-size:20px;
    }
    .star{
      width:22px; height:22px; display:inline-block;
      filter: drop-shadow(0 10px 20px rgba(0,0,0,.35));
    }
    .scoreBox{
      font-family:var(--mono);
      font-size:12px;
      padding:8px 10px;
      border-radius:12px;
      background: rgba(0,0,0,.28);
      border:1px solid var(--border);
      color: rgba(255,255,255,.9);
      white-space:nowrap;
    }
    .bars{display:flex; flex-direction:column; gap:8px; margin-top:12px}
    .barRow{display:grid; grid-template-columns: 34px 1fr 54px; gap:10px; align-items:center}
    .barLabel{color:rgba(255,255,255,.86); font-size:12px; font-family:var(--mono)}
    .barTrack{
      height:10px; border-radius:999px;
      background: rgba(255,255,255,.08);
      overflow:hidden; border:1px solid var(--border);
    }
    .barFill{height:100%; width:0%}
    .barPct{color:var(--muted); font-size:12px; text-align:right; font-family:var(--mono)}
    .note{
      margin-top:12px;
      color:var(--muted);
      font-size:12px;
      line-height:1.45;
    }
    .pill{
      display:inline-flex; align-items:center; gap:8px;
      padding:8px 10px;
      border-radius:999px;
      background: rgba(0,0,0,.22);
      border: 1px solid var(--border);
      font-size:12px;
      color: rgba(255,255,255,.88);
      font-family: var(--mono);
    }
    .mono{font-family:var(--mono)}
    .small{font-size:12px; color:var(--muted); line-height:1.5}
    .hr{height:1px; background:var(--border); margin:12px 0}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="title">
        <h1>Review → Prediksi Bintang (1–5)</h1>
        <div class="subtitle">
          Prototype front-end untuk memprediksi rating Yelp dari teks review + metadata.
          <span class="mono">Dummy mode</span> (selalu 4★).
        </div>
      </div>
      <div class="badge" id="modeBadge">MODE: <span id="modeText">OFFLINE-DUMMY</span></div>
    </header>

    <div class="grid">
      <!-- Left: Input -->
      <div class="card">
        <h2>Input Review</h2>
        <textarea id="reviewText" placeholder="Tempel / ketik review di sini..."></textarea>

        <div class="row">
          <div class="field">
            <div class="label">Useful (votes)</div>
            <input id="useful" type="number" min="0" step="1" value="0" />
          </div>
          <div class="field">
            <div class="label">Funny (votes)</div>
            <input id="funny" type="number" min="0" step="1" value="0" />
          </div>
          <div class="field">
            <div class="label">Cool (votes)</div>
            <input id="cool" type="number" min="0" step="1" value="0" />
          </div>
          <div class="field">
            <div class="label">Date (optional)</div>
            <input id="date" type="datetime-local" />
          </div>
        </div>

        <div class="btns">
          <button id="predictBtn">Prediksi Bintang</button>
          <button class="secondary" id="fillExampleBtn">Isi Contoh</button>
          <button class="secondary" id="clearBtn">Reset</button>
        </div>

        <div class="status" id="status">
          <span class="dot" id="statusDot"></span>
          <span id="statusText">Siap. Klik “Prediksi Bintang”.</span>
        </div>

        <div class="hr"></div>
        <div class="small">
          <div class="pill">MODE: <span id="apiUrlText">Dummy (always 4★)</span></div>
          <div class="note">
            Nanti kalau backend model sudah siap, kamu bisa ganti JS untuk fetch ke API.
          </div>
        </div>
      </div>

      <!-- Right: Output -->
      <div class="card">
        <div class="resultTop">
          <h2 style="margin:0">Hasil Prediksi</h2>
          <div class="scoreBox" id="modelBox">model: dummy_always_4</div>
        </div>

        <div class="stars" id="starsRow" aria-label="Predicted stars"></div>
        <div class="bars" id="probBars"></div>

        <div class="note" id="explain">
          Ini dummy mode: prediksi selalu 4★, distribusi hanya simulasi.
        </div>

        <div class="hr"></div>
        <div class="small">
          Kamu bisa pakai layout ini untuk deploy, lalu sambungkan ke backend API (FastAPI/Flask) nanti.
        </div>
      </div>
    </div>
  </div>

  <script>
    const MODE = "OFFLINE-DUMMY";

    // UI refs
    const elText = document.getElementById("reviewText");
    const elUseful = document.getElementById("useful");
    const elFunny = document.getElementById("funny");
    const elCool = document.getElementById("cool");
    const elDate = document.getElementById("date");

    const elPredictBtn = document.getElementById("predictBtn");
    const elFillExampleBtn = document.getElementById("fillExampleBtn");
    const elClearBtn = document.getElementById("clearBtn");

    const elStatusDot = document.getElementById("statusDot");
    const elStatusText = document.getElementById("statusText");

    const elStarsRow = document.getElementById("starsRow");
    const elProbBars = document.getElementById("probBars");
    const elModelBox = document.getElementById("modelBox");

    function setStatus(type, msg){
      elStatusDot.className = "dot";
      if(type === "ok") elStatusDot.classList.add("ok");
      if(type === "bad") elStatusDot.classList.add("bad");
      if(type === "work") elStatusDot.classList.add("work");
      elStatusText.textContent = msg;
    }

    function starSVG(filled=true){
      const fill = filled ? "rgba(122,162,255,.95)" : "rgba(255,255,255,.16)";
      return `
        <svg class="star" viewBox="0 0 24 24" aria-hidden="true">
          <path fill="${fill}" d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
        </svg>
      `;
    }

    function renderStars(stars){
      const s = Math.max(1, Math.min(5, Math.round(stars)));
      let html = `<div class="scoreBox">pred: <b>${s}★</b></div>`;
      html += `<div style="display:flex; gap:6px; margin-left:8px;">`;
      for(let i=1;i<=5;i++) html += starSVG(i<=s);
      html += `</div>`;
      elStarsRow.innerHTML = html;
    }

    function renderBars(probs){
      const p = probs.slice(0,5).map(x => Math.max(0, Number(x)||0));
      const sum = p.reduce((a,b)=>a+b,0) || 1;
      const pn = p.map(x => x/sum);

      let html = "";
      for(let i=0;i<5;i++){
        const pct = Math.round(pn[i]*100);
        html += `
          <div class="barRow">
            <div class="barLabel">${i+1}★</div>
            <div class="barTrack"><div class="barFill" style="width:${pct}%; background:rgba(103,232,249,.65)"></div></div>
            <div class="barPct">${pct}%</div>
          </div>
        `;
      }
      elProbBars.innerHTML = html;
    }

    // DUMMY: selalu 4 bintang + prob simulasi
    function dummyPredict(){
      return {
        stars: 4,
        probs: [0.02, 0.06, 0.12, 0.52, 0.28],
        model: "dummy_always_4"
      };
    }

    elPredictBtn.addEventListener("click", async () => {
      const text = (elText.value || "").trim();
      if(!text){
        setStatus("bad", "Review text masih kosong.");
        return;
      }
      setStatus("work", "Memproses prediksi (dummy)...");
      elPredictBtn.disabled = true;

      try{
        const out = dummyPredict();
        elModelBox.textContent = `model: ${out.model}`;
        renderStars(out.stars);
        renderBars(out.probs);
        setStatus("ok", "Selesai. (Dummy selalu 4★)");
      } catch(err){
        setStatus("bad", `Gagal: ${err.message}`);
      } finally {
        elPredictBtn.disabled = false;
      }
    });

    elFillExampleBtn.addEventListener("click", () => {
      elText.value = "Had a party of 6 here for hibachi. The waitress was friendly and the food was delicious. Great experience — would recommend!";
      elUseful.value = 1;
      elFunny.value = 0;
      elCool.value = 1;
      setStatus("ok", "Contoh diisi. Klik “Prediksi Bintang”.");
    });

    elClearBtn.addEventListener("click", () => {
      elText.value = "";
      elUseful.value = 0;
      elFunny.value = 0;
      elCool.value = 0;
      elDate.value = "";
      renderStars(0);
      renderBars([0,0,0,0,0]);
      elModelBox.textContent = "model: dummy_always_4";
      setStatus("ok", "Form di-reset.");
    });

    // default render
    renderStars(0);
    renderBars([0,0,0,0,0]);
  </script>
</body>
</html>
"""

# Height bisa kamu naik/turunin sesuai kebutuhan
components.html(HTML, height=860, scrolling=True)
