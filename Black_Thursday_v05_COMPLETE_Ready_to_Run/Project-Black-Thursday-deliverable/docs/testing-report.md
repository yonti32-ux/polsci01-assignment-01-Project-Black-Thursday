# Testing report — 1 November 2026

**Legend:** PASS = actually tested in this environment; PARTIAL = core checked, a major required part not; BLOCKED = unavailable testing environment, not implied to pass; PENDING = human/student action.

| ID | Method / observed result | Status |
|---|---|---|
| A-01 | `python python/app.py` started local API on 127.0.0.1:8000; `curl GET /api/health` returned `{"status":"ok","model_version":"1.0"}`. Browser network navigation to this origin blocked by sandbox policy. | PARTIAL |
| A-02 | Playwright injected actual HTML/CSS/JS, traversed slide indexes 1–14, headings matched and counters read `01 / 14` through `14 / 14`. | PASS |
| A-03 | Navigation code inspected; drawer open/close and ArrowLeft from slide 13 went to slide 14 in Playwright. Button/hashes still to be tested in live origin browser. | PARTIAL |
| A-04 | Screenshots inspected at 1366×768; fonts rendered, visible English dates/citations. More mixed-language spot checks on user PC recommended. | PARTIAL |
| A-05 | All 14 slides produced nonempty original layouts and explanatory text; screenshots saved. | PASS |
| A-06 | WebGL source includes true mesh, normal lighting, view/perspective; headless Chromium returned no WebGL. Equivalent real CPU mesh renderer generated movie. | PARTIAL |
| A-07 | **PASS:** FFprobe confirmed 72.000s H.264 MP4, 1280×720, 20fps/yuv420p. FFmpeg decoded an actual 39s frame. Playwright loaded the actual MP4 as a data URI into the real `<video>`, confirmed `readyState=4`, `videoWidth=1280`, `duration=72`, and `play()` advanced time while `paused=false`. Screenshot `player-real-frame.png`. Native-origin route in browser still to test on user PC. | PASS for media, origin-specific UI PENDING |
| A-08 | Python simulation unit tests and API service pass; browser front-end chart rendered when fed exact Python-produced JSON. Direct browser HTTP to Python blocked by sandbox; verify normally on a user PC. | PARTIAL |
| A-09 | Repeatability and sell-pressure sanity assertions passed. | PASS |
| A-10 | 0/100 input bounds and invalid strings/out-of-range raise handled errors, tests pass. | PASS |
| A-11 | Nonnegative decreasing finite budgets; depletion tests pass. | PASS |
| A-12 | Simulation disclaimer present in permanent slide-13 footer; axes use simulated 1–12 periods. | PASS |
| A-13 | S02 6 Oct and 18 days; S05 445% in 1984 and stabilization in 1985; cited. | PASS |
| A-14 | S01 9.1bn explicitly qualified as cumulative spending including financing and **not ultimate net loss**. | PASS |
| A-15 | Aridor correctly named finance minister; resignation linked to dollarization not crisis alone. | PASS |
| A-16 | 16 Apr 1986 supported by secondary chronology; inquiry/judicial distinction stated; primary report close-reading pending. | PARTIAL |
| A-17 | Bibliography contains real public URLs; S01/S02/S05/S07/S08 inspected, S03/S04/S06 full details pending. | PARTIAL |
| A-18 | Buttons semantic, navigation accessible, reduced-motion CSS. Full accessibility audit pending. | PARTIAL |
| A-19 | Playwright traversed all 14 at **1366×768 and 1920×1080** with zero slide scroll overflow, no page JS errors. Mobile horizontal overflow corrected and retested at 390px (`0`). | PASS for tested dimensions |
| A-20 | No page errors in Playwright HTML injection traversal. Full video playback console audit in live origin blocked. | PARTIAL |
| A-21 | README contains actual install/run commands, screenshots, architectural and research description; film frame verification pending encode. | PARTIAL |
| A-22 | Master prompt really copied and tests logged; original PRD and Git commit history inaccessible because repo could not be cloned. | BLOCKED |
| A-23 | All figures original and rights credits written; no source PDF/news images included. | PASS |
| A-24 | GitHub access and both students' Moodle submissions not attempted. | PENDING |

## Test execution evidence

```text
python -m unittest discover -s python/tests -v
Ran 8 tests ... OK
```

Live source inspection: the 1993 State Comptroller preface explicitly distinguishes $9.1bn expenditure and net loss. Yale case abstract gives 6 Oct/18 days. Bank of Israel page identifies 1984/1985. 1983 Washington Post dispatch dates Aridor resignation. The Supreme Court opening recounts escalating selling and the market closure.

## Important blocked tests

The sandbox's Chromium browser refused direct navigation to localhost and test domains with `ERR_BLOCKED_BY_ADMINISTRATOR`. It also reported WebGL unavailable. We therefore used browser script injection for actual layout screenshots and local API/unit tests, **not a fake assertion of running the whole browser demo against the real local server**.

## Skeptical review checklist for a second AI/human

Check market-history claims against page-level S03/S04/S06, verify Bejski procedural distinctions, test money-vs-share ownership phrasing, review Hebrew BiDi/keyboard accessibility in a local browser, verify that the MP4 decodes and subtitles are readable, and compare model outputs at multiple input extremes. Assign severity and file/slide citations. Independent second-model review has **not** been performed.

## Verified video playback after export

FFprobe: `codec_name=h264`, `width=1280`, `height=720`, `r_frame_rate=20/1`, `pix_fmt=yuv420p`, `duration=72.000000`, `size=1526708` bytes. Playwright `video.play()` started and advanced in a real Chromium HTML5 player. This was tested via a data-URI MP4 because the sandbox blocks browser navigation to localhost; test the file on `http://127.0.0.1:8000/` on a normal computer too.
