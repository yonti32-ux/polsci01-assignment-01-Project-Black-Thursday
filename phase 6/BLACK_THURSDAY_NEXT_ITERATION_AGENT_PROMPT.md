# AI Coding Agent — Next Iteration Brief (read before touching the project)

You are joining an **existing** GitHub project, not starting a new one.

**Repo:** https://github.com/yonti32-ux/polsci01-assignment-01-Project-Black-Thursday  
**Team:** Yonatan + Liron  
**Group ID:** `polsci01`  
**Goal:** Safely move an existing 14-slide Hebrew-RTL interactive HTML documentary about Israel's 1983 bank-share crisis toward a research-verified, production-ready university assignment. Required components: working HTML presentation, embedded genuine 3D video, functional Python computation, prompt trail, PRD, README with real screenshots, meaningful commits and QA.

## HARD RULES

1. Start with `git status -sb`, `git log --oneline -10`, `git branch -vv`, `git remote -v` (avoid exposing tokens), and list repository contents. **Never** initialize a new repository, overwrite a colleague's changes, force-push, discard uncommitted work, or blindly replace the existing deck.
2. Read `PRD 0.1.md`, both available READMEs, the Phase 3 storyboard and historical sources, the current deliverable under `Project-Black-Thursday-deliverable/`, and `BLACK_THURSDAY_REPO_AUDIT_AND_ROADMAP.md` (if included).
3. The current implementation already has slides, a raw-WebGL source scene, **72s H.264 software-rendered 3D film**, and working Python API. **Do not promise a Three.js build without checking**: Three.js was originally chosen but is **not** the film's current renderer. Decide whether the genuine 3D requirement is satisfied before scope-creeping.
4. Liron is actively improving presentation design. Work in a separate branch, make small changes with clear ownership, and propose a PR/merge instead of replacing her working files. Ask for team approval only when a potentially conflicting change is unavoidable.
5. Preserve real provenance and label model graphics `סימולציה לימודית — לא נתוני 1983`. Do not fabricate newspaper images, historical share-price series, direct quotes, model calibration, screenshots, test results, or Git commits.
6. Primary historical sources: State Comptroller's **December 1984** *דו"ח על מניות הבנקים — משבר אוקטובר 1983* (95-page scan uploaded to team research folder); State Comptroller **1993** audit (https://library.mevaker.gov.il/sites/DigitalLibrary/Pages/Publications/641.aspx); Ministry of Justice retrospective by **Moshe Lador** (https://www.gov.il/BlobFolder/reports/roots_1983/he/roots-1983.pdf); Yale (https://newbagehot.yale.edu/docs/israeli-bank-shares-arrangement-hesder-hamenayot-habankayot). These have distinct financial figures and temporal standpoints. Cite precisely.

## FIRST CHANGESET — documentation and source normalization only

- Update **root README.md** to describe the **implemented** prototype, not a planned one; link real images under `Project-Black-Thursday-deliverable/media/screenshots/` and give correct root-to-app launch commands.
- Record actual `polsci01` group code (exactly 8 characters), but do not invent the course deadline or assume Moodle suffix without checking.
- Reconcile **PRD 0.1.md** versus expected `PRD.md`, keeping original history; note draft PDF in `presentation - phase 5/` is **not** the live HTML deliverable.
- Unify competing `S01`/`S02` reference IDs between Phase 3 and the actual app; do this through a mapping table so links and claims remain correct.
- Add the **1984 Comptroller** and **Ministry of Justice** as two additional historical anchors with printed-page metadata.
- Remove Word lock file `~$lm-shotlist.md` only after reviewing the exact working tree.
- Update development log and prompt history with *this actual instruction*, date, changes and observed behavior.

Stop after the first changeset and report modified files, tests, unresolved issues, and suggested commit; **don't automatically push** unless explicitly authorized.

## SECOND CHANGESET — historical content

Propose narrowly scoped slide modifications with source references before editing:
- **Slide 7/12:** December 1981 `מסמך הארבעה` warning; distinguish banks' practices from regulators' response.
- **Slide 7:** original measured **Jan–Sep 1983 real return** comparison: nonbank shares **−57.5%** versus **all commercial-bank shares +8.6%**, based on 1984 Comptroller Table 1.3, printed pp. 18–19. Avoid calling the second group 'only regulated bank shares'.
- **Slide 6:** approximate **US$1.06bn bank-support share inventory on Oct 6**, if explanation helps, not as amount of fiscal rescue.
- **Slide 10:** arrangement negotiated and signed **by Oct 20, 1983** with future redemptions, not immediate government takeover of day-to-day management.
- **Slide 11:** 1984 prospective **~US$6.9bn** government obligations versus 1993 retrospective **~US$9.1bn** cumulative expenditure (incl. financing through Oct 1991). Don't equate either to final net state loss.
- **Slide 8:** 1984 report's '14 days' versus Yale's '18 days' must be checked for counting conventions; do not silently choose one. 6 October closure is uncontested.
- **Slide 12:** distinguish an audit's institutional criticisms, Bejski Commission findings, prosecutor's retrospective, district-court verdicts and appeals.

Keep all newly inserted Hebrew wording sourced in a machine-readable claim registry and clearly marked as FACT / ANALYSIS / SIMULATION.

## THIRD CHANGESET — live QA and polish

1. Run `python -m unittest discover -s python/tests -v` in `Project-Black-Thursday-deliverable/`, check Python service `GET /api/health`, `POST /api/simulate`, and record results. The snapshot already passed 8/8 tests and direct HTTP checks; retest after changes.
2. In a **normal browser with direct localhost access**, navigate all 14 slides, run slide-13 simulator, compare scenarios, use the videos, review accessible captions, URL hash navigation, source drawers, keyboard behavior, RTL labels, responsive layout and console errors.
3. Update/screenshots from the **actual final running build**; verify that they render on GitHub. Preserve existing high-quality branding rather than gratuitously redesigning.
4. Execute an independent red-team audit and document defect severity, exact file/slide, source, fix and retest evidence.

## STOP/DELIVERY REQUIREMENTS

Return a concise file-by-file diff summary and accurate test status. Preserve colleague work. Identify any unverified claim and don't convert it into a confident assertion. Keep GitHub and individual PDF-submission rules separate from software feature completion.
