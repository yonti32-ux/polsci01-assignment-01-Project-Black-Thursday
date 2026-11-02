# PROMPT FOR GEMINI — Independent Examiner / Red Team (ready to send, **not yet sent**)

**Background:** We are two University of Haifa Political Science students, Yonatan and Liron (`polsci01`), completing the first AI Vibe Coding assignment. You are an independent skeptical reviewer, NOT a supportive teammate. You will receive: (1) a complete repository ZIP, (2) our two lecture summaries and the latest assignment/submission instructions, and optionally (3) the 1984 State Comptroller primary-source report. The project is **Black Thursday**, a Hebrew 14-slide HTML interactive presentation explaining Israel's 1983 bank-share crisis, containing a coded 3D video and working Python simulation.

## Your instructions

1. **Inspect actual files.** Read `README.md` and `PRD.md`, implementation code, real prompts, citations, testing reports, video or frames and the Git structure or provided commit evidence. If you cannot inspect something, say **NOT VERIFIED**, never infer it worked merely from the README.
2. **Grade against the course**, not imagined extra requirements. The documented deliverable is an **HTML presentation with an embedded 3D video and running Python** related to political science. Also evaluate PRD, README with real screenshots, meaningful Git history, original prompts and iterative work, creativity, accurate explanation, and required submission protocol.
3. **Historical red team:** Check *all material claims and dates* in the video and presentation against the supplied 1984 State Comptroller report, the 1993 report and Yale/other sources. In particular: the January–September 1983 real-return comparison **+8.6% all commercial-bank shares / −57.5% nonbank shares**; separate inventory (~US$1.06bn) from rescue costs; 6 October suspension; disputed reopening dates or duration conventions; 1981 warnings; public guarantees vs actual cash paid; 1983 bank-share arrangement vs 1985 stabilization. Quote only if accurately sourced.
4. **Financial/political-science review:** Evaluate whether institutional responsibilities, moral hazard, conflicts of interest, regulatory oversight and public costs are explained with nuance and without making a single politician the sole cause. Distinguish *fact, interpretation, illustration and simulation*.
5. **Visual/UX review:** Review all 14 slides and the actual **82-second v3 MP4** if accessible. Inspect text placement, font clarity, Hebrew RTL, graph proportionality, consistency of exact Liron palette, and whether the 3D footage is genuinely coded 3D. Avoid mislabeling raw WebGL and Python rendering as Three.js.
6. **Technical review:** Check app pathways (BAT → Python app → HTML → video and POST `/api/simulate`), actual functioning if tools permit, eight Python unit tests, mathematical/model caveats, input validation, no fake historical data, and resilience offline. Treat a successful direct HTTP response and a full browser button test as **different**.
7. **GitHub review:** Is there exactly one obvious canonical runnable project? Does README work from a clean clone? Do screenshot links resolve? Are real prompt exchanges preserved? Are dependencies and launch instructions adequate? Is the repository available to the lecturer? Mark unavailable/access checks **NOT VERIFIED** if you cannot access GitHub.
8. **Administrative review:** Group ID must be exactly `polsci01`, eight characters. The university official Word template must be filled only in existing fields and exported to PDF `polsci01-ex01.pdf` if exercise number is 01, individually submitted by **both students**. The PDF is not the GitHub README. Student IDs and private documents must not be public. Do not invent a template field if you haven't seen the template.
9. **Produce skeptical but fair feedback.** Identify severity: CRITICAL, HIGH, MEDIUM, LOW; with `path:line` or screenshot/frame/time references and reproducible reasoning. Don't say you tested a feature that you merely inspected statically.

## Required output structure

### A. Independent score recommendation
Give a **recommended academic score out of 100**, with a detailed rubric and explicit uncertainty due to unverified steps. This is **your external assessment**, not the official grade and not the team's chosen self-grade. Give a separate *confidence level* in your assessment (high/medium/low).

### B. Rubric table
Propose transparent weights that sum to 100 and cover: technical assignment completion, historical accuracy/political-science reasoning, design/video quality, real AI engineering/iteration/documentation, reliability/access and submission protocol. State these are **your proposed review weights**, not a purported official lecturer rubric unless the materials explicitly provide percentages.

### C. Evidence summary
Use **PASS / PARTIAL / FAIL / NOT VERIFIED** with file/screenshot evidence for each course requirement.

### D. Defect register
List precise issues, severity, impact, proof, and narrow proposed fixes. Especially flag unsourced claims, broken references, fake tests, historical accounting errors, source-ID confusion or misleading graphics.

### E. Three highest-return improvements
Rank fixes that could improve the assignment most without large scope creep. Prefer correctness and reproducibility to decorative changes.

### F. Submission readiness
Conclude **READY / CONDITIONAL / NOT READY**, separating code quality from the lecturer's necessary access and PDF steps.

### G. Constructive dissent
State at least two plausible challenges to the narrative/assumptions that a careful historian, political economist or software evaluator might raise.

**Integrity constraints:** No invented scores supposedly assigned by the lecturer, no false assertions that GitHub or Windows was tested, no conflation of 3D and Three.js, no unearned citation verification, and no pre-filled self-grade on our behalf. We will save your actual output under `docs/reviews/gemini-assessment-<date>.md` and document corrections in Git.
