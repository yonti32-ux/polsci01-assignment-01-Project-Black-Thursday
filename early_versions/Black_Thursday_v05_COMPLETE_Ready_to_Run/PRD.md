# PRD v1.2 — Video V3 Editorial & QA Addendum (2 November 2026)

**Team:** Yonatan and Liron | **Group code:** `polsci01` (eight characters). **Status:** candidate prepared for team approval; live browser/Windows verification remains open. Retains PRD v1.1 and original v1.0 below.

1. **Liron's second-round requirements are prioritized:** Retain seven-stage story, produce clean centered caption containers, abstract professional movements, business/political tone, verified chart quantities, uniform use of the exact nine-color palette `#1c242c #c19d43 #d3cebe #1f3c58 #8ab9ee #7a8694 #e7eef4 #f5cb39 #ed1c16`. Body text beige, positive returns blue, negative returns red.
2. **Working implementation:** `animation/render_movie_v3.py` re-renders original 3D mesh objects **without legacy caption overlays**, then applies a new original animated infographic layer. `animation/export_v3.py` creates the final **82-second, 1280×720, 20-fps H.264** film. The film is not a Three.js recording; the separate WebGL scene is preserved.
3. **Historical quantitative boundary:** Jan–Sep 1983 real returns are **+8.6% all commercial-bank shares** and **−57.5% nonbank shares**, from 1984 Comptroller, Table 1.3 (printed p. 19); measured from one shared zero baseline. This is **not** a historical daily bank index or a single-day October price drop. Share-support inventory **~US$1.06bn** on 6 Oct is **not** the bailout's cost.
4. **Precise institutional context:** Trading at the TASE was suspended on 6 October 1983, not the physical exchange “collapsing.” The original redemption schedule represented future rights for eligible shareholders, not instant 1983 payouts. The 1981 warnings / 1983 events frame the final political-accountability question.
5. **Documentation and rollback:** Native `<video>` on slide 9 references `crisis-animation-v3.mp4` and `video-poster-v3.png`; v1 and v2 remain available. Preserve actual partner prompt, export method, transcript, original screenshots, QA note, README status and history. No claim is made that this candidate has already been committed to GitHub.
6. **Acceptance:** playable video and real centering/colors/labels checked from decoded film frames. Required real Windows/browser review, student historical/editorial sign-off, and complete backend integration testing remain release gates. See `docs/ITERATION_v0.5_VIDEO_QA.md` and `animation/EXPORT_v3.md`.

---

# PRD v1.1 — Implementation Addendum (2 November 2026)

**Current group:** `polsci01` · **Team:** Yonatan and Liron. This is the **canonical PRD.md**, preserving the original baseline below as a historical record. The file `PRD 0.1.md` is intentionally retained in the repository; it must not be silently overwritten or deleted.

## Recorded decisions after the original specification

1. **What actually exists:** A 14-slide HTML/RTL presentation, a genuine 3D film, and a working Python educational scenario API. The source-code implementation uses **raw WebGL and a separate Python CPU mesh renderer**, rather than Three.js originally selected as a design technology. The actual 3D video is not represented as a Three.js render. See `Project-Black-Thursday-deliverable/animation/EXPORT.md` and `EXPORT_v2.md`.
2. **Liron's revised video requirement:** Clear, source-verified, visually organized seven-stage documentary; **60–90 seconds**; color palette `#1c242c #c19d43 #d3cebe #1f3c58 #8ab9ee #7a8694 #e7eef4 #f5cb39 #ed1c16`. Candidate v2 is an edited **72-second** version of existing real 3D footage, not a newly re-rendered scene from scratch. Preserve v1 for provenance/rollback.
3. **Easy to run:** Full interactive mode is a **one-click Windows batch launcher** backed by real Python (existing standard-library server fallback; no Flask installation required). **Static local file** preview is also supported for all slides/video; it does *not* execute Python simulation and explains that limitation on slide 13. The Python feature must work in full mode for the assignment to be accepted.
4. **Research upgrades:** The **1984 State Comptroller report** is the new primary source for the 1981 warnings, the **Jan–Sep 1983** real-return comparison (all bank shares +8.6% versus nonbank shares −57.5%), and the **US$1.06bn support inventory** by 6 Oct. It is not the **1993** audit that reports later state expenditure. See `docs/SOURCE_ID_CROSSWALK.md` to avoid colliding `Sxx` codes.
5. **Terminology and intellectual honesty:** Do not claim a real daily TASE composite index crashed by an invented percent; the exchange **suspended trading** on 6 Oct 1983, it did not itself declare bankruptcy. All 3D footage is schematic, not archive. A historically data-backed 9-month return chart is **not** a simulated daily stock-index series. Avoid a definite claim about 14 vs 18 days until counting basis is resolved.
6. **Release gate:** Windows double-click, Python simulation, all 14 slides/video, historical/source citations, captions, keyboard/RTL, GitHub public/shared visibility and each student's PDF submission **must be tested on the final computer**. This preparation does not certify those tests as passed. Use actual prompt logs and screenshots, not placeholders or synthetic evidence.

**Precedence:** For the decisions in items 1–6 only, this dated v1.1 addendum supersedes the older planned assumptions (Three.js-only movie, launch requiring terminal-only server, no compiled film). For all other requirements, keep the original PRD below. Once reviewed by both students, future revisions should be recorded as dated changelog entries, not untracked edits.

---

# ORIGINAL PRODUCT SPECIFICATION (v1.0, retained as originally committed)

# PRD — Black Thursday: The Political Economy of Israel's 1983 Bank-Share Crisis

> **Hebrew working title:** יום חמישי השחור: הכלכלה הפוליטית של משבר מניות הבנקים בישראל (1983)  
> **Deliverable:** A Hebrew, RTL, interactive historical documentary presented in HTML, containing a genuine 3D animated video and a functioning Python-powered educational simulation.  
> **Course:** Applications of Vibe Coding and AI in Science and Everyday Life, University of Haifa  
> **Assignment:** Exercise 01 — verify numbering against Moodle before submission  
> **Document version:** 1.0 — product specification baseline  
> **Date:** 2026-11-01  
> **Owners:** Two-student political science team — names to be added  
> **Group identifier:** TBD — must be exactly eight characters, with no spaces  
> **Status:** Direction C (documentary + simulation) selected; historical content and implementation subject to evidence checks and acceptance tests.

---

## 1. Executive summary

**Black Thursday** is a concise, research-grounded interactive documentary about the 1983 Israeli bank-share crisis. It explains how prolonged bank-share price support (ויסות מניות הבנקים), economic instability, investor behavior, institutional incentives, inadequate oversight, and political intervention interacted. The presentation tells the verified historical story, shows the financial mechanism through a Three.js 3D animation, and invites viewers to experiment with a **clearly hypothetical** Python simulation of financial-system stress and intervention.

**Our differentiator:** We connect an engaging visual experience to a political-science argument about institutions, accountability, risk transfer, and the state–market relationship. Every material historical claim will be traceable to a source. The audience will always be able to tell **historical fact**, **analytical interpretation**, and **educational simulation** apart.

**Primary deliverables:**
1. Navigable, fully Hebrew/RTL HTML presentation (target: 14 slides, allowable range 12–16).
2. A genuine 3D animated sequence designed in Three.js and exported as a playable video embedded in the presentation (target: 45–75 seconds); an optional live navigable 3D scene is a stretch goal.
3. Python computation that is actually executed and visibly affects a presentation component through a local HTTP API (Flask or similarly lightweight framework).
4. Verified references, source-to-claim mapping, quality-assurance evidence, and documented engineering iterations.
5. A complete GitHub repository with `PRD.md`, `README.md`, prompts, source code, screenshots, and meaningful commit history.
6. **Separate final administrative submission:** each student submits the university-provided Word form as a PDF to Moodle, without modifying its layout.

### 1.1 Assignment requirements versus project choices

| ID | Status | Requirement or design choice | Evidence of completion |
|---|---|---|---|
| A01 | **Course requirement** | Subject relates to political science | Research question, analysis, sources |
| A02 | **Course requirement** | HTML presentation | Working `presentation/index.html` served locally |
| A03 | **Course requirement** | 3D animated video within presentation | Embedded playable MP4/WebM created from genuine 3D scene |
| A04 | **Course requirement** | Running Python component used by the presentation | API response and updated on-screen visualization |
| A05 | **Course guidance** | Plan in `PRD.md` before implementation | This document in repository |
| A06 | **Course requirement** | Repository + accessible lecturer review | Public repository or explicit access for `rmisegal@gmail.com` |
| A07 | **Course requirement** | Full prompt development trail and readable README | `prompts/`, detailed `README.md`, actual screenshots |
| A08 | **Course emphasis** | Iterations, testing, meaningful Git pushes | Git history, change notes, QA report |
| A09 | **Submission requirement** | Exactly eight-character unique group ID | Validated group string |
| A10 | **Submission requirement** | One PDF form per student, correct filename | `xxxxxxxx-exyy.pdf`, individually uploaded |
| A11 | **Submission requirement** | Justified recommended self-grade | Score rationale and evidence |
| D01 | **Team design choice** | 14 Hebrew slides, 45–75s 3D video, scenario simulator | Product review / acceptance tests |

**Course-source basis:** Lecture 2, section 11.1–11.4 (printed pp. 21–23): HTML + 3D video + running Python, PRD, GitHub, iteration, approximately 4–8 shared hours and up to ~20 slides; Lecture 1, sections 3 and 9: domain expertise stays with students and independent red-team QA. The lecturer's newer written instructions supplied by the team govern submission details where more specific.

---

## 2. Problem, purpose, and political-science thesis

### 2.1 Problem

The 1983 crisis is often compressed into a simple narrative of a stock-market crash or blamed on a single political figure. This obscures the longer-running share-support practices, structural incentives, state oversight, and the distinction between preventing systemic collapse and distributing the financial burden.

### 2.2 Central research question

**How did the incentives and actions of Israeli banks, investors, regulators, and political leaders contribute to the 1983 bank-share crisis, and what does the intervention reveal about state responsibility, accountability, and financial stability?**

### 2.3 Supporting questions

- What was **ויסות מניות הבנקים** and why could it not continue indefinitely?
- How did inflation, currency expectations, and investor behavior contribute to selling pressure?
- Which public and private institutions had authority, information, and incentives to intervene?
- What did the October 1983 rescue arrangement stabilize, and what public obligations did it create?
- What did subsequent inquiries, particularly the Bejski Commission, identify as failures?
- What generalizable political-economy trade-offs arise when governments rescue financial institutions?

### 2.4 Analytical framework

Use these **interpretive lenses**, clearly labeled as analysis rather than historical findings: (i) principal–agent problems; (ii) conflicts of interest and regulatory oversight; (iii) moral hazard and incentives; (iv) systemic risk and collective action; (v) distribution of costs between private actors and the public. Cite scholarship where a specific theoretical claim is used.

### 2.5 Learning outcomes

By the end, a viewer should be able to:
1. Explain share-price support in plain Hebrew using a supply/demand diagram.
2. Identify at least three actor groups and their distinct incentives.
3. Place the major October 1983 events in their correct order.
4. Differentiate the historical state rescue from a hypothetical modern teaching model.
5. Articulate at least one policy trade-off and one institutional accountability question.

---

## 3. Audience, delivery, and design principles

**Primary audience:** University of Haifa lecturer and undergraduate students familiar with political science but not necessarily finance or programming.  
**Language:** Hebrew for narrative/UI; English only for unavoidable technical terms, with proper RTL/BiDi handling.  
**Delivery context:** A 7–10 minute guided presentation, also usable independently in Chrome/Edge on Windows.  
**Use environment:** Local machine with Python 3, current browser, and no requirement to purchase AI services or connect to paid APIs.  
**Presentation format:** 16:9, readable at 1366×768 and higher, with smaller-screen fallback; keyboard and mouse support.

### Core principles

- **Truth before spectacle.** No invented quotes, dates, archival footage, financial datasets, or attributions.
- **Clear visual semantics.** Money flows, inventory, intervention, and risk should be visible, not buried in narration.
- **Interactive for a reason.** Controls help investigate assumptions; they do not pretend to recreate historical counterfactuals reliably.
- **Technical resilience.** The slides work even if WebGL or the optional Python service fails; the missing feature is labeled honestly.
- **Full provenance.** Record who produced each visual and where each historical fact and dataset came from.
- **No false certainty.** Describe disputed responsibility and differing cost estimates with appropriate nuance.

---

## 4. Historical accuracy and evidence policy

### 4.1 High-confidence factual anchors — confirmed during PRD research

| Fact / event | Minimum authoritative support | Narrative use |
|---|---|---|
| Israeli banks systematically purchased/supportively traded their own shares, distorting market prices | State Comptroller of Israel (1993); Leonard (2021) | Mechanism and background |
| Inflation and currency devaluation formed important context; investors increasingly shifted toward foreign-currency holdings | Leonard (2021), Yale | Macro context and selling pressure |
| Tel Aviv Stock Exchange was closed beginning **6 October 1983** for **18 days**, reopening **24 October 1983** | Leonard (2021); Yale New Bagehot case | Precise dated timeline |
| Government negotiated an arrangement to protect eligible shareholders, involving significant public obligations | State Comptroller (1993); Leonard (2021) | Government response and cost allocation |
| The Bejski inquiry report was published in **1986** | Yale case; follow-up official sources to be added | Accountability and aftermath |
| **Yoram Aridor was Minister of Finance**, not “Minister of Economy”; he resigned **13 October 1983**, amid controversy over a proposed dollarization plan | Contemporary Washington Post report dated 14 October 1983 | Political context, not monocausal explanation |

### 4.2 Cost figures require special care

Do **not** combine figures that use different accounting definitions, dates, or dollar bases. For example, the State Comptroller's 1993 report states expenditures equivalent to approximately **$9.1 billion through October 1991, including financing costs through that date**. The Yale material presents multiple figures, including approximately **$9.2 billion** in one cumulative comparison and **$6.9 billion** under a different program-size/valuation definition. A slide should give the **exact cited source, price basis, timeframe, and what is being measured** beside any number. If those cannot be reconciled reliably, report them as differing estimates, not as interchangeable totals.

### 4.3 Source hierarchy

1. Official State Comptroller reports, Bank of Israel publications, government inquiry material, contemporaneous official documents.
2. Peer-reviewed or scholarly case studies with transparent citations (e.g., Yale School of Management).
3. Reliable historical reporting from the period, clearly designated as contemporaneous accounts.
4. Retrospective news coverage for context.
5. Wikipedia only as a starting index of potential sources, **not** sole evidence for disputed claims.

### 4.4 Mandatory citation workflow

- Create `research/claim-register.csv` with: `claim_id`, `slide`, `hebrew_claim`, `source_id`, `page_or_section`, `verified_by`, `status`, `notes`.
- Every **material on-slide historical assertion or exact number** must map to at least one specific source.
- Add unobtrusive source keys (e.g., `[S01]`) to relevant slides and full references on the final slide / `research/sources.md`.
- Quote primary sources verbatim only when wording has been checked; otherwise paraphrase accurately.
- Mark reconstructions **"המחשה חזותית — לא תיעוד היסטורי"** and model output **"סימולציה לימודית — לא נתונים היסטוריים"**.
- Do not recreate the facial likeness or spoken words of historical figures and present them as authentic footage.
- Before release, two student reviewers confirm every `verified` claim against the cited passage.

### 4.5 Scope boundary between events

The product is about the **1983 bank-share crisis**. The **1985 economic stabilization plan** may appear only as subsequent context, never as the immediate rescue mechanism of October 1983.

---

## 5. Product experience and slide-by-slide storyboard

**Navigation model:** home, previous, next; slide counter/progress bar; direct selection via overview; keyboard Left/Right with RTL-aware mapping documented; optional `Esc` to exit expanded media. All slides present a source badge when they include historical claims.

| # | Hebrew title / teaching point | Core visual | Source or interaction |
|---|---|---|---|
| 01 | **יום חמישי השחור — 1983** — hook and question | Cinematic 3D-derived hero still; discreet date | Present the research question |
| 02 | **ישראל בתחילת שנות ה-80** — inflation/currency context | Three fact cards with citations; sourced chart if available | Source-backed macro context |
| 03 | **מי פעל בתוך המערכת?** — banks, public, regulators, government | Actor/institution relationship network | Distinct roles and incentives |
| 04 | **מהו ויסות מניות?** — define support mechanism | Supply–demand and bank buyback animation | Historical explanation |
| 05 | **איך המחיר נתמך?** — circular support and resource use | Animated money-flow objects | Explicitly schematic, not exact records |
| 06 | **מדוע זה היה מסוכן?** — limits of support | 3D bank inventory and finite reserve meter | Structural mechanism |
| 07 | **סימני האזהרה** — increasing pressure in 1983 | Annotated timeline | Dated source-backed milestones only |
| 08 | **6 באוקטובר 1983** — exchange closes | Timeline centerpiece and closing-market transition | Exact historical date |
| 09 | **כך התפתח המשבר — סרט תלת-ממד** | Embedded 3D animated **video** with captions | Play/pause/replay/volume controls |
| 10 | **ההסדר וההתערבות** — October rescue and trade-offs | Government–banks–public flow diagram | Separate immediate steps from future redemptions |
| 11 | **מה היו המחירים והתוצאות?** | Source-qualified cost comparison and consequences | No mixed-base cost infographic |
| 12 | **מי נושא באחריות?** — competing institutions and inquiries | Four-column accountability matrix | Evidence versus interpretation labels |
| 13 | **מעבדת מדיניות: מה היה קורה אילו?** | Python-fed scenario comparison + chart | Interactive, visibly hypothetical model |
| 14 | **מסקנות, מגבלות ומקורות** | Three takeaways, source list and methodology note | Research question answered |

**Slide copy constraints:** One principal message per slide; default 35–65 Hebrew words for main text (not counting source notes); narrator notes may be longer. No wall of text. Formal historical analysis remains students' editorial responsibility.

**Narrative structure:** setup → mechanism → unsustainability → October 1983 collapse → public intervention → accountability and implications → hypothetical exploration.

---

## 6. Three.js animation specifications

### 6.1 Required deliverable

A locally playable video file (`media/video/crisis-animation.mp4`, with WebM optional) **rendered from a coded 3D scene** and embedded on slide 09 using an HTML `<video>` element. The source Three.js scene must remain in the repository as inspectable code. The video must be independently playable even if live WebGL is unavailable at presentation time.

- **Length target:** 45–75 seconds; ideal ~60 seconds.
- **Format:** 16:9, minimum 1280×720, MP4/H.264 where practical; browser-compatible fallback as needed.
- **Scene composition:** Actual 3D geometry with depth, lighting, shadows, camera motion, and perspective (e.g., bank buildings, share tokens, arrows, investor groups, reserve/capacity meter).
- **Language:** Hebrew captions overlaid in the video or synchronized to it; optional voiceover only if intelligible and properly licensed/created.
- **Labels:** Schematic illustrations must be marked; do not claim real bank cashflows or real share prices.
- **Sound:** Not required for comprehension; mute controls and accessible captions.

### 6.2 Shot list

| Time (approx.) | Shot | Movement and historical teaching purpose |
|---|---|---|
| 00–10 s | Banks and investor sphere | Establish actors with a slow camera orbit |
| 10–22 s | Share issuance and supportive purchases | Show bank purchases supporting the shares' apparent stability |
| 22–34 s | Resources become constrained | Reserve meter decreases; explain finite ability to absorb selling |
| 34–48 s | Selling surge and confidence break | Faster flow toward selling; market-support system no longer sustainable |
| 48–62 s | Government response | State guarantee/arrangement shown as public intervention, not instant elimination of all costs |
| 62–70 s (optional) | Political-economy question | Transition to the institutional-accountability slides |

**Media creation approach:** Design and animate in Three.js, record a deterministic camera sequence with a reliable desktop/browser capture workflow, trim/compress, export and replay in Chrome/Edge. Preserve source and an export note explaining how the video was made. A rotating live 3D companion view is *optional* and must not substitute for the mandatory embedded video.

**Fallback:** If video codec support fails, offer a second supported source or a still image with an explicit playback troubleshooting note; the build is not considered accepted until at least the primary target browser plays the actual video.

---

## 7. Python-powered educational simulation

### 7.1 Purpose and validity boundary

The simulation demonstrates **how assumptions about confidence, selling pressure, banks' capacity to absorb selling, and government intervention may affect financial stress** in a simplified hypothetical system. It **does not** estimate the actual bank-share prices, the historical probability of crisis, the fiscal costs of the rescue, or what definitely would have happened with different government policies.

**Always show, next to the chart:**  
**"סימולציה להמחשה בלבד. הפרמטרים אינם כיול לנתוני 1983, ואין לראות בתוצאה תחזית או שחזור היסטורי."**

### 7.2 Inputs and outputs

| Input | Type / permitted values | Interpretation |
|---|---|---|
| `confidence` | Integer 0–100 (default 65) | Initial hypothetical investor confidence |
| `sell_pressure` | Integer 0–100 (default 50) | Exogenous selling pressure |
| `bank_capacity` | Integer 0–100 (default 55) | Total limited bank support available |
| `intervention` | `none`, `delayed`, `early` (default `early`) | Timing of hypothetical public support |

**Outputs** (over 12 illustrative periods):
- A **stability index** initialized at 100 (unitless, **not** a historical share-price series).
- Unabsorbed selling pressure per period.
- Remaining bank support, intervention support used, and cumulative unmet demand (all illustrative units).
- One-sentence Hebrew interpretation of the comparison, explicitly conditional on model assumptions.
- Ability to reset inputs, compare two runs, and reproduce identical results with identical inputs.

### 7.3 Modeling guardrails

- Implement a **deterministic, transparent toy model** in `python/simulation.py`; no machine-learning claims and no undisclosed randomness.
- Document all formulae, parameter choices, and arbitrary teaching coefficients in `docs/model-methodology.md`.
- Each period must account for **finite total support budgets**, so the simulation cannot create unlimited funds.
- Compute selling demand from the inputs and a documented confidence feedback term; allocate buying capacity, then intervention support; record any unmet demand. A bounded stability index responds to unmet demand. State the equation alongside the implementation.
- Never label an index as "bank share index 1983" or use historic dates on its horizontal axis.
- Compare identical base conditions under different policy settings; avoid causal assertions broader than the model.
- Include a clear disclaimer in the output and source code comments.

### 7.4 Integration contract

**MVP choice: Python Flask server.** It serves the HTML presentation **and** a JSON API, avoiding CORS complexity.

```text
Browser (HTML/CSS/JavaScript)
  ├── 14-slide presentation
  ├── <video> showing Three.js-derived 3D animation
  └── Slide 13 controls / comparison chart
             │ POST /api/simulate (JSON)
             ▼
Python Flask app (local, e.g., http://127.0.0.1:8000)
             │
             ▼
Deterministic simulation.py
             │ JSON metrics & time series
             ▼
JavaScript chart + clearly labeled explanatory text
```

**API contracts:**
- `GET /api/health` → `{ "status": "ok", "model_version": "1.0" }`.
- `POST /api/simulate` with four validated inputs → `{ "inputs": {...}, "periods": [...], "summary": {...}, "model_version": "1.0", "historical": false }`.
- Reject malformed/out-of-range input with HTTP 400 and a readable JSON error.
- `GET /` serves the presentation and static assets.
- The app runs locally with `python -m pip install -r requirements.txt` and `python python/app.py`; exact launch instructions will be finalized after the first successful run.

**Offline behavior:** No remote API calls at runtime. If the server is unavailable, presentation content and video remain readable via static delivery, while the simulator shows an honest "Start the Python app" message instead of silently displaying fabricated results.

---

## 8. UX and visual design system

**Art direction:** Serious, contemporary financial documentary; historical atmosphere without fake photographs. Graphite/navy backgrounds, restrained antique-gold accents for institutions, muted green for inflows/stability, restrained red for stress, cream/off-white for main text.

- Hebrew RTL layout using `<html lang="he" dir="rtl">`; wrap LTR dates, numbers, code, URLs in appropriate `<bdi>` / direction-safe containers.
- Headline typography large enough for projection; body text approximately 24–30 px at presentation scale; source lines ~14–16 px, legible when expanded.
- Maintain strong contrast and non-color labels (patterns, text, or icons) for charts.
- Standard layout: title, one key insight, main visual, small provenance line.
- Interactive controls must have keyboard focus, labels, hover/focus indication, and clear loading/error states.
- Navigation and playback may not require network connectivity.
- Respect `prefers-reduced-motion` for UI transitions. The film's play/pause remains controllable.
- Provide captions/transcript (possibly an accessible text panel) for the 3D film.
- Browser should not autoplay sound; require deliberate user playback.

### 8.1 Visual assets and copyright

Prefer original vector/3D graphics generated from code, verifiable public-domain materials, or individually licensed archival assets. For every third-party image/video/audio asset, record: creator, source URL, license, attribution requirement, and repository usage rights in `media/ASSET-CREDITS.md`. Do **not** simply copy newspaper pages, course slides, or licensed archival photographs into a public repository without permission. Reuse of course diagrams is not required; recreate concepts in original graphics instead.

---

## 9. Technical architecture and repository specification

### 9.1 Stack

- HTML5 + CSS3 + vanilla JavaScript for the presentation.
- Three.js for source 3D scene and animation.
- Native HTML5 `<video>` for recorded animation playback.
- Python 3.11+ and Flask for model execution and local content serving.
- Browser Canvas or light SVG for time-series chart; avoid introducing a chart dependency unless it saves time.
- Git / GitHub for version control; Markdown for requirements, notes, and prompt transcripts.

**Rationale:** Minimize fragile dependencies, keep AI-generated code inspectable, retain genuine 3D depth, and demonstrate real Python integration. Avoid building a full React app, remote hosting backend, database, login system, or AI runtime agents for a 4–8-hour class project.

### 9.2 Proposed directory structure

```text
<8-character-group-code>/
├── README.md
├── PRD.md
├── requirements.txt
├── .gitignore
├── presentation/
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── slides/
├── animation/
│   ├── scene.html
│   ├── scene.js
│   └── EXPORT.md
├── python/
│   ├── app.py
│   ├── simulation.py
│   └── tests/
├── media/
│   ├── video/
│   │   └── crisis-animation.mp4
│   ├── screenshots/
│   ├── images/
│   └── ASSET-CREDITS.md
├── research/
│   ├── sources.md
│   ├── historical-timeline.md
│   └── claim-register.csv
├── prompts/
│   ├── 01-original-trial-prompt.md
│   ├── 02-planning-and-prd.md
│   └── [subsequent real prompts in chronological order]
└── docs/
    ├── model-methodology.md
    ├── development-log.md
    ├── testing-report.md
    └── release-checklist.md
```

**Important:** The `prompts/` files must preserve **actual prompts and outcomes**. Don't fabricate a chronological conversation. Copy the team's genuine first trial prompt unchanged; record this planning/PRD instruction and subsequent development instructions with their dates, model/tool, output, observed defects, and corrections.

### 9.3 README specification

The root `README.md` must include: project title and one-paragraph pitch; political-science research question; team/course information (exclude sensitive IDs); screenshot of title slide; actual frame from 3D video; screenshot of Python-generated simulation result; technologies; setup and run commands; how to navigate and change simulation inputs; source list and methodology caveat; architecture diagram; development milestones and test status; licenses and credits; authorship/AI-assistance transparency.

Use **relative file links**, e.g. `media/screenshots/slide-01.png`, so images render on GitHub. Screenshots must be real captures of outputs, not AI-generated mockups purporting to be the implemented app.

### 9.4 Git strategy

Keep meaningful commits and **push throughout development**. Suggested checkpoints:
1. PRD and source plan.
2. Validated historical timeline and storyboard.
3. First functioning HTML slides.
4. First actual Three.js animated scene.
5. Video export and embedded playback.
6. Python API + first successful chart update.
7. Accessibility/RTL/performance fixes.
8. QA report, screenshots, polished README, release tag.

Commit messages describe *what changed and why*. No meaningless pushes just to inflate counts. Preserve broken versions in Git when useful for demonstrating iteration, but release a working baseline.

---

## 10. Functional requirements with measurable acceptance criteria

| Req. | Priority | Definition of done / test |
|---|---|---|
| FR-01 | Must | Launch project locally from documented instructions without paid services |
| FR-02 | Must | All 14 planned slides reachable by next, previous, home, and keyboard; no dead ends |
| FR-03 | Must | Hebrew RTL correct on all slides, including mixed dates, percentages, and citations |
| FR-04 | Must | Slide 09 contains a video produced from an actual 3D-coded scene; native controls work |
| FR-05 | Must | Animation source contains true 3D geometry, camera motion, and intended depth |
| FR-06 | Must | Python process starts; `GET /api/health` succeeds; slide 13 calls `POST /api/simulate` |
| FR-07 | Must | Changing at least one input changes rendered output; identical inputs produce identical output |
| FR-08 | Must | Invalid inputs rejected gracefully; browser displays an understandable error, not a crash |
| FR-09 | Must | Simulation explicitly labeled hypothetical in UI, chart, code, and documentation |
| FR-10 | Must | Historical claims and figures on slides trace to registered sources |
| FR-11 | Must | GitHub README shows real slide/video/simulation screenshots and working setup steps |
| FR-12 | Must | Prompt log, PRD, historical sources, Git history and test report all in repository |
| FR-13 | Must | Repository visible to lecturer (public OR successful invitation to specified email) |
| FR-14 | Must | Reporting Word template untouched in layout, filled correctly, converted to PDF and submitted by each student |
| FR-15 | Should | Source link available per slide; final bibliography easy to navigate |
| FR-16 | Should | Layout readable at 1366×768; no clipped Hebrew, controls or charts |
| FR-17 | Should | Tested in current Chrome and Edge; external assets unnecessary at playback time |
| FR-18 | Could | Live 3D orbit camera or interactive scene as supplementary feature |
| FR-19 | Could | Brief optional narration and synchronized subtitle track |
| FR-20 | Could | Presenter notes, alternative overview/navigation view |

### Non-functional targets

- **Reliability:** Zero uncaught frontend errors during a complete guided run; simulation processes 20 consecutive valid requests; invalid input handled safely.
- **Performance:** Presentation loads in under ~5 seconds on team's primary Windows laptop on local server; 3D scene aims for smooth playback on that device (target 30 fps where interactive).
- **Portability:** The documented local launch path works from a fresh Git clone with installed Python and specified dependencies; no absolute file paths.
- **Security:** Server binds to `127.0.0.1` by default, never requires user credentials, and runs no shell commands from HTTP inputs.
- **Privacy:** Do not commit students' ID numbers, account tokens, personal documents, or submission forms containing sensitive information.
- **Reproducibility:** Exact models/parameters and source versions documented; dependencies pinned or bounded reasonably.
- **Maintainability:** Separate slides, presentation styles/logic, animation source, and Python model; include clear comments for non-obvious formulas.

---

## 11. QA and independent red-team review

### 11.1 Test matrix

| Test ID | Test | Acceptance evidence |
|---|---|---|
| T01 | Clone and run from README | Clean local startup and screenshot of terminal/health endpoint |
| T02 | Navigate slides forward/backward/home/keyboard | Correct slide counter, no unreachable pages |
| T03 | Verify RTL, dates, source badges on every slide | Screenshots at target resolution; no overlapping or reversed text |
| T04 | Play complete 3D movie; replay, pause, captions | MP4 plays end-to-end and controls work |
| T05 | Confirm genuine 3D scene | Source reviewed; depth visible on camera orbit |
| T06 | Change confidence or intervention in simulator | Updated graph and values returned by Python |
| T07 | Repeat same inputs; compare outputs | Exactly matching deterministic JSON results |
| T08 | Stress input edge cases: 0, 100, invalid strings, omitted values | Valid bounded results or HTTP 400, no server traceback |
| T09 | Stop Python server and open presentation | Fallback message honest; other slides still readable |
| T10 | Audit historical timeline and all displayed numbers | Claim register contains support and reviewer verification |
| T11 | Audit all costs and currency bases | Different cost estimates never visually conflated |
| T12 | Audit assets and citations | No unlicensed copyrighted material or unverifiable figure |
| T13 | Inspect GitHub page and repository permissions | Lecturer can access; screenshots render and files are present |
| T14 | Final PDF submission check | Correct eight-character name, assigned exercise number, unchanged form layout |

### 11.2 Red-team procedure

1. Primary building model creates a version.
2. Team performs direct manual testing, including reading historical source passages.
3. A **different LLM**, acting as a skeptical committee (historian, political economist, statistician, software QA engineer, accessibility reviewer, academic integrity reviewer), audits the repo and outputs a severity-ranked defect list. Roles are a prompting method, **not** actual independent human experts.
4. Team checks criticisms against evidence, fixes genuine defects, and documents rejected suggestions with rationale.
5. Repeat until all critical/high-severity defects are closed or explicitly accepted as documented limitations.

**Stop rule:** Do not pursue polish while required functionality or source accuracy is still unresolved. Submit only when every *Must* acceptance test passes.

---

## 12. Development roadmap, ownership, and risks

### 12.1 Work order and collaborative estimate

| Phase | Activities | Indicative team time | Exit gate |
|---|---|---:|---|
| P0 — Scope | Confirm topic, group code, slides, PRD | 30–45 min | PRD agreed, repository initialized |
| P1 — Research | Verify timeline, disputed figures, sources, copy | 45–75 min | Claim register ready for scripted facts |
| P2 — HTML | Navigation, slide shell, typography, visual layout | 60–90 min | All slides reachable and RTL tested |
| P3 — 3D | Three.js scene, camera sequence, film export | 75–120 min | Recorded 3D video plays in slide |
| P4 — Python | Toy-model formulas, API, chart, error handling | 45–75 min | Controls visibly trigger Python |
| P5 — QA & docs | Red-team, screenshots, README, Git, final package | 60–90 min | All Must gates pass |

**Planning note:** The lecturer mentions 4–8 hours of team work. This is a target, not a quality guarantee; trim stretch goals first if the estimate slips.

**Suggested responsibilities:** Student A leads historical sourcing, slide narrative, and claim validation; Student B leads implementation, 3D export, and Python integration. Both review the political-science conclusion, test the app, author genuine prompts, and sign off on release. Adjust to actual skills.

### 12.2 Risks and mitigation

| Risk | Severity | Mitigation |
|---|---|---|
| Historical oversimplification or blame assigned to one politician | High | Multi-actor framework; two-person claim review |
| Mixing differing fiscal cost figures | High | Source metadata, timeframe and accounting basis beside all numbers |
| Video doesn't play or is merely 2D-looking | High | Genuine Three.js source, screen recording, MP4 playback gate |
| Python exists but presentation does not use it | High | Concrete API request and visible graph update on slide 13 |
| Local-file CORS/path errors | Medium | Run presentation through Python server on same origin |
| Browser/device performance | Medium | Simplify geometry, compress video, provide fallback |
| Scope creep on simulation realism | High | Teaching model explicitly hypothetical; no data-fitting claims |
| GitHub lacks development evidence | High | Commit and push after each actual milestone; prompt log from start |
| Public repository contains copyrighted files or private IDs | High | Asset register; no IDs/tokens; submit form only through Moodle |
| Incorrect PDF template/filename or inaccessible repository | Critical | Separate administrative QA checklist with both students' signoff |

---

## 13. Release and submission protocol

1. Freeze a version (`v1.0.0`) only after historical, UI, animation, and Python tests pass.
2. Run from a clean checkout, following only the README; record success.
3. Capture actual screenshots: opening slide, 3D video playing, simulation result, Python process/endpoint; verify each link displays inside GitHub README.
4. Ensure `PRD.md`, `research/`, `prompts/`, `docs/testing-report.md`, and working code are all committed and pushed.
5. Confirm unique **eight-character** group ID; select correct `exyy` number from Moodle (expected `ex01`, not assumed definitive).
6. Make repository **public**, or explicitly share with `rmisegal@gmail.com`; test access while logged out or from an allowed account.
7. Complete only the provided Word template fields; **do not alter layout or insert extra commentary**. Save as `xxxxxxxx-exyy.pdf`. Do not use Word format as the submission.
8. Have **each student** submit their own PDF to Moodle; verify upload status individually. Provide a justified self-grade according to the form instructions.
9. Plan for the lecturer's late penalty: **5 points for every 24-hour delay**. Exceptional circumstances require an official university authorization, not private medical documentation uploaded to the lecturer.

**Release blocker:** If any major deliverable is inaccessible, nonfunctional, historically misleading, or not committed, do not mark this release complete.

---

## 14. Out-of-scope and future enhancements

**Out of scope for Exercise 1:** Fully realistic econometric reconstruction, market data prediction, film-quality photorealistic historical figures, user accounts, a database, online multiplayer, live financial APIs, unsourced real historical price curves, universal mobile optimization, full documentary-length narrated film, and a public backend hosting deployment.

**Optional extensions after core completion:** More detailed historical timeline, live orbit camera, user-selectable model assumptions, sourced historical datasets and comparative institutional case studies. All extensions are gated by the assignment time budget and required functionality.

---

## 15. Change control and open decisions

**Decided now:** Historical focus = October 1983 bank-share crisis; Direction C hybrid; Hebrew RTL; approximately 14 slides; Three.js-coded 3D video; Python-executed simulation; professional GitHub/QA documentation; accuracy-first framing.

**Decisions pending first implementation:**
- Exact eight-character group identifier and student responsibilities.
- Whether final video will include voiceover; captions are mandatory either way.
- Exact verified historical figures, labels and any charts on slide 02/11 after source-level review.
- Specific test machine/browser versions and final supported resolution.
- Whether a supplementary orbitable 3D scene fits the time budget.
- Exercise number, Moodle deadline and official submission template when available.

**Change process:** Update the relevant PRD subsection, increment document version (e.g., 1.1), describe the reason in `docs/development-log.md`, and create a meaningful Git commit. Avoid undocumented scope changes.

---

## 16. Sources, methods, and provenance

### Course specification sources

- **L01** — Dr. Yoram Segal, *Lecture 1: Introduction to AI, LLM and Vibe Coding*, 13 October 2026, University of Haifa. Especially printed pp. 3–5, 13–15: the student as AI manager, professional judgment and red-team testing.
- **L02** — Dr. Yoram Segal, *Lecture 2: Pixels, Objects and Vectors*, 20 October 2026, University of Haifa. Especially printed pp. 18–23: HTML slide design, Three.js, PRD, Github, 3D video and Python integration.
- **Course submission notice** — User-provided Hebrew instructions on GitHub access, group code, PDF template/filename, independent Moodle submission, recommended grade, lateness and privacy. The notice governs the applicable administrative requirements.

### Historical verification sources (seed bibliography)

- **S01** — State Comptroller of Israel (4 January 1993), *ההיערכות למכירת מניות הבנקים שבהסדר*. https://library.mevaker.gov.il/sites/DigitalLibrary/Pages/Publications/641.aspx  
  Particularly: manipulation, distortion of market versus economic value, rescue obligations, reported expenditure and the distinction between expenditure and net state loss.
- **S02** — Natalie Leonard (2021), *Israeli Bank Shares Arrangement (Hesder Hamenayot Habankayot)*, *Journal of Financial Crises* 3(3), 210–227. https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss3/13/  
  Particularly: background, 6 October closure, 18 days, government arrangement and time-dependent cost definitions.
- **S03** — Yale Program on Financial Stability / New Bagehot Project, case details for *Israeli Bank Shares Arrangement*. https://newbagehot.yale.edu/docs/israeli-bank-shares-arrangement-hesder-hamenayot-habankayot  
  Especially the timeline, governance arrangements, and alternative program cost estimates.
- **S04** — Edward Walsh, *Israel's Finance Minister Quits in Row Over Plan Tying Economy to Dollar*, *The Washington Post*, 14 October 1983. https://www.washingtonpost.com/archive/politics/1983/10/14/israels-finance-minister-quits-in-row-over-plan-tying-economy-to-dollar/95eb7e07-e2a0-4c03-a888-4f1c1fb3c40a/  
  Contemporary evidence for Aridor's portfolio, resignation and dollarization controversy.
- **S05** — Marshall Sarnat, *20 שנה למשבר מניות הבנקים*, *Ynet*, 9 September 2003. https://www.ynet.co.il/articles/1,7340,L-2749362,00.html  
  Retrospective analysis by a former Bejski Commission member; use as attributed interpretation, not as an official ruling.

### Provenance and claim status

The factual anchors in §4 were checked against the cited sources during PRD preparation. This **does not** constitute final line-by-line verification of every future slide, video caption or number. Those are separately required by FR-10/T10 and the claim register. The analytical frameworks, interface design, simulation behavior, and development plan are **team design proposals**, not facts stated in historical or lecture sources.

---

## 17. Sign-off

| Gate | Reviewer | Status |
|---|---|---|
| Topic and research question approved | Student A / Student B | Proposed for sign-off |
| PRD scope approved | Student A / Student B | Proposed for sign-off |
| Historically sourced storyline | Both reviewers | Pending production |
| Three.js video acceptance | Both reviewers | Pending implementation |
| Python integration acceptance | Both reviewers | Pending implementation |
| Red-team and final QA | Both reviewers | Pending implementation |
| GitHub and PDF submission access | Both students individually | Pending submission |

**Product definition of success:** A reviewer can clone the repository, follow the README, experience a visually coherent 14-slide Hebrew presentation, play a genuine 3D animated video, run a Python-powered interactive hypothetical scenario, inspect sources for all significant historical claims, and trace the team's AI-directed iteration process through prompts, Git commits and QA evidence.
