# Project Black Thursday — Full repository audit and next-iteration roadmap

**Audit date:** 2 November 2026  
**Team:** Yonatan and Liron | **Official group code:** `polsci01` (exactly eight characters)  
**Repository:** https://github.com/yonti32-ux/polsci01-assignment-01-Project-Black-Thursday  
**Basis:** the uploaded `assignment 01.zip` working-copy snapshot, supplied 95-page **State Comptroller, *דו"ח על מניות הבנקים — משבר אוקטובר 1983* (December 1984)**, Ministry of Justice's *שורשים במשפט* retrospective (Moshe Lador), the earlier PRD/storyboard, and previously identified authoritative sources. This is **not** a live GitHub audit or a review of edits Liron makes after the ZIP export.

## Executive decision

**Continue from the working prototype; do not restart.** The assignment's core technical concept is already implemented. Prioritize (1) correcting project documentation and source attribution, (2) upgrading historical quality using the newly supplied primary source, (3) a complete student-machine end-to-end test, (4) targeted visual/UX polish and credible, documented team iteration, then (5) final release/submission. Keep the documentary+interactive-simulation direction C.

## 1. Actual repository snapshot

- Git snapshot contains **5 commits** ending at `a7c9caa` (`main`, `origin/main` in the exported checkout). This is evidence in the ZIP only, not confirmation of current live GitHub.
- The root document is **`PRD 0.1.md`**, **not `PRD.md`** as planned. Do not rename or overwrite before checking with Liron; add an explicit link or create a canonical `PRD.md` by team decision, preserving old version in history.
- The **root `README.md` is outdated**: it describes an unimplemented project, includes broken image paths at `media/screenshots/…`, and offers root launch commands that don't work without changing directories. A second, substantially more accurate `README.md` exists inside `Project-Black-Thursday-deliverable/`.
- The **working implementation is nested** under `Project-Black-Thursday-deliverable/`; Phase 3 research occupies `black-thursday-phase3/`, and the old `presentation - phase 5/` directory contains a separate static 14-page PDF draft and master prompt. The PDF draft is *not* the HTML deliverable and even displays a film placeholder.
- The snapshot includes **two claim registers and two bibliography systems** that reuse source IDs inconsistently. Example: **S01** means Yale in Phase 3, but the State Comptroller's **1993** report in the working deck. Do not merge these registries blindly: choose one canonical source registry and change dependent IDs together.
- The snapshot's working tree reports two modified files, but `git diff --ignore-space-at-eol --stat` is empty: the differences appear to be line-ending normalization only. Preserve them nevertheless until checked with Liron.
- Remove the tracked Word temporary lock file `black-thursday-phase3/content/~$lm-shotlist.md` in a separate documented maintenance commit.
- No verified official academic group number outside the team-provided `polsci01` is needed: `polsci01` is **8 characters** and suits `polsci01-ex01.pdf` **if Moodle confirms `ex01`**.

## 2. Technical review — what was directly checked

| Component | Observed status in ZIP | Evidence / limitation |
|---|---|---|
| Hebrew-RTL HTML presentation | **Implemented** | `presentation/index.html`, `slides-data.js` (14 content slides), `app.js`, `styles.css`; real captures provided. |
| Slides/navigation/interactions | **Implemented; live-browser retest needed** | Code includes hash navigation, previous/next, keyboard support, interactive diagram controls, actors, notes/source drawers. Screenshots are visually polished. |
| Historical 3D video | **Playable file exists** | `media/video/crisis-animation.mp4`: H.264, 1280×720, **72 seconds**, 20fps; real decoded frame screenshot included. |
| Three.js requirement/choice | **Not implemented as originally selected** | Source scene is **raw WebGL**, video is exported through **Python CPU rendering**. This can fulfill *genuine 3D video* but is not a Three.js-produced movie; disclose deviation, or reimplement if instructor specifies Three.js as mandatory. |
| Running Python model | **Working** | `python/app.py`, `simulation.py`, `GET /api/health`, `POST /api/simulate` checked with real local HTTP requests. |
| Python unit tests | **8 / 8 pass** | Independently reran `python -m unittest discover -s python/tests -v` from deliverable directory. |
| JS syntax | **Passed** | `node --check` passed on `presentation/app.js`, `slides-data.js`, and `animation/scene.js`. |
| Local assets | **HTTP 200** | Root `/`, `presentation/app.js`, MP4, and `animation/scene.js` served successfully over localhost. |
| Full browser-to-Python test | **Not independently verified here** | Browser in current environment blocks `http://127.0.0.1:8000` with `ERR_BLOCKED_BY_ADMINISTRATOR`; test on Yonatan's/Liron's Windows PC. |
| Docs/research | **Exists, needs consolidation** | Nested development log, QA report, methodology, sources, claim register and animation export instructions are present. |
| GitHub access/individual PDF | **Not verified** | Confirm current repository visibility and lecturer access, and each student's Moodle upload separately. |

**Reproducible technical commands (from Git repository root):**

```powershell
cd Project-Black-Thursday-deliverable
python -m unittest discover -s python/tests -v
python python/app.py
# Then browse to http://127.0.0.1:8000/
```

The app works using Flask if installed, otherwise falls back to a standard-library server. On a clean machine verify Python 3.11+ and browser playback. The video export's dependencies are additional and not required for viewing.

## 3. Major discoveries in NEW historical sources

### A. The 1984 State Comptroller report is our most valuable new primary source

The actual **cover reads December 1984** despite the uploaded filename containing `1993`. Cite it as **State Comptroller, *דו"ח על מניות הבנקים — משבר אוקטובר 1983* (December 1984)**. Its independent historical perspective is not the same as the Comptroller's **1993** follow-up report about sale of the arrangement shares.

**Source page pointers below refer to the *printed* page number; the uploaded PDF uses an offset (e.g., printed p. 7 is PDF page 5).**

1. **A years-long phenomenon, not Aridor's one-man mistake.** The 1984 Comptroller traces the practices to the early 1970s and identifies purchases, related entities, affiliated funds, client advice and other mechanisms (printed pp. **7–8, 22–24**). It makes an explicit distinction between normal, stabilizing market-making and *manipulative* support to alter the market trend (printed pp. **8, 22–23**).
2. **An ignored institutional warning is now traceable.** The **December 1981 'מסמך הארבעה'** documented danger to market and bank stability, but authorities did not put in place an effective solution (printed pp. **11–13, 21, 32**). This is an especially strong political-science point: *regulatory coordination failure and delayed action*. Add it to slide 7 or 12.
3. **The mechanism's scale can be illustrated with real, sourced figures.** On **6 October 1983**, the banks' aggregate share-support inventory was about **US$1.06 billion** at then-prevailing rates (printed **p. 7**; further discussion p. 10). This is a **stock of shares held in support operations**, *not* total market loss, a cash payout, or ultimate rescue cost.
4. **The 1984 report offered an ex-ante estimate of future obligations.** It projected about **US$6.9 billion** in dollar-equivalent future government commitments (printed **p. 7**). This is a **1984 prospective obligation estimate**, not the same metric as **1993's retrospective US$9.1bn cumulative gross expenditure through October 1991 including financing**. Never plot them as if the government 'lost' both amounts or one replaced the other.
5. **Use the first nine months of 1983 as a real sourced chart** (printed pp. **18–19**, Table 1.3 and explanatory text): **nonbank shares −57.5% real**, versus **all commercial-bank shares +8.6% real**. The bank-share aggregate includes banks beyond the manipulated subset, per the table's note; label the series accordingly. This is stronger and more accurate than a manufactured market trend. This data is a **return over Jan–Sep 1983**, not an indexed daily price path and not necessarily a weighted 'regulated-bank-only' return.
6. **An important distributional point** (printed **p. 11**): the report criticizes how the arrangement protected shareholders/controlling interests while transferring substantial burdens to the public, including people without comparable share portfolios. Attribute this to the **Comptroller's assessment**, rather than asserting it is an uncontested truth.
7. **Financial agreement date:** the 1984 report states the agreements were prepared/signed **by 20 October 1983** (printed **p. 11**). Useful if exact events are shown.
8. **Regulatory actors:** the Comptroller specifically assessed the roles of the **Israel Securities Authority, Ministry of Finance, and Bank of Israel**, not one unified 'regulator' (printed **pp. 11–13**). Its report explicitly notes limitations in directly reviewing the banks because those organizations fell outside the Comptroller's audit jurisdiction (printed **p. 7**).
9. **Caution on suspension duration:** printed p. **17** describes closure as **14 days**, whereas Yale describes an **18-day** closure. These may use different counting conventions (e.g., market/trading versus elapsed days), but **this interpretation is not independently established**. Keep '6 October closure' as firm, and investigate precise counting before labeling '18 days' unqualified on the screen.

### B. Ministry of Justice: historical legal interpretation, not a substitute for the verdicts

The government link `https://www.gov.il/he/pages/roots_1983` leads to the Ministry of Justice's legal-historical retrospective by **Moshe Lador**, *פרשת ויסות מניות הבנקים — כשתופעה מקרו כלכלית מוצאת עצמה על ספסל הנאשמים*. Its actual PDF is `https://www.gov.il/BlobFolder/reports/roots_1983/he/roots-1983.pdf`.

It describes the banks' long-running manipulation, how the crisis threatened financial stability, the risk of a hypothetical **run on bank deposits** (not proof a general run occurred), and the later criminal proceedings. The author writes from a **prosecutorial perspective** and references court judgments, indictments, and the commission. If we make a specific legal claim, inspect and cite the **judgment** itself where feasible; distinguish allegations, trial judgment, appeals and commission findings. The retrospective's approximate **$7bn** is not directly interchangeable with the **1993** accounting total.

### C. Historical accuracy changes to prioritize in presentation

| Priority | Slide(s) | Proposed correction / enhancement | Source anchor |
|---|---|---|---|
| **P0** | 07, 12 | Add the actual **1981 written warnings** and who received them; move from 'nobody noticed' to 'known risk and weak coordination' | 1984 audit pp. 11–13, 21, 32 |
| **P0** | 08, timeline/video | Reconcile **14 vs 18 days** before asserting an unqualified closure length; retain uncontroversial **6.10.1983** | 1984 audit p. 17; Yale case |
| **P0** | 11 | Keep **$9.1bn** as cumulative **expenditure through Oct 1991 incl. financing**, not the state's final net loss; separately label 1984 **$6.9bn** future-commitment estimate if shown | 1993 audit preface; 1984 audit p. 7 |
| **P0** | 03/12 | Attribute culpability/oversight assertions to source bodies and distinguish bank management from ISA, BOI and Treasury | 1984 audit pp. 7, 11–13; Lador |
| **P1** | 07 | Add an **actual, sourced two-column comparison**: −57.5% real for nonbank shares versus +8.6% real for all commercial-bank shares in Jan–Sep 1983. Label population, units, interval and table. | 1984 audit Table 1.3 pp. 18–19 |
| **P1** | 06 | Add a documentary evidence card: **~$1.06bn share-support inventory by Oct 6**, with careful definition. | 1984 audit pp. 7, 10 |
| **P1** | 10 | Differentiate **agreement signed by Oct 20**, future redemption obligations and later ownership, avoiding 'government paid all shares immediately'. | 1984 audit p. 11; Yale case |
| **P1** | 12 | Consider a decision-flow illustration: early warning → multiple agencies aware → insufficient action → later rescue. | 1984 audit pp. 11–13 |
| **P2** | 09 | If revising the film, show the 1981 warning and changing public liability, but only if this enhances understanding, not merely visual spectacle. | 1984 audit; Ministry of Justice retrospective |

**Other protections:** Inflation **445%** belongs to 1984; the 1985 stabilization plan is separate from October 1983; Yoram Aridor was Finance Minister and not the sole author of years of bank practices. Confirm any named bank or bank officer before adding portraits.

## 4. Agreed work plan — split into merge-safe stages

### Stage 1 — Stabilize and align the repository (P0, first)

1. Before coding, **Yonatan and Liron each run `git status`, `git pull --ff-only`** only when their working trees are clean. Protect in-progress changes first. Make separate feature branches if both edit the same files.
2. Agree on canonical source of truth for PRD (`PRD.md` vs current `PRD 0.1.md`) and canonical working deck path. Keep history intact; do **not** flatten or delete previous prototypes before reviewing relevant references.
3. **Update the root README** from planning-only to current-prototype status, with correct nested launch commands and **real image links** pointing into `Project-Black-Thursday-deliverable/media/screenshots/…`. Keep verified tests separate from pending live browser testing.
4. Select **one bibliography ID scheme** and revise phase 3/doc references together; link original 1984 report and Ministry of Justice PDF; retain old documents as archived history if appropriate.
5. Remove temporary Word lock file, confirm `.gitignore` works, and make a meaningful documentation-only commit. Avoid touching Liron's presentation files during this stage.

**Exit criterion:** Someone viewing the GitHub root can see the *actual* implemented project, launch it successfully by following the README, and open the correct screenshots/sources.

### Stage 2 — Primary-source-based historical upgrade (P0/P1)

1. Add the **1984 Comptroller** as a **distinct new source** from the 1993 audit in the `research/sources.md`/claim registry. Add the Ministry of Justice retrospective with explicit author and legal-source caveat.
2. Draft exact Hebrew slide edits for slides **6, 7, 10, 11, 12**, with a claim ID, printed page and explanatory note before changing code.
3. Add the genuine 1983 two-bar chart; distinguish banking-share subset issues. Add **1981 warning** as a high-value institutional-politics milestone.
4. Resolve ambiguity around closure duration, reopen date, and financial estimates. Anything unresolved should be conservatively phrased and logged.
5. Have **both team members read the changed slide text** for academic accuracy and legibility.

**Exit criterion:** Every added number/quotation has a pinpoint source citation. Simulations remain clearly hypothetical.

### Stage 3 — Collaborative visual and interaction refinement (P1)

1. **Liron's ongoing visual improvements should land on a separate branch/PR**; do not replace her code with an older ZIP.
2. Review specific slide 6, 7, 11, 12 layouts for readable data labels, source notes, date direction and interaction purpose; retain high-performing visual identity from current prototype.
3. Evaluate whether 3D film/scene should stay with documented raw-WebGL/CPU rendering or be rebuilt in Three.js. **Course minimum is a genuine 3D video**; don't undertake a time-consuming re-render merely to match a non-mandatory library preference without confirming rubric or payoff.
4. Test media controls, source chips, note drawers, all slides, the Python simulator (including comparison/reset), keyboard nav and projected readability on a real laptop/browser.

**Exit criterion:** Full guided demonstration passes on at least one student machine; screen recordings or screenshots document it.

### Stage 4 — Red team and documented QA (P0 release gate)

1. Independent adversarial review by another LLM with explicit tasks: historian, banking-policy scholar, legal source verifier, statistics/modeling reviewer, browser QA, accessibility and GitHub compliance reviewer.
2. Convert findings into an issue list: ID, severity, exact slide/file, evidence, decision, fix commit, status.
3. Execute local unit tests and browser-to-Python check again after the final merge; capture *current* screenshots from final code. Verify repository permissions to lecturer.
4. Check readability in Chrome and Edge (projected 1366×768 and 1920×1080); video codec, captions, complete 72-second playback, and Python network requests.
5. Update `docs/testing-report.md` and the **root README** with *real test results*, not claims from earlier versions.

**Exit criterion:** All mandatory HTML, embedded 3D video, running Python, GitHub trail, historical/source and final-form requirements pass; no P0 defects open.

### Stage 5 — Release/admin (P0)

- Keep **group code `polsci01`** in project metadata. Verify the exercise suffix on Moodle (`ex01` expected but confirm).
- Repository must be **public** or specifically accessible to lecturer `rmisegal@gmail.com`.
- Two students separately fill the **official Word template** without layout changes, export to PDF as `polsci01-ex01.pdf` if the suffix is correct, and each submit individually.
- Add justified self-grade only after actual QA. No personal IDs or sensitive submission forms in public GitHub.

## 5. Highest-return improvements for our political-science assignment

**First: 'They were warned'** — the **1981 four-person warning document** shows this was not simply a market accident; it was also an institutional response problem. The Comptroller's sharply critical assessment should be attributed and allow discussion about divided responsibility.

**Second: 'Real data, not decorative graphs'** — the **Jan–Sep 1983** comparison (nonbank shares −57.5% versus all commercial-bank shares +8.6% real) is an ideal transition into the distortion mechanism. Keep the Python experiment visibly separate.

**Third: 'Who was protected, who bore risk?'** — an evidence-based diagram on the future redemption arrangement with **1984 estimated commitments** versus **1993 recorded expenditure**, showing why accounting definitions and distribution matter.

**Fourth: 'Professional engineering, not more effects'** — a root README that matches reality, one canonical source ledger, real end-to-end test evidence, real Git progression and a prioritized critical-review log will probably return more value than an additional elaborate animation.

## 6. Proposed meaningful commits (only after real modifications)

```
docs: align root README with implemented prototype and polsci01 code
research: add 1984 Comptroller and Ministry of Justice source analysis
content: refine 1981 warnings and 1983 market comparison
feat: add sourced historical-data chart and oversight timeline
fix: address bilingual labels and presentation QA findings
test: document live browser media and Python integration checks
docs: finalize provenance, screenshots and self-review
```

**Important:** No changes were pushed to GitHub during this audit; no merged future Liron changes were reviewed. This document is an evidence-based **snapshot audit and proposed roadmap**.
