# Independent AI Assessment — Project Black Thursday

**Review date:** 2 November 2026  
**Reviewed submission:** `assignment 01(2).zip` uploaded by Yonatan and Liron  
**Group code:** `polsci01`  
**Assessment purpose:** Skeptical academic and engineering review before final Moodle submission.  
**Reviewer:** ChatGPT (GPT-6). This is **not** the lecturer's official grading or an officially supplied rubric.

## Executive verdict

**Current ZIP as delivered: 81 / 100 (provisional).** The intellectual and implemented product is strong, but the repository is **not submission-ready in its present structure**. A reviewer starting from the ZIP root will encounter a broken README and no root launcher, while the actual runnable build is nested one level deeper. There are also duplicate earlier builds and a Git remote discrepancy.

**Estimated product-only quality, if the correct nested build is deliberately launched: ~89 / 100.**  
**Realistic target after the listed high-priority fixes and human browser sign-off: ~90–93 / 100.**  
These estimates are reviewer judgments, **not promises** of the instructor's grade.

### Provisional rubric (constructed for this review)

| Criterion | Maximum | Awarded | Assessment |
|---|---:|---:|---|
| Historical research & political-science interpretation | 20 | **18** | Strong official sources and multi-actor explanation; some claim entries remain pending exact-page or team verification. |
| Hebrew HTML presentation & visual communication | 20 | **17** | 14 coherent interactive slides, polished consistent aesthetic; end-to-end browser experience not verified in this environment. |
| 3D video, clarity & originality | 20 | **17** | Real 82s H.264 documentary, controlled color system, factual comparative returns and inspectable code; 3D background is subordinate to infographic overlays and full playback is not independently witnessed here. |
| Python integration & technical behavior | 15 | **14** | Actual local API and deterministic model, eight passing tests, appropriate historical-simulation disclaimer, correct response paths. |
| PRD, prompt engineering, process & QA | 15 | **12** | Genuine prompts, iterative variants, documentation and meaningful Git history; incomplete source and editorial sign-offs; repeated files and unreconciled copy locations. |
| Repository discoverability, reproducibility & submission readiness | 10 | **3** | Broken README links and invalid root launch instructions; redundant builds and unresolved remote; no verified instructor access or official PDF. |
| **TOTAL** | **100** | **81** | **Release candidate, NOT final submission approval** |

> This rubric emphasizes all three actual course artefacts—HTML, 3D video and running Python—and evaluates the AI-driven engineering trail, as described in the supplied Lecture 1/Lecture 2 summaries and current lecturer's written instructions. Exact weights are my own because no official point-by-point rubric was supplied.

## What I actually inspected

- ZIP directory layout, root documents and nested release-candidate tree; approximately **700 entries** in ZIP, including Git internals and multiple historic builds.
- Root `README.md` and `PRD.md`; references checked against exact paths in uploaded ZIP.
- Existing Git log: **11 commits** in the local `.git` history, with recent merges and iterative work evident. Snapshot's Git remote points to `yonti32-ux/AI-Vibe-coding--assignment-01-Project-Black-Thursday`, **different** from the URL initially supplied in the conversation (`yonti32-ux/polsci01-assignment-01-Project-Black-Thursday`). I could not independently confirm either current GitHub access from this sandbox.
- `presentation/index.html`, `app.js`, `slides-data.js`, source registry and claim register; reviewed all 14 storyboarded slide sections and the slide 9/13 integration code.
- Existing opening-slide and film contact-sheet screenshots, together with video metadata and rendering/export notes.
- The 82-second `crisis-animation-v3.mp4`: `H.264`, `1280×720`, `20 fps`, valid file container and 2.65 MB size. That metadata is verified; it is **not** an end-to-end human playback sign-off.
- `python/simulation.py`, `python/app.py` and 8 Python tests; **8/8 passed**.
- Spawned the nested app's real Python server; `GET /`, `GET /api/health`, presentation JS and v3 film returned **HTTP 200**; `POST /api/simulate` returned `historical: false` and **12 periods**. A stressful scenario yielded materially different output compared with the default scenario.
- Attempted Chromium+Playwright navigation; the evaluation environment blocked `http://127.0.0.1:8000/` with **`net::ERR_BLOCKED_BY_ADMINISTRATOR`**. Therefore I **did not verify** onscreen navigation, real playback or a browser-driven slide 13 interaction. The team's successful tests on other computers are useful but not independent observations of this ZIP.
- Official historical input: December 1984 State Comptroller report, including the introduction, warning chronology, and table 1.3, as previously provided in this project; cited source register and University of Haifa requirements.

## Strengths that deserve a high score

1. **Substantive political-science framing.** Responsibility is allocated across banks, investors, government and supervisory institutions rather than falsely blaming one minister. The 1981 institutional warning and regulatory accountability add political analysis rather than just an economic timeline.
2. **Material historical discipline.** The video describes **+8.6% real return for all commercial-bank shares versus −57.5% for nonbank shares** over **January–September 1983**, not fictitious 6 October stock-index levels. The 1984 Comptroller's printed table 1.3 supports this comparison; the primary document must remain correctly cited. The ~$1.06bn bank support inventory is kept distinct from state rescue outlays. The 1993 Comptroller's ~$9.1bn expenditure is described as gross expenditure through October 1991 including financing—not final net taxpayer loss.
3. **Strong aesthetic coherence.** RTL deck, consistent dark/gold financial-investigation identity, restrained 3D/infographic film and visible source chips. Real screenshots exist.
4. **Three integrated technical components.** Browser-based HTML, a code-produced genuinely spatial video, and a Python API which feeds a user-editable chart. This is not merely a Python `.py` file placed in a directory to satisfy a rubric.
5. **Process evidence.** Original prompts, Liron's exact feedback iterations, multiple video versions, PRD changes, QA records and a preserved Git history support the assignment's goal of students directing AI development.

## High-priority defects (must be corrected before final submission)

### CRITICAL — Repository root does not actually contain the canonical runnable app

The uploaded ZIP unpacks to a repository folder with:

```text
assignment 01/
  README.md                    # expects app and launcher in root
  PRD.md                       # expects docs/ and app in root
  Black_Thursday_Final_Review_Candidate/
      START_BLACK_THURSDAY.bat # ACTUAL launcher
      launch_presentation.py
      Project-Black-Thursday-deliverable/
      docs/                    # ACTUAL docs
      prompts/                 # ACTUAL prompts
  early_versions/              # many old copies
```

- The ZIP's **root `README.md` contains 23 broken local Markdown paths** in my file-existence audit, including the screenshot, executable launcher, source files and review report. The ZIP's **root `PRD.md` has six broken local Markdown links**.
- There is **no `START_BLACK_THURSDAY.bat` at the ZIP repo root** despite the root README saying to double-click it there.
- `Black_Thursday_Final_Review_Candidate/` itself does **not** include an `README.md` or `PRD.md` copy: they are one level higher; moving *only* the candidate without its documents would create a different incomplete package.
- A repository evaluator may follow the wrong instructions, incorrectly conclude the project cannot be run or stop after encountering broken images. This is a **material grade risk** even if the application works on your own PC.

**Required fix:** In the existing Git clone (never overwrite `.git`), move the contents of `Black_Thursday_Final_Review_Candidate/` into the **repository root** alongside existing root `README.md` and `PRD.md`, retaining those root documents and updating any conflicting files. Final root should directly contain `START_BLACK_THURSDAY.bat`, `launch_presentation.py`, `Project-Black-Thursday-deliverable/`, `docs/`, `prompts/`, `README.md` and `PRD.md`. Validate every README link after committing. Make a backup and use `git mv` where feasible so Git records changes cleanly. Delete redundant runnable copies *only after* verifying the approved version is safely staged and committed; Git history already preserves prior builds.

### HIGH — Repository URL / access inconsistency

The local Git `origin` in this ZIP is:

`https://github.com/yonti32-ux/AI-Vibe-coding--assignment-01-Project-Black-Thursday`

Earlier conversation supplies:

`https://github.com/yonti32-ux/polsci01-assignment-01-Project-Black-Thursday`

**Required fix:** Determine which is the actual submission repository. Verify the URL in a private/logged-out browser or accepted lecturer invite, then update your README, Moodle form and local remote. This review **did not** verify current remote accessibility.

### HIGH — Several historical/source checks still require final approval

The live `research/claim-register.csv` contains **17 entries** including **2 flagged `analysis_team_review`**, **1 `needs_page_verification`**, and **1 `checked_secondary_primary_review_pending`**. Close material open review statuses or explicitly mark claims as interpretations and support them in presenter notes. Distinguish the official 1984 primary report from the separate 1993 accounting report. Confirm visual source rights. The bank-share transaction halt's **calendar versus trading-day duration** deserves precise labeling when an exact number is displayed.

### HIGH — Full browser walkthrough and lecturer access not evidenced

Although backend and static assets work by direct HTTP, the actual GUI (14 slide navigation, video play/pause, simulation interaction, responsive display and Hebrew text) was **not tested successfully inside this assessment environment**. The team should document a real Chrome or Edge walkthrough with screenshots and a short QA checklist. Uploading a ZIP here does not automatically mean the lecturer has repository access.

### MEDIUM — Historical version duplication and working-tree cleanliness

The ZIP includes about **155 files / 21 MB** in `early_versions/`, plus an additional **95 files / 13.5 MB** in the current candidate. Previous video variants exist as genuine development evidence but do not all need to stay in the live runnable tree. `.git` is included in the uploaded ZIP and several files are modified/deleted compared with its recorded HEAD. Check `git status`, preserve the commit record, commit intentional changes, remove editor lock/temp files and do not use a downloaded ZIP as a replacement for your actual Git clone.

### MEDIUM — Historical and technical disclosure

The original PRD mentioned Three.js, while the final product uses original raw WebGL/Python code-rendered 3D and infographic layers. The later PRD documents this change appropriately. Keep this transparent to the instructor and do not call the produced video a full Three.js build.

## Recommended final steps, in order

1. **Fix the root immediately** (consolidate the single approved build; align root links and launcher). This will also help Gemini or any automated reviewer find the right files.
2. Validate `git status`, confirm actual remote, push a meaningful cleanup commit, and verify external read access.
3. From a fresh clone, double-click the *root* `.bat` on Windows; navigate all slides, play all 82 seconds of the video, interact with slide 13, and capture evidence.
4. Close pending material source citations and student review flags; update the QA report with actual results.
5. Preserve this review unedited under `docs/reviews/chatgpt-independent-assessment-2026-11-02.md`. Add a separate response file detailing each resolved issue and its commit.
6. Confirm the eight-character code `polsci01` and exercise number (`ex01` **if** Moodle specifies 01). Complete only the official Word template fields, save as `polsci01-ex01.pdf`, and **each team member submits their own copy**. Do not upload students' IDs or individual submission forms to the public GitHub repository.

## Self-grade recommendation

**Do not enter 100** solely because the presentation looks finished. The course instructions warn that this invokes maximal scrutiny, and several easily checked repository issues remain.

- **If you submitted this exact ZIP/repository structure now:** My independent estimate is **81/100**, with a real risk of a lower evaluation if reviewers cannot locate the runnable artefacts from the root.
- **After root consolidation, verified GitHub access, completed GUI walkthrough and closed factual checks:** I would consider a **team self-recommendation around 90–92/100** defensible. Reassess once you have real sign-off evidence.

Your recommended numeric grade belongs in the **designated field of the lecturer's official reporting template** (if provided), converted to PDF and uploaded privately to Moodle by *each student*. The team can also record the rationale in `docs/SELF_ASSESSMENT.md`; the GitHub file is supporting evidence, **not** the official form. The exact location of the grade box cannot be confirmed without examining the actual template.

---

**Assessment limitations:** Manual review of the project code, provided screenshots and representative source text; direct Python/backend checks; video metadata verification. Not an independent real-Windows or full-browser playback certification. Not a guarantee of institution score and not a direct check of current live GitHub visibility. This assessment is intentionally skeptical, as requested for the red-team learning process.
