import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Review → Prediksi Bintang (Prototype)",
    page_icon="⭐",
    layout="wide"
)

# Optional: kalau suatu saat mau sambung API, set env var API_URL di Streamlit Cloud secrets/env
API_URL = os.getenv("API_URL", "").strip()

# Hilangkan padding default streamlit biar "full page" look
st.markdown(
    """
    <style>
      .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
      iframe {border: 0 !important;}
    </style>
    """,
    unsafe_allow_html=True
)

HTML = rf"""
<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Review → Prediksi Bintang (Prototype)</title>
  <style>
    :root{{
      --bg:#0b1220; --card:#111a2e; --muted:#8ea0c7; --text:#e9efff;
      --accent:#7aa2ff; --accent2:#67e8f9; --danger:#ff6b6b; --ok:#34d399;
      --border: rgba(255,255,255,.08);
      --shadow: 0 18px 60px rgba(0,0,0,.35);
      --radius: 18px;
      --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      --sans: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji";
    }}
    *{{box-sizing:border-box}}
    body{{
      margin:0; font-family:var(--sans); color:var(--text); background:
        radial-gradient(1200px 600px at 20% 0%, rgba(122,162,255,.25), transparent 55%),
        radial-gradient(900px 500px at 100% 10%, rgba(103,232,249,.20), transparent 55%),
        radial-gradient(700px 400px at 40% 100%, rgba(52,211,153,.12), transparent 60%),
        var(--bg);
      min-height:100vh;
      display:flex; align-items:center; justify-content:center;
      padding:26px;
    }}
    .wrap{{width:min(1100px, 100%)}}
    header{{
      display:flex; align-items:flex-start; justify-content:space-between; gap:16px;
      margin-bottom:18px;
    }}
    .title{{display:flex; flex-direction:column; gap:6px;}}
    h1{{margin:0; font-size:22px; letter-spacing:.2px}}
    .subtitle{{color:var(--muted); font-size:13px; line-height:1.4}}
    .badge{{
      font-family:var(--mono); font-size:12px; color:rgba(255,255,255,.85);
      background:rgba(255,255,255,.06); border:1px solid var(--border);
      padding:8px 10px; border-radius:999px;
      display:flex; gap:8px; align-items:center;
      white-space:nowrap;
    }}
    .grid{{
      display:grid;
      grid-template-columns: 1.2fr .8fr;
      gap:16px;
    }}
    @media (max-width: 900px){{ .grid{{grid-template-columns:1fr}} }}
    .card{{
      background: linear-gradient(180deg, rgba(255,255,255,.04), rgba(255,255,255,.02));
      border:1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding:16px;
    }}
    .card h2{{margin:0 0 10px 0; font-size:14px; font-weight:650; letter-spacing:.2px;}}
    textarea{{
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
    }}
    textarea:focus{{border-color:rgba(122,162,255,.45); box-shadow:0 0 0 4px rgba(122,162,255,.10)}}
    .row{{display:flex; gap:10px; flex-wrap:wrap; margin-top:12px}}
    .field{{flex:1; min-width:160px; display:flex; flex-direction:column; gap:6px;}}
    .label{{color:var(--muted); font-size:12px}}
    input[type="number"], input[type="datetime-local"]{{
      width:100%;
      padding:10px 10px;
      color:var(--text);
      background:rgba(0,0,0,.25);
      border:1px solid var(--border);
      border-radius:12px;
      outline:none;
    }}
    input:focus{{border-color:rgba(122,162,255,.45); box-shadow:0 0 0 4px rgba(122,162,255,.10)}}
    .btns{{display:flex; gap:10px; margin-top:14px; flex-wrap:wrap}}
    button{{
      border:none; cursor:pointer;
      padding:11px 14px;
      border-radius:14px;
      font-weight:650;
      color:var(--text);
      background: rgba(122,162,255,.25);
      border:1px solid rgba(122,162,255,.35);
      transition: transform .08s ease, background .2s ease, border-color .2s ease;
    }}
    button:hover{{background: rgba(122,162,255,.32); border-color: rgba(122,162,255,.55)}}
    button:active{{transform: translateY(1px)}}
    .secondary{{background: rgba(255,255,255,.06); border:1px solid var(--border); color: rgba(255,255,255,.9);}}
    .secondary:hover{{background: rgba(255,255,255,.08)}}
    .status{{
      margin-top:10px;
      font-size:12px; color:var(--muted);
      display:flex; gap:8px; align-items:center;
      min-height:18px;
    }}
    .dot{{width:8px; height:8px; border-radius:999px; background: rgba(255,255,255,.25);}}
    .dot.ok{{background: var(--ok)}}
    .dot.bad{{background: var(--danger)}}
    .dot.work{{
      background: var(--accent2);
      box-shadow: 0 0 0 0 rgba(103,232,249,.5);
      animation: pulse 1.2s infinite;
    }}
    @keyframes pulse{{
      0%{{box-shadow:0 0 0 0 rgba(103,232,249,.45)}}
      70%{{box-shadow:0 0 0 10px rgba(103,232,249,0)}}
      100%{{box-shadow:0 0 0 0 rgba(103,232,249,0)}}
    }}
    .resultTop{{display:flex; align-items:center; justify-content:space-between; gap:12px; margin-bottom:10px;}}
    .stars{{display:flex; gap:6px; align-items:center; font-size:20px;}}
    .star{{width:22px; height:22px; display:inline-block; filter: drop-shadow(0 10px 20px rgba(0,0,0,.35));}}
    .scoreBox{{
      font-family:var(--mono);
      font-size:12px;
      padding:8px 10px;
      border-radius:12px;
      background: rgba(0,0,0,.28);
      border:1px solid var(--border);
      color: rgba(255,255,255,.9);
      white-space:nowrap;
    }}
    .bars{{display:flex; flex-direction:column; gap:8px; margin-top:12px}}
    .barRow{{display:grid; grid-template-columns: 34px 1fr 54px; gap:10px; align-items:center}}
    .barLabel{{color:rgba(255,255,255,.86); font-size:12px; font-family:var(--mono)}}
    .barTrack{{height:10px; border-radius:999px; background: rgba(255,255,255,.08); overflow:hidden; border:1px solid var(--border);}}
    .barFill{{height:100%; width:0%}}
    .barPct{{color:var(--muted); font-size:12px; text-align:right; font-family:var(--mono)}}
    .note{{margin-top:12px; color:var(--muted); font-size:12px; line-height:1.45;}}
    .pill{{
      display:inline-flex; align-items:center; gap:8px;
      padding:8px 10px;
      border-radius:999px;
      background: rgba(0,0,0,.22);
      border: 1px solid var(--border);
      font-size:12px;
      color: rgba(255,255,255,.88);
      font-family: var(--mono);
    }}
    .mono{{font-family:var(--mono)}}
    .small{{font-size:12px; color:var(--muted); line-height:1.5}}
    .hr{{height:1px; background:var(--border); margin:12px 0}}
    .explainBox{{
      margin-top:12px;
      padding:10px 12px;
      border:1px solid var(--border);
      border-radius:12px;
      background:rgba(0,0,0,.22);
      font-family:var(--mono);
      font-size:12px;
      color:rgba(255,255,255,.85);
      white-space:pre-wrap;
      line-height:1.45;
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="title">
        <h1>Review → Prediksi Bintang (1–5)</h1>
        <div class="subtitle">
          Prototype front-end untuk memprediksi rating Yelp dari teks review + metadata.
          Mode <span class="mono">{'API' if API_URL else 'OFFLINE-HEURISTIC'}</span>.
        </div>
      </div>
      <div class="badge" id="modeBadge">MODE: <span id="modeText">-</span></div>
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
          <div class="pill">API_URL: <span id="apiUrlText">-</span></div>
          <div class="note">
            Saat ini memakai heuristic scoring (rule-based) agar terasa seperti model.
            Jika kamu set <span class="mono">API_URL</span>, tombol akan memanggil API backend.
          </div>
        </div>
      </div>

      <!-- Right: Output -->
      <div class="card">
        <div class="resultTop">
          <h2 style="margin:0">Hasil Prediksi</h2>
          <div class="scoreBox" id="modelBox">model: -</div>
        </div>

        <div class="stars" id="starsRow" aria-label="Predicted stars"></div>
        <div class="bars" id="probBars"></div>

        <div class="note" id="explain">
          Output menampilkan prediksi bintang dan pseudo “confidence distribution”.
          Ini bukan model ML, tapi rule-based yang meniru perilaku scoring model.
        </div>

        <div class="explainBox" id="explainBox">details: -</div>

        <div class="hr"></div>
        <div class="small">
          <div><span class="mono">Contract API</span> (opsional):</div>
          <pre class="mono" style="margin:8px 0 0 0; padding:10px; border:1px solid var(--border); border-radius:12px; background:rgba(0,0,0,.25); overflow:auto;">
POST /predict
{{
  "text": "...",
  "useful": 0,
  "funny": 0,
  "cool": 0,
  "date": "2016-07-25 07:31:06"
}}

Response:
{{
  "stars": 4,
  "probs": [0.02, 0.05, 0.12, 0.46, 0.35],
  "model": "your_model_name",
  "details": "optional string"
}}
          </pre>
        </div>
      </div>
    </div>
  </div>

  <script>
    // ============================
    // CONFIG (API optional)
    // ============================
    const API_URL = "{API_URL}";
    const MODE = API_URL ? "API" : "OFFLINE-HEURISTIC";

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
    const elModeText = document.getElementById("modeText");
    const elModelBox = document.getElementById("modelBox");
    const elApiUrlText = document.getElementById("apiUrlText");
    const elExplainBox = document.getElementById("explainBox");

    elModeText.textContent = MODE;
    elApiUrlText.textContent = API_URL || "Tidak diset";

    function setStatus(type, msg){
      elStatusDot.className = "dot";
      if(type === "ok") elStatusDot.classList.add("ok");
      if(type === "bad") elStatusDot.classList.add("bad");
      if(type === "work") elStatusDot.classList.add("work");
      elStatusText.textContent = msg;
    }

    // ----- Stars render
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

    // ============================
    // OFFLINE HEURISTIC "pseudo-model"
    // ============================
    // Weighted lexicon (simple but feels "model-ish")
    const POS = {{
      "amazing":2.2,"awesome":2.1,"excellent":2.2,"perfect":2.2,"fantastic":2.1,"wonderful":2.0,"superb":2.0,
      "love":2.0,"loved":2.0,"lovely":1.7,"best":1.8,"great":1.6,"good":1.1,"nice":1.0,
      "delicious":1.8,"tasty":1.6,"yummy":1.5,"fresh":1.3,"clean":1.2,"friendly":1.4,"fast":1.0,
      "recommend":1.4,"recommended":1.4,"helpful":1.2,"pleasant":1.2,"cozy":1.0,"value":1.0
    }};
    const NEG = {{
      "worst":2.3,"awful":2.2,"terrible":2.2,"horrible":2.2,"disgusting":2.1,
      "hate":2.0,"hated":2.0,"bad":1.4,"poor":1.4,"rude":1.7,"dirty":1.6,"slow":1.3,
      "overpriced":1.3,"waste":1.6,"cold":1.2,"stale":1.3,"mediocre":1.2,
      "unfriendly":1.6,"problem":1.1,"bugs":1.2,"disappointed":1.7,"disappointing":1.7,"never":0.6
    }};
    const INTENS = {{"very":1.25,"really":1.2,"super":1.25,"extremely":1.35,"so":1.12}};
    const NEGATORS = new Set(["not","no","never","dont","don't","didnt","didn't","isnt","isn't","wasnt","wasn't","cant","can't","won't","wont","cannot"]);

    function tokenize(text){
      return (text||"")
        .toLowerCase()
        .replace(/[^a-z0-9\s']/g, " ")
        .split(/\s+/)
        .filter(Boolean);
    }

    function softmax(arr){
      const m = Math.max(...arr);
      const ex = arr.map(v => Math.exp(v - m));
      const s = ex.reduce((a,b)=>a+b,0) || 1;
      return ex.map(v => v/s);
    }

    function clamp(v, lo, hi){ return Math.max(lo, Math.min(hi, v)); }

    function heuristicPredict(payload){
      const text = payload.text || "";
      const tokens = tokenize(text);
      const n = tokens.length;

      // counts / features
      const excl = (text.match(/!/g) || []).length;
      const quest = (text.match(/\?/g) || []).length;

      // vote effect (log)
      const v_use = Math.log1p(payload.useful || 0);
      const v_fun = Math.log1p(payload.funny || 0);
      const v_cool= Math.log1p(payload.cool || 0);
      const vote_score = 0.70*(v_use + 0.85*v_cool) - 0.35*v_fun;

      // lexicon score with negation + intensity window
      let pos=0, neg=0;
      let s_pos=0, s_neg=0;

      for(let i=0;i<tokens.length;i++){
        const w = tokens[i];
        const prev = tokens[i-1] || "";
        const prev2 = tokens[i-2] || "";

        const intens = (INTENS[prev] || 1.0) * (INTENS[prev2] || 1.0);
        const negated = NEGATORS.has(prev) || NEGATORS.has(prev2);

        if(POS[w]){
          pos++;
          let val = POS[w] * intens;
          if(negated) { s_neg += 0.9*val; neg++; }
          else s_pos += val;
        }
        if(NEG[w]){
          neg++;
          let val = NEG[w] * intens;
          if(negated) { s_pos += 0.8*val; pos++; }
          else s_neg += val;
        }
      }

      // length & punctuation effects
      const len_bonus = 0.015 * Math.min(n, 260);       // panjang review
      const excl_bonus = 0.10 * Math.min(excl, 12);     // excitement
      const quest_pen  = 0.08 * Math.min(quest, 10);    // uncertainty/complaint-ish

      // raw score
      const raw = (s_pos - 1.15*s_neg) + len_bonus + excl_bonus - quest_pen + vote_score;

      // convert raw -> star distribution (pseudo calibration)
      // centers tuned to give reasonable mapping
      const centers = [-3.0, -1.4, 0.0, 1.6, 3.2];  // for 1..5
      const temp = 1.35;
      const logits = centers.map(c => -Math.abs(raw - c)/temp);
      const probs = softmax(logits);

      // expected star
      let expStar = 0;
      for(let k=0;k<5;k++) expStar += probs[k]*(k+1);

      // discrete stars with slight "rounding bias" (more stable)
      const stars = clamp(Math.round(expStar + 0.05), 1, 5);

      // confidence proxy (top prob)
      const pmax = Math.max(...probs);
      const details =
`tokens=${n}
pos_terms=${pos} (score=${s_pos.toFixed(2)})
neg_terms=${neg} (score=${s_neg.toFixed(2)})
votes: useful=${payload.useful} funny=${payload.funny} cool=${payload.cool} (vote_score=${vote_score.toFixed(2)})
punct: !=${excl} ?=${quest}
raw_score=${raw.toFixed(3)}
E[stars]=${expStar.toFixed(3)}  maxP=${pmax.toFixed(3)}`;

      return {{
        stars,
        probs,
        model: "heuristic_rulebase_v1",
        details
      }};
    }

    // ============================
    // API predict (optional)
    // ============================
    async function apiPredict(payload){
      const res = await fetch(API_URL, {{
        method: "POST",
        headers: {{"Content-Type":"application/json"}},
        body: JSON.stringify(payload)
      }});
      if(!res.ok){{
        const txt = await res.text().catch(()=> "");
        throw new Error(`API error ${{res.status}}: ${{txt || res.statusText}}`);
      }}
      const data = await res.json();
      if(typeof data.stars !== "number") throw new Error("Invalid API response: missing 'stars'");
      if(!Array.isArray(data.probs) || data.probs.length !== 5) throw new Error("Invalid API response: 'probs' must be length 5");
      return data;
    }

    function getPayload(){
      const useful = Number(elUseful.value || 0);
      const funny  = Number(elFunny.value || 0);
      const cool   = Number(elCool.value || 0);
      const dateLocal = elDate.value ? new Date(elDate.value) : null;

      let dateStr = null;
      if(dateLocal && !isNaN(dateLocal.getTime())){
        const pad = (n)=>String(n).padStart(2,"0");
        dateStr = `${dateLocal.getFullYear()}-${pad(dateLocal.getMonth()+1)}-${pad(dateLocal.getDate())} ${pad(dateLocal.getHours())}:${pad(dateLocal.getMinutes())}:${pad(dateLocal.getSeconds())}`;
      }

      return {
        text: (elText.value || "").trim(),
        useful: Math.max(0, Math.floor(useful)),
        funny: Math.max(0, Math.floor(funny)),
        cool: Math.max(0, Math.floor(cool)),
        date: dateStr
      };
    }

    function clampStars(s){ return Math.max(1, Math.min(5, Math.round(s))); }

    // ---- Events
    elPredictBtn.addEventListener("click", async () => {
      const payload = getPayload();
      if(!payload.text){
        setStatus("bad", "Review text masih kosong.");
        return;
      }

      setStatus("work", "Memproses prediksi...");
      elPredictBtn.disabled = true;

      try{
        let out;
        if(API_URL){
          out = await apiPredict(payload);
          elModelBox.textContent = `model: ${out.model || "api_model"}`;
          elExplainBox.textContent = out.details || "details: (no details from API)";
        } else {
          out = heuristicPredict(payload);
          elModelBox.textContent = `model: ${out.model}`;
          elExplainBox.textContent = out.details;
        }

        const stars = clampStars(out.stars);
        renderStars(stars);
        renderBars(out.probs || [0,0,0,0,1]);

        setStatus("ok", API_URL ? "Prediksi dari API berhasil." : "Prediksi heuristic selesai.");
      } catch(err){
        console.error(err);
        setStatus("bad", `Gagal: ${err.message}`);
        elExplainBox.textContent = "details: error";
      } finally {
        elPredictBtn.disabled = false;
      }
    });

    elFillExampleBtn.addEventListener("click", () => {
      elText.value = "Had a party of 6 here for hibachi. The waitress was very friendly and the food was delicious. Great experience — would recommend!";
      elUseful.value = 2;
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
      elModelBox.textContent = "model: -";
      elExplainBox.textContent = "details: -";
      setStatus("ok", "Form di-reset.");
    });

    // default render
    renderStars(0);
    renderBars([0,0,0,0,0]);
    elModelBox.textContent = API_URL ? "model: api_model" : "model: heuristic_rulebase_v1";
    elExplainBox.textContent = "details: -";
  </script>
</body>
</html>
"""

# height agak besar supaya layout mu terlihat penuh
components.html(HTML, height=950, scrolling=True)
