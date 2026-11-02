# Release and Submission Checklist — `polsci01`

**Review build:** final documentation candidate, v0.5 app and v3 movie. **Do not tick tests until actually performed.**

## Technical demonstration

- [x] v3 MP4 exists and is H.264, 1280×720, 82 seconds (FFprobe).
- [x] Eight Python unit tests passed in independent Linux review (2 Nov 2026).
- [x] Root local HTTP response, health, video, and JavaScript assets responded HTTP 200.
- [x] JavaScript syntax checks passed with Node.
- [ ] Double-click `START_BLACK_THURSDAY.bat` in **the cleaned actual repository** on a Windows machine.
- [ ] Verify video playback full length with working play/pause/replay, readable Hebrew text, no odd glyphs.
- [ ] Check all 14 slides in Chrome or Edge; navigation and text are correct in Hebrew RTL.
- [ ] On slide 13 change inputs, click **הרץ**, see new Python-backed chart values, compare scenarios/reset.
- [ ] Test the direct HTML mode, ensuring the simulator displays the correct offline explanation.
- [ ] Test at 1366×768 and 1920×1080; record screenshots of actual final app.
- [ ] Any browser console JS errors fixed or documented.

## Historical / visual quality

- [ ] Both students approve every central historical conclusion and remaining `analysis_team_review` / `needs_page_verification` claims.
- [ ] Confirm 1984 report's +8.6% / −57.5% are **Jan–Sep 1983 real returns**; no fabricated daily market figures.
- [ ] Verify share-support inventory vs. future obligations vs. cumulative outlay and net loss are not conflated.
- [ ] Confirm October 1983 rescue vs July 1985 stabilization remain separate.
- [ ] Resolve or avoid exact 24/25 October reopening ambiguity.
- [ ] Both students confirm the v3 film meets Liron's exact palette, movement, textual layout and political storytelling goals.
- [ ] Check copyright/asset credits; don't publish copied archive images without rights.

## Documentation and GitHub

- [x] Root README and PRD present in review candidate; current v3 screenshots/launch steps documented.
- [x] Real primary prompts, original PRD, and phase3 notes retained, clearly marked historical.
- [ ] Resolve Git remote mismatch; verify correct working GitHub URL via `git remote -v` and browser.
- [ ] Merge clean candidate into the **actual existing clone**, not a new reinitialized repository.
- [ ] Resolve current uncommitted changes before deletion or restructuring; backup original ZIP.
- [ ] Verify no redundant v04/v05 *runnable* folder variants remain at repo root.
- [ ] Inspect README pictures and all relative links on GitHub after push.
- [ ] Record a genuine cleanup commit and push; check recent commit is visible publicly/to lecturer.
- [ ] Make repository public OR invite lecturer `rmisegal@gmail.com`, ensure access is accepted and working.
- [ ] Confirm submitted repo URL actually matches current `origin` and available branch.

## Independent AI red-team and assessment

- [ ] Send final clean ZIP plus lecturer requirements to Gemini using `prompts/06-gemini-independent-review-prompt.md`.
- [ ] Save actual Gemini feedback unaltered under `docs/reviews/` (e.g. `gemini-assessment-2026-11-02.md`).
- [ ] Record critical/high issues, what was fixed, what is rejected and why; run regression tests.
- [ ] Agree on a justified **team recommended self-grade**, record it in `docs/SELF_ASSESSMENT.md`.
- [ ] Enter recommended grade **in the official university form's designated field** (if present, per instructions), not as an extra GitHub-only file.

## Moodle / university

- [ ] Confirm group ID `polsci01` (8 characters) and official assignment `ex01` numbering.
- [ ] Each student completes their **own** copy of the designated Word form, changing only prescribed fields.
- [ ] Each saves to PDF **`polsci01-ex01.pdf`** (if this is Exercise 01); do not upload `.docx`.
- [ ] Keep the PDF containing real student IDs **private** and OUT of public GitHub.
- [ ] Both students individually upload their PDF before deadline and verify receipt.
- [ ] If seeking a special extension, use only the university-authorized procedure, never submit sensitive medical files to the lecturer.
