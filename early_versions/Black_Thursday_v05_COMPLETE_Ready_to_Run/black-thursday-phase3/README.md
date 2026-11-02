# Black Thursday — Phase 3 Historical Research & Storyboarding

**Date:** 2026-11-01  
**Project:** *Black Thursday — The Political Economy of Israel's 1983 Bank-Share Crisis*  
**Role in course:** Historical evidence and narrative planning before HTML / Three.js / Python implementation.

## Folder contents

- `research/sources.md` — annotated bibliography, supported claims, source caveats and historic-media rights notes.
- `research/historical-timeline.md` — verified causal sequence, dated milestones and institutional actor matrix.
- `research/claim-register.csv` — claim-to-source index with review status for historical assertions in individual slides.
- `content/storyboard.md` — full 14-slide Hebrew on-screen draft, presenter notes, visuals, interactions, evidence and QA checklist.
- `content/film-shotlist.md` — 60–70-second genuinely 3D explanatory film plan with timecodes and accuracy safeguards.
- `docs/prd-integration-notes.md` — corrections and additions to original `PRD.md`, proposed as an auditable v1.1 revision.
- `prompts/00-original-trial-idea.md` — user's actual initial experimental prompt, preserved unpolished.
- `prompts/01-phase3-brief.md` — user's actual Phase 3 request; not a fabricated development log.

## Method

1. The two class summary PDFs and the instructor's latest written requirements define **what must be built** (HTML presentation + embedded 3D video + running Python + GitHub trail).
2. We researched authoritative historical sources including Israel's State Comptroller, the Ministry of Justice, the Bank of Israel, the Supreme Court record, and Yale's Program on Financial Stability.
3. We separated **documented fact**, **our explanatory analysis**, **schematic film depiction**, and **hypothetical simulation**; we recorded pending source questions instead of silently resolving conflicts by guesswork.
4. The slide drafts maintain the 14-slide PRD architecture and make historical citations part of implementation acceptance criteria.

## What the coding assistant must do next

1. Read `../PRD.md` or the GitHub-root PRD, then read this Phase 3 folder completely.
2. Present any conflicts between the PRD and these notes to the team; don't silently change historical claims.
3. Implement presentation incrementally, starting with navigable RTL HTML and bibliography links.
4. Record genuine versions/commits, full prompts and screenshots. No screenshots or video are included yet: **the implementation does not exist at Phase 3**.
5. Build film as actual Three.js geometry, capture a playable file, and integrate a running Python API into slide 13.
6. Validate `claim-register.csv` and `docs/prd-integration-notes.md` before final release.

## Mandatory labels in final work

- `המחשה סכמטית — אינה שחזור של נתוני מסחר`
- `סימולציה לימודית — לא נתוני 1983`
- For outlay figure: `הוצאה מצטברת, לרבות מימון עד אוקטובר 1991; לא הפסד נטו`

**Scope statement:** This is a research-and-storyboard packet. No video, code implementation, historical photo license, or final academic approval is claimed at this phase.
