# 🏦 BLACK THURSDAY | יום חמישי השחור
### An interactive political-economy documentary about Israel's 1983 bank-share crisis

**University of Haifa · Political Science · AI Vibe Coding — Assignment 01**  
**Project team:** Yonatan & Liron · **Group identifier:** `polsci01`  
**Status:** Functional **prototype**, undergoing historical review, collaborative visual refinement, and complete end-to-end QA.  
**Repository:** https://github.com/yonti32-ux/polsci01-assignment-01-Project-Black-Thursday

![Actual opening slide from the prototype](Project-Black-Thursday-deliverable/media/screenshots/opening.png)

> **What is this?** A Hebrew/right-to-left 14-slide HTML presentation combining a source-backed political-science explanation of the **October 1983 Israeli bank-share crisis**, a genuine 3D animated documentary video, and an interactive model that runs in **Python**. We distinguish historical evidence, our analysis, visually schematic illustrations, and hypothetical simulation outputs.

## 🎯 Research question

**כיצד תרמו התמריצים והפעולות של הבנקים, המשקיעים, רשויות הפיקוח והמנהיגים הפוליטיים למשבר מניות הבנקים של 1983, ומה מלמדת התערבות המדינה על אחריות ציבורית וחלוקת סיכונים?**

We analyze conflicts of interest, institutional incentives, regulatory oversight, systemic risk, state intervention and distribution of financial costs. We do **not** attribute years of banking practice to a single minister.

## 🚦 Current development status (snapshot reviewed on 2 Nov 2026)

| Deliverable | Current snapshot | Next verification |
|---|---|---|
| PRD and historical storyboard | ✅ Present: `PRD 0.1.md` and `black-thursday-phase3/` | Consolidate version/links and update with new primary sources |
| HTML interactive deck | ✅ 14 slides in `Project-Black-Thursday-deliverable/presentation/` | Live student-computer browser QA |
| Genuine 3D film | ✅ 72s H.264 / 1280×720 MP4 included | Full normal-browser playback, captions and UX QA |
| Python simulation | ✅ Working local HTTP API, 8/8 unit tests in snapshot | Browser → Python → browser scenario and comparison test |
| Historical research citations | 🟡 Source registry exists | Add 1984 Comptroller and reconcile two source-ID systems |
| Screenshots and README | 🟡 Real screenshots exist; this root README is an update proposal | Confirm links render after merge and recapture changed pages |
| Team red-team review and submission | ⏳ In progress / not verified | Independent review, permissions, individual PDFs |

**Integrity note:** This README is a proposed update based on the uploaded ZIP, **not** a statement that Liron's newer in-progress edits have been reviewed or merged. The source videos and figures are not historical market recordings.

## 🖼️ Screenshots from the implemented prototype

| Schematic share support | 3D video frame | Python policy laboratory |
|---|---|---|
| ![Slide 4 - share support](Project-Black-Thursday-deliverable/media/screenshots/slide-04.png) | ![Real 3D film frame](Project-Black-Thursday-deliverable/media/screenshots/player-real-frame.png) | ![Actual Python-simulation slide](Project-Black-Thursday-deliverable/media/screenshots/python-simulation.png) |

## 💻 Run locally

Requires Python **3.11+**, an up-to-date desktop browser, and the project repository.

From the **repository root**:

```powershell
cd Project-Black-Thursday-deliverable
python python/app.py
```

Open **http://127.0.0.1:8000/** in a browser. Leave the terminal open. The app uses Flask when available or a zero-dependency Python standard-library fallback. No external API keys are required to view the presentation.

If `python` is not recognized on macOS/Linux, use `python3`. The source video can be watched without rebuilding its frames. Optional renderer/re-export dependencies are in `animation/requirements-render.txt`.

### Run automated tests

From `Project-Black-Thursday-deliverable/`:

```bash
python -m unittest discover -s python/tests -v
```

**Last independent snapshot check:** all **8 tests passed**; real `GET /api/health`, `POST /api/simulate` and asset requests returned successful responses. A complete real-browser-to-local-server test was **not possible in the review sandbox**, so it remains a student acceptance task. See [testing report](Project-Black-Thursday-deliverable/docs/testing-report.md).

### Controls

- **←** next slide; **→** previous slide; **Home** first; **End** last; **Esc** closes opened information dialogs.
- **תוכן עניינים**: jump to any slide. **הערות מרצה**: instructor notes and references.
- Slide 3: inspect institutional actors; slide 4: toggle schematic price support; slides 5–7: explore mechanisms, pressure and timeline.
- Slide 9: play/replay the original 3D educational video.
- Slide 13: adjust confidence, selling pressure, support capacity, and government intervention; run the real Python model, compare scenarios or reset.

## 🏗️ Technology and architecture

| Layer | Implementation | Current status |
|---|---|---|
| Presentation | HTML5, CSS, vanilla JavaScript, accessible interactive SVG | Implemented |
| 3D | Inspectable **raw WebGL** scene and CPU/software-rendered MP4 using Python | Implemented; **not** Three.js at present |
| Python | `python/simulation.py`, `python/app.py` (Flask / stdlib) | Implemented |
| Simulation exchange | `POST /api/simulate` returns 12 hypothetical periods as JSON | Tested at API level |
| Research and QA | `research/`, `docs/`, `prompts/`, unit tests, version history | Implemented, ongoing consolidation |

> The requirement is an **HTML presentation with a 3D video and functioning Python**. The original PRD suggested Three.js; the working prototype uses **actual 3D geometry and a software-rendered video**. This implementation decision is documented rather than hidden.

The **Python simulation is hypothetical**, deterministic and uses finite illustrative support budgets. It is **not** a simulation calibrated to 1983 exchange prices or a verified prediction of counterfactual policy outcomes. See [model methodology](Project-Black-Thursday-deliverable/docs/model-methodology.md).

## 📚 Historical evidence and accuracy

A selected evidence base:

1. **State Comptroller (December 1984):** *דו"ח על מניות הבנקים — משבר אוקטובר 1983* — first, detailed contemporaneous audit of manipulation and oversight. [Official catalog](https://library.mevaker.gov.il/sites/DigitalLibrary/Pages/Publications/1418.aspx). The actual report is dated **1984**, regardless of confusing PDF filename.
2. **State Comptroller (4 January 1993):** [*ההיערכות למכירת מניות הבנקים שבהסדר*](https://library.mevaker.gov.il/sites/DigitalLibrary/Pages/Publications/641.aspx) — government expenditures and share-sale accounting. **~US$9.1bn by Oct 1991 incl. financing ≠ net state loss.**
3. **Moshe Lador, Ministry of Justice:** [*שורשים במשפט: פרשת ויסות מניות הבנקים*](https://www.gov.il/he/pages/roots_1983) — legal retrospective; distinguish narrative from court holdings.
4. **Natalie Leonard, Yale Program on Financial Stability (2021):** [*Israeli Bank Shares Arrangement*](https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss3/13/) — scholarly chronology and rescue mechanics.
5. **Blass and Grossman (1996):** [Bank of Israel discussion paper](https://www.boi.org.il/media/rn3favup/dp9603e.pdf) — scholarly economic discussion.

**Current editorial checks:** reconcile source-ID collisions between phase-3 and deliverable research; clarify 14-vs-18-day closure counting; add the **1981 `מסמך הארבעה`** warning; optionally feature the State Comptroller's verified **Jan–Sep 1983** real-return comparison (nonbank stocks **−57.5%** versus all commercial-bank shares **+8.6%**) with exact category labels; preserve the distinction between a projected **1984 ~US$6.9bn obligation** and later **1993 ~US$9.1bn expenditure**.

## 🗂️ Repository navigation

- [Original product requirements draft](PRD%200.1.md) — initial project specification; pending canonical `PRD.md` adoption by team.
- [Phase 3 narrative and sources](black-thursday-phase3/README.md) — historical timeline, original storyboard, primary questions.
- [Working presentation and application](Project-Black-Thursday-deliverable/README.md) — actual code, environment and controls.
- [Current simulation source](Project-Black-Thursday-deliverable/python/simulation.py) and [tests](Project-Black-Thursday-deliverable/python/tests/test_simulation.py).
- [Video export notes](Project-Black-Thursday-deliverable/animation/EXPORT.md).
- [Claims and bibliography](Project-Black-Thursday-deliverable/research/sources.md) — currently use delivery-specific source IDs.
- [QA report](Project-Black-Thursday-deliverable/docs/testing-report.md), [development log](Project-Black-Thursday-deliverable/docs/development-log.md), [model methodology](Project-Black-Thursday-deliverable/docs/model-methodology.md).
- [Actual AI master instruction](Project-Black-Thursday-deliverable/prompts/2026-11-01-master-implementation-prompt.md).

*The `presentation - phase 5/` PDF is an earlier static draft, not the runnable HTML application.*

## 🤝 Collaborative engineering workflow

The team records **genuine** prompts, commits, test results, reviewer criticism and fixes. Changes should be made on branches and reviewed before merge, especially while Liron works on visuals and Yonatan reviews historical content. The root README must be updated at each meaningful milestone with working commands, a status change, sources and real captures. Avoid meaningless commit spam, synthetic test evidence and undocumented rewriting of history.

## ✅ Assignment and release checks

- [x] Valid team code of exactly 8 characters: `polsci01`.
- [x] HTML deck, genuine 3D video file, and Python-backed local simulation exist in uploaded snapshot.
- [x] Actual prompt history and Git commits appear in snapshot (five commits at review time).
- [ ] Team reviews/merges Liron's latest branch and new historical research.
- [ ] All final historical claims have pinpoint source references; no fake market data.
- [ ] Normal-browser-to-Python integration, film playback and accessibility verified.
- [ ] Root README screenshots render and reflect **final** code.
- [ ] Repository is public or lecturer has accepted access via `rmisegal@gmail.com`.
- [ ] Both students use the **official** Word report form unchanged, export PDF with group code and correct `exyy`, and **submit separately** via Moodle.
- [ ] Recommended self-grade is justified by the final work and QA results.

**Suggested group filename for exercise 01 (confirm Moodle numbering):** `polsci01-ex01.pdf`.

---
**README proposed update:** 2 Nov 2026 — prepared from the ZIP snapshot. This draft must be reconciled with the live repository and partner's latest changes **before** replacing root `README.md`.
