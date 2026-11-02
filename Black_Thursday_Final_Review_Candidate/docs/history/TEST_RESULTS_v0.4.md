# Black Thursday — Candidate v0.4 test report

**Date:** 2026-11-02 · **Scope:** uploaded repository snapshot + candidate selective files; no GitHub push/merge performed.

## Executed and passed here

| Check | Result | Evidence |
|---|---|---|
| Python unit/API tests | **PASS: 8/8** | `python -m unittest discover -s python/tests -v` run in deliverable directory; all completed with `OK` |
| JavaScript syntax | **PASS** | `node --check` for modified presentation `app.js` and `slides-data.js` |
| Movie export | **PASS** | v2 created by reproducible `render_movie_v2.py`, original 3D MP4 retained; 7 chapter overlays and transcript provided |
| Movie metadata | **PASS** | `ffprobe`: **H.264, 1280×720, 20fps, 72.000s**, 955,189-byte v2 MP4 |
| Movie frame inspection | **PASS (visual sample)** | Extracted frames at seconds 4, 13, 24, 35, 47, 58 and 69; corrected chart rendering within card |
| Python launcher HTTP (headless) | **PASS** | Launched `launch_presentation.py`; `GET /api/health` 200; `GET /` 200; JS 200; MP4 200; PNG 200; `POST /api/simulate` 200, 12 periods, `historical: false` |
| Source figure labeling | **PASS (spot verification)** | 1984 State Comptroller, printed p.19, Table 1.3: +8.6% all commercial bank shares and −57.5% nonbank shares, Jan–Sep 1983 real returns; no invented daily bank or TASE index |
| Group-code formatting | **PASS** | `polsci01` is 8 characters |

## Not yet verified — must be tested on student computers

1. **Windows .bat double-click** — launcher worked with Python in headless Linux, but Windows shell operation itself has not been directly tested.
2. **Browser in actual local mode** — browser sandbox blocked navigation to `file://` and localhost (`ERR_BLOCKED_BY_ADMINISTRATOR`). Relative paths checked in code, but normal Chrome/Edge viewing still needs human acceptance testing.
3. **End-to-end media playback** — FFmpeg decoding and frame extraction passed, but a browser user must play/pause/seek slide 9 for the entire 72-second film and verify audio is intentionally absent.
4. **Slide 13 UI-to-Python roundtrip** — Python API passed; browser controls clicking, chart update, comparison and reset must be manually tested on a normal browser.
5. **All 14 slides at presentation resolution, keyboard/RTL focus, cited source links** — full regression review pending.
6. **GitHub current HEAD, root README rendering and lecturer sharing access** — not independently verified; supplied ZIP snapshot is not a live repository state.
7. **Historical signoff** — exact 14 vs 18 closure-duration characterization and source-ID crosswalk require human review before final release.

## Windows acceptance walkthrough

From repository root:
1. Double-click `START_BLACK_THURSDAY.bat`. Confirm a console opens and browser opens `http://127.0.0.1:8000/`.
2. Navigate slides 1–14 using buttons and keyboard; inspect sources and speaker notes.
3. On slide 9, play v2 until it ends; verify 7 distinct chapters, data bar chart, correct dates, readable Hebrew captions, replay and seek.
4. On slide 13, change investor confidence, click **הרץ סימולציה**, compare with another scenario, and confirm the server response changes the chart. Confirm warning label `סימולציה לימודית`.
5. Close the console and open `Project-Black-Thursday-deliverable/presentation/index.html` directly; verify the slides and v2 video work and slide 13 displays a clear Python-mode requirement.
6. Check screenshots of changed slides for cropped RTL and the 1366×768 layout. If all pass, add **real** evidence to Git and the root README.

**Verdict:** This is a tested **candidate iteration**, **not a final release certification**.
