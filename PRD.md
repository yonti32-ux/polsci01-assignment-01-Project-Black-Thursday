# PRD v1.3 — Black Thursday | יום חמישי השחור

**Document status:** Release-candidate implementation specification, reflecting the team's approved v3 film. **Not a certification of final university submission.**  
**Date:** 2 November 2026 · **Team:** Yonatan and Liron · **Group:** `polsci01` · **Course:** Political Science / AI Vibe Coding, University of Haifa.  
**Historical baseline:** 1983 crisis, 1984 State Comptroller inquiry, 1993 financial-exposure audit, Yale, Bank of Israel, Ministry of Justice.  
**Original PRD:** [`docs/history/PRD-original-v0.1.md`](docs/history/PRD-original-v0.1.md). Changes below document the current implementation rather than pretending the original plan was followed without revisions.

## 1. Product definition

A serious but visually compelling, fully Hebrew RTL, interactive **HTML documentary** (14 slides), containing a **real code-rendered 3D animated video** (82s, slide 9) and a **functioning Python-powered educational stress simulation** (slide 13). The application runs locally on Windows via one double-click launcher; optionally slides/video can be viewed directly from `file://`, but Python simulation requires the launcher.

### Research question

**כיצד תרמו התמריצים והפעולות של הבנקים, המשקיעים, רשויות הפיקוח והמנהיגים הפוליטיים למשבר מניות הבנקים של 1983, ומה מלמדת התערבות המדינה על אחריות ציבורית וחלוקת סיכונים?**

The purpose is **political-science explanation**: agency, institutional incentives, regulatory failure, systemic risk, public-private responsibility, and policy tradeoffs, not merely an economics chronology.

## 2. Mandatory assignment compliance and evidence

| Requirement | Current implementation | Completion evidence | Final gate |
|---|---|---|---|
| HTML presentation | 14 Hebrew RTL slides | `Project-Black-Thursday-deliverable/presentation/` | Run on student's browser and verify navigation, RTL |
| 3D video inside presentation | 82s v3 H.264 MP4 with code-rendered 3D objects and infographic graphics | `media/video/crisis-animation-v3.mp4`, 3D sources under `animation/`; slide 9 references video | Play full film in Chrome/Edge with readable captions |
| Python runs and affects presentation | Deterministic 12-period model via Python HTTP API | `python/app.py`, `python/simulation.py`, JavaScript `POST /api/simulate`, tests | Launch on student laptop; change inputs and verify graph changes |
| PRD | This v1.3 specification with preserved original | Root `PRD.md` + archived initial PRD | Students approve requirements |
| README, screenshots | Honest README with actual screenshots and launch steps | Root `README.md`, `media/screenshots/` | Check Markdown images render in GitHub |
| Prompt-development history | Original student prompts and Liron's actual feedback | Root `prompts/` + Git commits | Keep prompts honest, no fabricated exchanges |
| Version control | Existing `.git` history in student clone | 7 commits visible in uploaded snapshot; all new changes need a fresh commit | Preserve and push original history; no reinitialization |
| Independent critique | Gemini review planned | `prompts/06-gemini-independent-review-prompt.md`; `docs/reviews/` | Record actual returned review, address findings |
| Submission | 8-character team code + official individual PDF submission | `polsci01`, official Word template converted to PDF | GitHub accessible; both upload `polsci01-ex01.pdf` **if exercise number is 01** |

**Scope principle:** The instructor emphasized a working deliverable, effective AI prompting, GitHub iteration, and critical judgment. The number of slides, length of video, detailed color system, simulation formulas and launcher are **team design decisions**, not mandated technologies.

## 3. Academic accuracy and evidence methodology

- Use the **December 1984 State Comptroller report**, *דו״ח על מניות הבנקים — משבר אוקטובר 1983*, as a primary source for the manipulation mechanism, early warnings, returns and initial government arrangement.
- Use the **1993 State Comptroller report** separately for financial-exposure accounting and state-held shares. Avoid interchanging different fiscal definitions and estimates.
- Supplement with Yale's 2021 case study, Bank of Israel research, Ministry of Justice's *שורשים במשפט* analysis, and period newspaper reporting.
- The documentary's **+8.6% / −57.5%** comparison covers *real returns, January–September 1983*, respectively **all commercial-bank shares** and **nonbank shares**. Source: State Comptroller 1984, Table 1.3, printed p. 19. **This is not an October 6 single-day index movement**.
- The bank share-support **inventory** worth approximately **US$1.06 billion on 6 October 1983** is not a bailout payment. The 1984 report's forward-looking commitment estimate and the 1993 report's cumulative outlay are **different measures**. Gross public outlay is not automatically net loss after accounting for state-owned bank equity.
- The exchange **suspended trading on 6 October 1983**. Where reopening-day reporting/definitions conflict (24 vs. 25 October; 14 trading versus 18 elapsed days), avoid an exact unsourced wording rather than choosing a side by intuition.
- Long-running price manipulation cannot be attributed to **Yoram Aridor alone**. His title was **Minister of Finance**; the contemporaneous reporting on his 13 October resignation concerned a separate dollarization proposal controversy.
- **October 1983 bank-share arrangement ≠ July 1985 economic stabilization program**.
- Distinguish: **historical fact**, **attributed source interpretation**, **team political-science analysis**, **schematic 3D visualization** and **hypothetical numerical simulation**. Never present invented prices, archival images, official decisions or counterfactual results as factual.

**Canonical live source IDs:** [`Project-Black-Thursday-deliverable/research/sources.md`](Project-Black-Thursday-deliverable/research/sources.md) and [`claim-register.csv`](Project-Black-Thursday-deliverable/research/claim-register.csv). Original Phase 3 IDs differed and are preserved only as historical planning evidence in `docs/history`; crosswalk at [`docs/history/SOURCE_ID_CROSSWALK.md`](docs/history/SOURCE_ID_CROSSWALK.md).

## 4. Audience and editorial design

**Audience:** University instructor and political science students. **Presentation format:** ~7–10 minutes of guided explanation plus video and optional simulator exploration. **Language:** readable modern Hebrew, correct `lang="he" dir="rtl"`, robust numeric and Latin-language bidirectional handling.

**Creative direction:** restrained financial-documentary design (navy, beige, gold, blue positive, red negative); original diagrams; readable distance and projection; no invented photos/quotes. Text must remain centered and within clear designated cards. Useful animation should communicate a mechanism; no pointless flashing, clutter or confusing transitions. Explain unfamiliar terms in context.

**Liron's approved video palette (exact hex):** `#1c242c`, `#c19d43`, `#d3cebe`, `#1f3c58`, `#8ab9ee`, `#7a8694`, `#e7eef4`, `#f5cb39`, `#ed1c16`.

**Accuracy labeling:** `המחשה סכמטית — אינה שחזור של נתוני מסחר`; `סימולציה לימודית — לא נתוני 1983`. Voiceover not mandatory: the video must be understandable from displayed captions.

## 5. Slide storyboard — implemented fourteen-slide deck

| Slide | Theme / function | Political-science role |
|---|---|---|
| 01 | יום חמישי השחור | Research hook and institutional responsibility question |
| 02 | ישראל בתחילת שנות ה־80 | Macro context, distinct from underlying manipulation |
| 03 | מי השחקנים? | Banks, investors, government and differentiated regulators |
| 04 | מהו ויסות מניות? | Supporting demand versus genuine market demand; synthetic diagram |
| 05 | המנגנון מאחורי הקלעים | Networks, funding mechanisms, potential conflicts of interest |
| 06 | המחיר של יציבות מלאכותית | Finite capacity to absorb selling; illustrative units |
| 07 | 1983: סימני האזהרה | Selling pressure, institutional warning and incentives |
| 08 | 6 באוקטובר 1983 | Trading suspension and emergency policy context |
| 09 | סרט תלת־ממד | 82s abstract documentary showing seven stages |
| 10 | הסדר המדינה | Future redemption commitment, ownership ≠ management |
| 11 | עלויות וחלוקת נטל | Expenditures, assets, state risk; rigorous accounting footnotes |
| 12 | ועדת בייסקי ואחריות | Commission/institutional accountability, not a single verdict |
| 13 | מעבדת מדיניות | Python-generated conditional scenarios with disclaimer |
| 14 | מסקנות ומקורות | Students' political-science conclusions and cited evidence |

Existing working slide text lives in `presentation/slides-data.js`, not in this document. The archived original storyboard is in `docs/history/` and should not overwrite the implemented deck.

## 6. Final video specification (v3 approved creative baseline)

- **Artifact:** `media/video/crisis-animation-v3.mp4`; **82 seconds**, **1280 × 720**, **20 fps**, **H.264**, intentionally silent and readable without sound.
- **Source:** original coded 3D geometry/source with raw WebGL and Python renderer, then organized abstract motion-infographic overlays. **Do not claim Three.js renders this film**; Three.js was a planned option but was not the implemented choice.
- **Narrative structure:** seven stages (support practice → mechanisms → statistically verified 1983 contrast → rising sell pressure → 6 Oct trading halt → government arrangement → political accountability).
- **Mathematics:** normalized diverging return chart showing actual period values with correctly proportional bars and explicitly labeled January–September 1983. Any other visual bar/line/stress meter is conceptual and must say so.
- **Visual quality:** centered copy inside designated panels; stable baseline and margins; high contrast; no ghost text, clipped labels, non-Hebrew glyph errors, overlapping text or misleading stock indices; slow smooth movement and meaningful transitions.
- **Deliverable:** embedded on slide 9 with working browser controls and original `animation/` production code, `EXPORT_v3.md`, readable film transcript, and genuine screenshots.
- **Archive:** older real v1/v2 video assets may remain as development evidence; **v3 is the only active film referenced by slide 9**.

## 7. Python simulation (implemented)

**Server:** `Project-Black-Thursday-deliverable/python/app.py`, local `127.0.0.1:8000`; Flask or standard-library WSGI alternative.

| Endpoint | Purpose |
|---|---|
| `GET /` | Serve HTML presentation |
| `GET /api/health` | Report process and model version |
| `POST /api/simulate` | Validate controls and run Python simulation; JSON result |

**Inputs:** `confidence`, `sell_pressure`, `bank_capacity` — whole numbers 0–100 — and `intervention ∈ {none, delayed, early}`. **Outputs:** 12 time steps, simulated unitless stability index, illustrative selling demand, finite bank/public support budgets, unmet demand, and conditional model-language summary. Model deterministic with identical inputs; `historical:false` in response.

**Design rule:** The toy model is **not calibrated to 1983 data**, not a prediction, not causal identification; its formulae and coefficients are documented in [`docs/model-methodology.md`](docs/model-methodology.md). In direct `file://` mode, slides/video may load, but simulation must show a genuine offline notice. No static response passed off as Python execution.

## 8. Delivery architecture and access

Root launcher (`START_BLACK_THURSDAY.bat` / `.sh`) calls `launch_presentation.py`, which runs the actual server in the sibling `Project-Black-Thursday-deliverable/python/app.py`. On Windows it opens the default browser to `http://127.0.0.1:8000/`. No paid services, credentials or remote requests are needed for core functionality. Python 3.11+ is expected, but package installation is not needed for the standard-library fallback.

Browser files live in the `Project-Black-Thursday-deliverable/` directory. This project deliberately uses **one active runnable copy**. Older duplicates from the uploaded ZIP are excluded from the clean candidate to prevent the reviewer from opening the wrong version.

## 9. QA acceptance gates

1. Complete Windows BAT run from a fresh checkout with all 14 slides accessible; correct navigation and Hebrew layout.
2. Slide 9 plays v3 entire 82s; video controls and centered captions visible, numbers/units legible.
3. Slide 13 calls the real Python backend, chart and summary update, altered inputs produce altered results, reset/compare work.
4. No console JavaScript errors in a real browser during the guided workflow.
5. API tests pass, invalid inputs return HTTP 400, and `GET /api/health` works.
6. Every historical claim, cost figure, original image, and relevant citation is reviewable; no unsupported historical index chart.
7. Lecturer can access the exact GitHub repository provided in the official submission PDF.
8. A separate AI (Gemini) performs a skeptical independent assessment, which is **documented, not fabricated**; critical defects fixed before declaring final.
9. `README.md` paths, images and commands match committed content. Genuine prompts and Git history are preserved.
10. Individual official Moodle reporting forms submitted as PDFs, with exact `polsci01-exyy.pdf` filename and personally completed identification fields; no private IDs committed to GitHub.

**Already tested in review sandbox (2 Nov 2026):** 8/8 Python unit tests passed; local HTTP 200 for home/health/v3 video/JavaScript; FFprobe validated video encoding. **Not yet certified:** live-browser interaction (blocked by evaluation environment), physical Windows BAT launch, lecturer GitHub access, Gemini review, or students' final historical/editorial sign-off.

## 10. Git / prompt engineering / red team

- Store **actual** prompts in chronological `prompts/`, with first experimental request and Liron's video refinement instructions preserved unaltered as evidence. Preserve changes and defects in substantive commits, not artificial check-in spam.
- Original planning docs and older QA reports are clearly marked and archived in `docs/history/`. Do not duplicate entire old runnable builds at repository root; Git history provides prior versions.
- Gemini's review belongs in `docs/reviews/` and should include model/date/version, unedited feedback, rubric or scores, and disposition of issues. The team independently chooses the **recommended self-grade**, with rationale in `docs/SELF_ASSESSMENT.md` and in the **designated field in the university's official form**. No Gemini output should be represented as an instructor grade.

## 11. Release status and change log

| Date | Version | Change |
|---|---|---|
| Early development | v0.1 | Original PRD and initial concept (archived unchanged) |
| 1–2 Nov 2026 | v0.4 | Consolidated historical research, initial documented video refinement, one-click launcher |
| 2 Nov 2026 | v0.5 | Liron's v3 video, primary-source return figures, re-rendered caption panels and QA loop |
| 2 Nov 2026 | **v1.3 PRD** | Administrative/documentation consolidation around v0.5 **release candidate**; application source preserved |

**Approval rule:** This PRD reflects the **approved creative direction** and actual assembled candidate; it does **not** claim the university exercise has already passed independent testing or final submission. See [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md).
