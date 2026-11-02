# 🏦 BLACK THURSDAY | יום חמישי השחור
### An interactive political-economy documentary about Israel's 1983 bank-share crisis

**University of Haifa · Political Science · AI Vibe Coding — Assignment 01**  
**Project team:** Yonatan & Liron · **Group identifier:** `polsci01`  
**Status:** Functional **prototype** with 82-second **v3 documentary**, undergoing historical review, collaborative visual refinement, and complete end-to-end QA.  
**Repository:** https://github.com/yonti32-ux/polsci01-assignment-01-Project-Black-Thursday

![Actual opening slide from the prototype](Project-Black-Thursday-deliverable/media/screenshots/opening.png)

> **What is this?** A Hebrew/right-to-left 14-slide HTML presentation combining a source-backed political-science explanation of the **October 1983 Israeli bank-share crisis**, a genuine 3D animated documentary video, and an interactive model that runs in **Python**. We distinguish historical evidence, our analysis, visually schematic illustrations, and hypothetical simulation outputs.

### 🎬 Video preview from the v3 candidate

![Real frame from v3 H.264 film: Jan–Sep 1983 returns](Project-Black-Thursday-deliverable/media/screenshots/film-v3-verified-returns.png)

**Technical provenance:** the 82-second film contains newly centered and choreographed data/analysis panels over **cleanly re-rendered original 3D mesh footage**. It does not use Three.js to render the movie. The +8.6% and −57.5% values are *period returns*, not a daily bank index; all other imagery is schematic. See [v3 export and evidence](Project-Black-Thursday-deliverable/animation/EXPORT_v3.md), [Liron's actual feedback prompt](prompts/2026-11-02-liron-video-refinement-v3.md) and [v0.5 QA](docs/ITERATION_v0.5_VIDEO_QA.md).

## 🎯 Research question

**כיצד תרמו התמריצים והפעולות של הבנקים, המשקיעים, רשויות הפיקוח והמנהיגים הפוליטיים למשבר מניות הבנקים של 1983, ומה מלמדת התערבות המדינה על אחריות ציבורית וחלוקת סיכונים?**

We analyze conflicts of interest, institutional incentives, regulatory oversight, systemic risk, state intervention and distribution of financial costs. We do **not** attribute years of banking practice to a single minister.

## 🚦 Current development status (v0.5 candidate; 2 Nov 2026)

| Deliverable | Candidate snapshot | Next verification |
|---|---|---|
| PRD and historical storyboard | ✅ Canonical `PRD.md` v1.2 and preserved original `PRD 0.1.md`, and `black-thursday-phase3/` | Team reviews PRD addendum and official-source citations |
| HTML interactive deck | ✅ 14 slides in `Project-Black-Thursday-deliverable/presentation/` | Live student-computer browser QA |
| Genuine 3D film | ✅ 82s H.264 / 1280×720 v3 MP4 included | Full normal-browser playback and pacing QA; Liron approval of v3 |
| Python simulation | ✅ Working local HTTP API, 8/8 Python tests passed in this candidate | Browser → Python → browser scenario and comparison test |
| Historical research citations | 🟡 1984 Comptroller S10 added; registry exists | Finish validation and migrate archived source IDs systematically |
| Screenshots and README | 🟡 Real screenshots exist; this root README is an update proposal | Confirm links render after merge and recapture changed pages |
| Team red-team review and submission | ⏳ In progress / not verified | Independent review, permissions, individual PDFs |

**Integrity note:** This README is a proposed update based on the uploaded ZIP, **not** a statement that Liron's newer in-progress edits have been reviewed or merged. The source videos and figures are not historical market recordings.

## 🖼️ Screenshots from the implemented prototype

| Schematic share support | 3D video frame | Python policy laboratory |
|---|---|---|
| ![Slide 4 - share support](Project-Black-Thursday-deliverable/media/screenshots/slide-04.png) | ![Actual v3 MP4 frame showing proportionate returns](Project-Black-Thursday-deliverable/media/screenshots/film-v3-verified-returns.png) | ![Actual Python-simulation slide](Project-Black-Thursday-deliverable/media/screenshots/python-simulation.png) |

## ▶ One-click launch (recommended)

> **Packaging note (v0.4 complete test archive):** The `Black_Thursday_v04_Selective_Update.zip` distributed earlier was only an overlay and did **not** contain `Project-Black-Thursday-deliverable/python/app.py`. Running its BAT file directly produces a missing-server error. To test this version without merging anything, use `Black_Thursday_v04_COMPLETE_Ready_to_Run.zip`, extract it **fully**, and run the BAT file from the extracted folder. See `HOW_TO_RUN_FIRST.txt`. This complete archive is a snapshot and deliberately omits `.git`; integrate changes into your existing Git clone on a branch, not by replacing its `.git` folder.



**Windows:** From the **GitHub repository root**, double-click `START_BLACK_THURSDAY.bat`. It starts the project's actual Python service (Flask if installed, otherwise built-in Python stdlib fallback) and opens the browser automatically. Python 3.11+ must already be installed; video playback requires no special library. Close the terminal or press Ctrl+C to stop.

**Mac/Linux:** Run `sh START_BLACK_THURSDAY.sh` or `python3 launch_presentation.py` from the repo root.

**Static local-file viewing:** Double-click `Project-Black-Thursday-deliverable/presentation/index.html`. The slides and locally stored MP4 may be viewed without starting Python. **Slide 13 cannot calculate Python scenarios in `file://` mode**; use the launcher for the full mandatory functionality. This limitation is documented on slide 13. Test local-file playback in your browser before presenting.

## 💻 Run locally (manual alternative)

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

**Prior prototype check (2 Nov 2026):** all **8 tests passed**, and the Python launcher served the v3 MP4 and simulation API successfully; real `GET /api/health`, `POST /api/simulate` and asset requests returned successful responses. A complete real-browser-to-local-server test was **not possible in the review sandbox**, so it remains a student acceptance task. See [candidate QA report](docs/TEST_RESULTS_v0.4.md) and [original implementation report](Project-Black-Thursday-deliverable/docs/testing-report.md).

### Controls

- **←** next slide; **→** previous slide; **Home** first; **End** last; **Esc** closes opened information dialogs.
- **תוכן עניינים**: jump to any slide. **הערות מרצה**: instructor notes and references.
- Slide 3: inspect institutional actors; slide 4: toggle schematic price support; slides 5–7: explore mechanisms, pressure and timeline.
- Slide 9: play/replay the v3 3D-backed educational video.
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

## 🎞️ Film v3 — Liron's second-round improvements

The existing **real 3D footage** was re-rendered as an **82-second, seven-stage, business-focused documentary** using a consistent two-column system. The previous caption layer was removed; all Hebrew text is centered inside intentional cards. Abstract 3D motion remains visible behind code-generated explanations. Positive numbers appear in blue and negative figures in red, using only Liron's palette. It now distinguishes the **bank-share category** and **nonbank stocks traded on the Tel Aviv exchange**, explicitly identifies the trading halt of **6 October 1983**, and illustrates the **future government redemption commitment** rather than implying an immediate payout.

A real historical comparison appears in the film: for **January–September 1983**, the **real return on all commercial-bank shares was +8.6%**, while **nonbank shares returned −57.5%**. These are period returns from the **1984 State Comptroller, Table 1.3 (printed p.19)**—**not** a daily banking index, nor an October crash percentage. See [film v3 export and provenance](Project-Black-Thursday-deliverable/animation/EXPORT_v3.md) and [v3 self-audit and remaining checks](docs/ITERATION_v0.5_VIDEO_QA.md). The original source film is retained for rollback.

![Real v3 frame documenting proportional January–September 1983 returns](Project-Black-Thursday-deliverable/media/screenshots/film-v3-verified-returns.png)

## 📚 Historical evidence and accuracy

A selected evidence base:

1. **State Comptroller (December 1984):** *דו"ח על מניות הבנקים — משבר אוקטובר 1983* — first, detailed contemporaneous audit of manipulation and oversight. [Official catalog](https://library.mevaker.gov.il/sites/DigitalLibrary/Pages/Publications/1418.aspx). The actual report is dated **1984**, regardless of confusing PDF filename.
2. **State Comptroller (4 January 1993):** [*ההיערכות למכירת מניות הבנקים שבהסדר*](https://library.mevaker.gov.il/sites/DigitalLibrary/Pages/Publications/641.aspx) — government expenditures and share-sale accounting. **~US$9.1bn by Oct 1991 incl. financing ≠ net state loss.**
3. **Moshe Lador, Ministry of Justice:** [*שורשים במשפט: פרשת ויסות מניות הבנקים*](https://www.gov.il/he/pages/roots_1983) — legal retrospective; distinguish narrative from court holdings.
4. **Natalie Leonard, Yale Program on Financial Stability (2021):** [*Israeli Bank Shares Arrangement*](https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss3/13/) — scholarly chronology and rescue mechanics.
5. **Blass and Grossman (1996):** [Bank of Israel discussion paper](https://www.boi.org.il/media/rn3favup/dp9603e.pdf) — scholarly economic discussion.

**Current editorial checks:** reconcile source-ID collisions between phase-3 and deliverable research; clarify 14-vs-18-day closure counting; show the **1981 `מסמך הארבעה`** warning more explicitly; optionally feature the State Comptroller's verified **Jan–Sep 1983** real-return comparison (nonbank stocks **−57.5%** versus all commercial-bank shares **+8.6%**) with exact category labels; preserve the distinction between a projected **1984 ~US$6.9bn obligation** and later **1993 ~US$9.1bn expenditure**.

### Source-ID caution

Earlier Phase 3 research uses different `S01`–`Sxx` IDs from the working deck. The actual app bibliography is canonical; see [source-ID crosswalk](docs/SOURCE_ID_CROSSWALK.md). Newly assigned **S10** refers to the original 1984 audit.

## 🗂️ Repository navigation

- [Canonical PRD v1.2 with change record](PRD.md), plus [preserved original PRD](PRD%200.1.md).
- [Phase 3 narrative and sources](black-thursday-phase3/README.md) — historical timeline, original storyboard, primary questions.
- [Working presentation and application](Project-Black-Thursday-deliverable/README.md) — actual code, environment and controls.
- [Current simulation source](Project-Black-Thursday-deliverable/python/simulation.py) and [tests](Project-Black-Thursday-deliverable/python/tests/test_simulation.py).
- [Video v3 export notes](Project-Black-Thursday-deliverable/animation/EXPORT_v3.md).
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
**README update candidate:** 2 Nov 2026 — v0.4. Prepared from the uploaded ZIP, not pushed to GitHub. On-machine tests and partner approval remain outstanding. Update this file after each meaningful verified commit.
