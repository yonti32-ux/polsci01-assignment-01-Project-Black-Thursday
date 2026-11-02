# Film v3 — Rendered 3D Documentary / Export & Research Provenance

**Version:** v0.5 candidate · **Date:** 2 November 2026  
**Film:** `media/video/crisis-animation-v3.mp4` · **82 seconds** · **1280×720** · **20 fps** · H.264/yuv420p · Silent with Hebrew text burned into frames.

## What's new since v2 (Liron's refinement)

The film now uses an entirely rebuilt, consistent editorial composition: two stable panels for the illustration and historical explanation; text that is centered **inside** its assigned cards; restrained abstract motion; subtle original 3D building geometry; a seven-part narrative; fixed source footer, sensible color semantics, clearer financial terms and non-overlapping captions. The obsolete v2 overlay text has **not** been retained in the imagery.

**Exact requested palette** (no other named design colors):
`#1c242c` `#c19d43` `#d3cebe` `#1f3c58` `#8ab9ee` `#7a8694` `#e7eef4` `#f5cb39` `#ed1c16`.

**Usage rules:** beige (`#d3cebe`) for main text; blue (`#8ab9ee`) for positive percentage; red (`#ed1c16`) for negative percentage and crisis warnings; gold (`#c19d43`) for institutional framing; yellow (`#f5cb39`) for important dates, and navy for the government/market backdrop.

## Film structure

| Video range | Section | Graphic/point |
|---|---|---|
| 00–11 s | שוק שנראה יציב | Abstract low-poly 3D bank silhouettes and historical share-price support |
| 11–23 s | כך עבד הוויסות | Simplified institutional flow: investors selling → linked purchases → supported prices |
| 23–37 s | מגמות מנוגדות | **Accurate diverging horizontal bars**: +8.6% versus −57.5% (identical zero baseline and scale) |
| 37–49 s | יכולת התמיכה נשחקה | Schematic growing share inventory plus the documented **~US$1.06 billion** historical point |
| 49–60 s | נקודת השבר | **6 October 1983**, suspension of trading in Tel Aviv; not physical destruction of the exchange |
| 60–72 s | המדינה מתערבת | State arrangement, future eligible redemption dates (1985 / 1987 / 1988 / 1989) |
| 72–82 s | שאלת האחריות | Official **1981** warnings versus the **1983** crisis; raises political accountability question |

## Quantitative authenticity

**Source:** State Comptroller of Israel (December 1984), *דו"ח על מניות הבנקים — משבר אוקטובר 1983*.

- **Table 1.3, printed p. 19, PDF page 16:** January–September 1983 **real returns**: **all commercial-bank shares +8.6%** and **nonbank shares −57.5%**. These figures are returns over *nine months*, **not** an invented “Bank Index” value or the percentage decline on 6 October.
- **Printed pp. 7 and 10, PDF pp. 5 and 8:** share-support inventory reached approximately **US$1.06 billion** on 6 October 1983. This is the value of accumulated supported shares, **not** the cost of the eventual government arrangement.
- **Printed pp. 7, 11, PDF pp. 5, 9:** the October 1983 arrangement involved redemption commitments in **two, four, five and six years**, not full immediate payment in October 1983.
- **Printed pp. 11–13, PDF pp. 9–11:** official criticism of the regulators and a joint 1981 warning (`מסמך הארבעה`). The final scene is an interpretive political-science question, not a fabricated criminal verdict.

**Bar-chart audit:** a single shared linear map `x(v) = left + ((v + 60)/80) × (right-left)` for the complete −60%…+20% scale; bank bar width equals `8.6 / 80` of plot width, nonbank bar equals `57.5 / 80` of plot width. Both values are explicitly labeled. The bar entrance animation becomes fully extended quickly and **never pretends to be a time-series trajectory**.

**Caution:** Years marked on the redemption timeline are the nominal original agreement schedule; not real disbursement amounts. The curve/blocks appearing elsewhere are *schematic*, not historical prices. No “14 vs 18 day” closure-duration claim is made in this video.

## What is genuinely 3D?

`animation/render_movie.py` contains an inspectable CPU 3D renderer with X/Y/Z mesh vertices, camera perspective, scene movement and lighting. The updated `render_movie_v3.py` **re-renders the original 3D scene objects without their former captions** to create a lightly visible depth background. The new charts, cards and titles are code-generated 2D editorial overlays. The live raw WebGL scene (`scene.js`) remains separate. This is **not** a claim that the film was rendered using Three.js or that it is archival footage.

## Regenerating the movie (optional; not needed to play it)

Python 3.11+, `numpy`, `opencv-python`, `Pillow`, and FFmpeg on PATH required *for regeneration only*:

```bash
python -m pip install -r animation/requirements-render.txt
python animation/export_v3.py
```

The exporter renders genuine 3D background plus animated infographic frames in short chunks, and encodes the complete MP4 via FFmpeg. It also writes the real image poster `media/images/video-poster-v3.png`. It cleans temporary frames afterward. For quick single-frame QA:

```bash
python animation/render_movie_v3.py --sample 30 --out video-qa-frame.png
```

**Playback needs no video-renderer dependencies:** the finished MP4 is already committed into the presentation's `media/video/` directory and loaded by slide 9's native browser `<video>` element. Previous v1/v2 movies are preserved for comparison and rollback.

## Editorial acceptance: pending vs completed

Completed from local export: full video successfully encoded; geometry source preserved; genuine video screenshots captured; seven sections, source facts and color values checked in rendering code; Hebrew fonts in the encoded frames visually inspected. Pending student sign-off: viewing with normal Chrome/Edge on student Windows computer; overall pacing and intellectual clarity reviewed by Liron; final bibliography/claim-register review; optional subtitles for screen-reader users.
