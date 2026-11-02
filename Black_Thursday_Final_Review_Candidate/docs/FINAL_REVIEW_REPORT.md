# Final-Pass Audit — Black Thursday (Release Candidate)

**Audit date:** 2 November 2026  
**Assessed material:** student's uploaded `assignment 01 (2).zip`, extracted as a Git working tree; canonical build chosen from `Black_Thursday_v05_COMPLETE_Ready_to_Run/`.  
**Team code:** `polsci01` · **Decision:** **Approve for external Gemini red-team review, NOT yet certify as submitted/final without student device tests and GitHub checks.**

## 1. Key findings

### Repository organization (high impact, now addressed in the candidate)

The uploaded repository contained:
- A root `Project-Black-Thursday-deliverable/` **older runnable prototype**.
- A `Black_Thursday_v04_Selective_Update/` **non-standalone patch**.
- A `Black_Thursday_v05_COMPLETE_Ready_to_Run/` **full later working version**, including the approved 82-second v3 film and current launcher.
- Several competing READMEs, PRDs, research identifiers and earlier PDF/phase drafts.

This created a genuine risk of reviewers running the **wrong version**. Our **clean release candidate** preserves the active v0.5 implementation **once**, removes redundant root-level runnable duplicates, stores original requirements/storyboard/older QA under `docs/history/`, and unifies real prompt records under `prompts/`. The app's self-contained source tree is retained unchanged to avoid disrupting a working prototype. Previous Git commits remain in **the student's original Git repository**, not inside the packaged clean candidate (which deliberately excludes `.git`).

### A Git-specific warning (must address before merge)

The student ZIP contained **7 commits** and **5 modified uncommitted paths** (mostly within prompt/phase3 files and v0.5 launcher). Do **not** blindly delete or reset them; back up or commit valid work before importing the clean candidate. The ZIP's `.git/config` remote was:

`https://github.com/yonti32-ux/AI-Vibe-coding--assignment-01-Project-Black-Thursday`

An earlier conversation referred to:

`https://github.com/yonti32-ux/polsci01-assignment-01-Project-Black-Thursday`

**Mismatch is unresolved.** We could not connect to GitHub from the review container; check `git remote -v` and verify which URL is actually shared with the lecturer. Do not change URLs on assumption.

## 2. Technical tests on the supplied v0.5 code

| Check | Observed | Status |
|---|---|---|
| `python -m unittest discover -s python/tests -v` | All eight tests passed, 2 Nov | **PASS** |
| JavaScript syntax check (`node --check`) | All presentation JS + `animation/scene.js` parsed | **PASS** |
| `GET /` with current local Python service | HTTP **200** | **PASS** |
| `GET /api/health` | HTTP **200** | **PASS** |
| `GET /media/video/crisis-animation-v3.mp4` | HTTP **200**, `video/mp4` | **PASS** |
| `GET /presentation/app.js` | HTTP **200** | **PASS** |
| FFprobe v3 film | H.264, **1280×720**, **20 fps**, **82.0s** | **PASS** |
| End-to-end Chrome/Edge navigation and Python button click | Attempted local Playwright navigation; `ERR_BLOCKED_BY_ADMINISTRATOR` | **NOT VERIFIED** |
| Windows double-click BAT and actual user flow | Not executable in Linux review runtime | **STUDENT MUST VERIFY** |
| Lecturer's account can access GitHub | No network visibility/access to GitHub | **STUDENT MUST VERIFY** |
| Independent Gemini grading feedback | Not yet received | **PENDING** |

**Testing integrity:** A server passing its endpoints is **not** a substitute for clicking slide 13 in Chrome or watching the film. We make no claim that the full browser workflow has been independently verified.

## 3. Historical and narrative review

### Confirmed high-value evidence

The December **1984** State Comptroller report, supplied by students, documents:
- Multiple banks' share-price support practices and the financial strain on **6 October 1983** (printed pp. 7–10).
- A historic comparison of **January–September 1983 real returns**: **+8.6% all commercial-bank shares** versus **−57.5% nonbank shares** (printed p. 19, Table 1.3). This is a period return comparison, **not** daily trading, not an October 6 crash percentage.
- Institutional warnings in **1981** and criticism of authorities' failure to act before the crisis (printed pp. 11–13).
- Estimated future obligations under the contemporaneous 1983 arrangement; **not** the same as the later 1993 retrospective's cumulative expenditure, or final net taxpayer loss.

These data are used in the v3 documentary and referenced in the live slide registry as **S10**. We retained the PRD rules about avoiding an unsourced daily banking index and ensuring cost definitions appear beside any historical number.

### Outstanding editorial checks

1. `Project-Black-Thursday-deliverable/research/claim-register.csv` includes rows with `needs_page_verification` or `analysis_team_review`. Those statuses must not be called fully verified until reviewed by Yonatan and Liron.
2. The **24/25 October reopening** and **14 trading days / 18 elapsed days** terminology should be reconciled from primary sources or described without a misleading exact phrasing; the current deck uses '18 days' based on Yale.
3. The difference between **1983 rescue** and **1985 stabilization** must remain clear.
4. Legal commission findings, judicial findings and individual responsibility must not be conflated.
5. Asset redistribution permissions are not independently certified; original graphics are preferred.
6. There is a previous **source ID mismatch** between the original Phase 3 research and the current slide registry. We set the *live* registry as canonical and labeled the earlier documents as historical drafts, with crosswalk preserved.

## 4. Team's approved creative result and remaining film test

The v3 documentary reflects Liron's requests: 7 stages, centered Hebrew captions, abstract professional motion, exact nine-color palette, beige text, blue positive/red negative returns, proportionate historical values, and more political/institutional framing. The encoded MP4 and actual screenshots exist. We did not alter the film or its production code in this final documentation pass.

Before declaring final, **watch the entire 82 seconds in Chrome and/or Edge**, ensure there are no unexpected glyphs or clipping in transitions, check legibility at 1366×768 and 1920×1080, and record both partners' editorial approval.

## 5. Gemini assessment vs university recommended self-grade

**Two separate artifacts:**

1. **Gemini independent red-team evaluation:** Use [`../prompts/06-gemini-independent-review-prompt.md`](../prompts/06-gemini-independent-review-prompt.md), supply complete repository ZIP and course instructions, save Gemini's **real output** in [`reviews/`](reviews/). Its proposed grade is external feedback, **not official**. Address any serious defects and log the actual action.
2. **Team recommended self-grade (ציון עצמי מומלץ):** The team's chosen number and rationale should be recorded in [`SELF_ASSESSMENT.md`](SELF_ASSESSMENT.md) after reviewing evidence, and **entered into the corresponding field of the lecturer's official Word reporting template** before exporting the final PDF. The template was not supplied here; do **not** add new text areas, pages, or free text if no such field exists. Check the template/Moodle instructions if uncertain.

**Individual submission:** Each student fills their own official university form and uploads a PDF named **`polsci01-ex01.pdf` if Moodle confirms exercise number 01**, never a Word file. Keep student ID information out of public GitHub.

## 6. Final release decision

**Documentation/code candidate:** **APPROVED FOR EXTERNAL REVIEW.**  
**Actual assignment submission:** **CONDITIONAL / HOLD** pending: (a) full student-device/browser/video/Python test, (b) accurate GitHub remote and lecturer access, (c) partner academic sign-off, (d) Gemini critique addressed, and (e) correct individual Moodle PDF form.

This distinction protects the grade: the university treats missing access and incorrect submission format as serious failures regardless of aesthetic quality.

### Final packaging smoke test — clean ZIP (2 November 2026)

After creating `Black_Thursday_Final_Review_Candidate.zip`, we extracted it into a **fresh temporary directory**, without relying on the original uploaded repository or its working paths. From the extracted canonical app:

- Eight Python tests passed (`unittest`, clean copy).
- `GET /` returned **HTTP 200** with HTML content type.
- `GET /api/health` returned **HTTP 200** with JSON content type.
- `GET /media/video/crisis-animation-v3.mp4` returned **HTTP 200** with `video/mp4`.
- `POST /api/simulate` with default parameters produced `historical: false` and **12 periods**.
- README and PRD relative Markdown links were checked for file existence in the clean folder.

This **validates packaging and backend/API behavior**, not the still-pending human Windows GUI and full browser walkthrough.
