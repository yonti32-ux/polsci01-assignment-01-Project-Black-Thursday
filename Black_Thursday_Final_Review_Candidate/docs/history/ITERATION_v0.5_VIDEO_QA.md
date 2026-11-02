# Iteration v0.5 — Film improvement and documentation (2 Nov 2026)

## Scope: prioritized Liron's slide 9 feedback

Completed **in this candidate archive**, not yet committed to GitHub:

- Rendered a new **82-second / 1280x720 / 20-fps** v3 video from caption-free original 3D scene geometry, with newly drawn animated financial diagrams and consistent, centered narration cards.
- Followed requested nine-color palette: #1c242c, #c19d43, #d3cebe, #1f3c58, #8ab9ee, #7a8694, #e7eef4, #f5cb39, #ed1c16.
- Adopted **beige** for narrative text, **blue positive**, **red negative**, gold for structured institutional visuals.
- Added a correctly scaled diverging return chart of **+8.6% / −57.5%** with explicit January–September 1983 scope; no invented daily bank index or October 6 percentage.
- Improved political-science analysis: role of regulators, government rescue commitments, early warnings (1981).
- Updated the video source and poster links in `presentation/slides-data.js`, preserved v1 and v2 for auditability.
- Updated root README, delivered app README, PRD change log, original prompt history, export method and accessible transcript.
- Captured real output frames as screenshots for README.

## Self-assessment against Liron's prompt

| Request | Implementation evidence | Result |
|---|---|---|
| Keep existing film structure | Seven stages (00–11, 11–23, 23–37, 37–49, 49–60, 60–72, 72–82) | PASS |
| Text in assigned bubbles, centered | Deterministic rounded cards and center-anchored Hebrew text in animation code; 7 representative PNG checks | PASS in captured stills |
| More abstract, smooth professional graphics | Subtle object-based 3D background, animated flows/cards/bar growth, consistent two-column composition | PASS, subjective final approval pending |
| Professional and politically relevant | Regulators/1981 warnings, government commitments, public-accountability question | PASS |
| Exact colors | All named design colors match specified 9-element palette; alpha blending only | PASS |
| Numerical accuracy | Returns mapped to **same -60..+20% x-axis**, correct endpoints; inventory amount explicitly distinguished from rescue costs | PASS at completed chart frames |
| No anomalous/text overlap | Earlier v2 captions are no longer present; no unsupported glyph boxes in film frames | PASS in inspected stills; full visual playback still pending |
| Run without manual steps | Existing one-click BAT/stdlib server mechanism remains unchanged | Script presence verified; Windows GUI testing pending |
| Professional documentation | PRD, README, export, transcript, log, QA and authentic prompts updated | PASS in candidate archive |

## Technical checks performed

- FFprobe verified H.264, **1280×720**, **20 fps**, **82.0 seconds**, limited-range yuv420p, audio intentionally absent.
- Video decoded successfully for actual screenshot captures at 30s, 54s and 77s; screenshot files are genuine frames from the MP4.
- Video has self-contained Hebrew text and does not require sound to follow the explanation.
- Original 3D source and previous films retained; slide 9 references `crisis-animation-v3.mp4` and `video-poster-v3.png`.
- Existing Python test suite and local API should be rerun against this candidate before merge; state results below after run.

## Historical evidence audit — specific primary source

State Comptroller, **December 1984**, *דו"ח על מניות הבנקים — משבר אוקטובר 1983* (provided by students):
- printed p.19 / PDF page 16, Table 1.3: **+8.6% all bank shares; −57.5% nonbank shares**, **real returns Jan–Sep 1983**;
- printed p.7 / PDF page 5: bank-support inventory **US$1.06 billion** on **6 October 1983** and market trading closure;
- printed pp.7,11: future redemption terms and state commitments;
- printed pp.11–13: early institutional warnings and regulatory critique.

**Do not label** these as single-day price-index falls or a stock-market building collapse. **Do not equate** support inventory with bank bailout costs. Keep original report source on GitHub only where redistribution rights allow; a bibliographic link is sufficient.

## Pending real-device acceptance (students)

1. Double-click `START_BLACK_THURSDAY.bat` on a Windows laptop; load all 14 slides and play the v3 film end to end in Chrome/Edge.
2. Check normal playback, scrubbing, full screen and Hebrew legibility from at least two viewing distances.
3. Ask Liron specifically whether pacing, centered cards and clear graph meet her intended meaning of 'no odd'.
4. Verify Python slide 13 still calls the backend, rather than a hardcoded chart.
5. Re-check bibliography source labels and case-sensitive paths after GitHub merge.
6. Record final version's user tests and make meaningful Git commit(s); no GitHub push occurred here.

**Release decision:** Candidate is ready for partner review, **not** certified as the final submission.

### Completed local regression pass (2 November 2026)

- `python -m unittest discover -s Project-Black-Thursday-deliverable/python/tests -v` → **8 / 8 passed**.
- `ffmpeg -v error -i .../crisis-animation-v3.mp4 -f null -` → video decoded without reported errors.
- Verified the Python server `GET /api/health` returned HTTP 200, and the **v3 video asset returned HTTP 200** with `video/mp4` MIME type from the actual local server.
- Checked code contains all nine exact palette swatches and the ratio-preserving `−60…+20` return chart; verified actual MP4 screenshots at 30s, 54s and 77s.
- A Playwright navigation attempt to `http://127.0.0.1:8000/` was blocked by the evaluation browser's administrator policy (`ERR_BLOCKED_BY_ADMINISTRATOR`). **Therefore no full browser playback or slide-13 UI test is claimed.** Such tests must be run on the student's normal Windows computer.

### Actual-film screenshot correction loop

The first decoded v3 return-chart screenshot revealed that the red **−57.5%** label touched/overlapped the negative bar. We corrected the label's fixed vertical alignment, regenerated the 23–37s frames and re-encoded the entire 82s film. The replacement actual MP4 screenshot now shows an unobstructed red value below its bar. This is a documented, concrete example of QA-driven iteration prompted by Liron's readability request.
