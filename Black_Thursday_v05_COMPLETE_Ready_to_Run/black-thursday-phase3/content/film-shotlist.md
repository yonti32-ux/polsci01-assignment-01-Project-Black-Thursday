# Three.js 3D Documentary Shot List v1.0 — Black Thursday

**Target:** 60–70 seconds, 16:9, 1280×720 or higher, H.264 MP4 + source Three.js scene.  
**Historical status:** *symbolic visual explanation*, **not** camera footage, reconstructed economic time series, or testimony.  
**Integrated into:** slide 09 (`<video>` with clear controls and caption track).  
**All characters:** anonymous, nonportrait symbols, not photo-real recreations of named historical persons.

| Timestamp | What viewer sees | Camera / rendering | Hebrew card/narration draft | Evidence / controls |
|---|---|---|---|---|
| 0–8s | Low-poly city with four *generic* bank towers; share tokens flow from investors | Slow orbit, depth-of-field subtle; cinematic nighttime palette | `שנות ה־70 וה־80: מניות הבנקים נעשו השקעה מרכזית` | S01a; S02. Abstract symbols, no fake stock data. |
| 8–20s | Prices stay on a rising rail while bank-linked entities catch shares being sold | Track sideways along two flows; label `ביקוש רגיל` / `רכישה תומכת` | `גופים הקשורים לבנקים רכשו מניות ותמכו בשעריהן` | S01a; S03. Do not show as guaranteed return for each account. |
| 20–30s | Several levers labeled `הנפקות`, `המלצות`, `קרנות קשורות` connect to one support system | Elevated isometric camera; arrows split/merge | `מערך התמריצים יצר גם ניגודי עניינים` | S01a; S02. Conceptual flows, not literal count. |
| 30–42s | Growing red 'sell' tokens; illustrative capacity bar decreases with each supported purchase | Camera dolly toward capacity bar; audio bed rises | `לחץ המכירות עלה. יכולת הבנקים לקלוט את ההיצע הייתה מוגבלת` | S01a; S03; bar units = illustration. |
| 42–52s | Calendar zoom to **6 October 1983**; market gates close; banks remain standing | Slow freeze / cinematic silence on closing gates | `6 באוקטובר 1983 — המסחר בבורסה הופסק` | S01; S03. Absolutely no buildings physically collapsing as if it occurred. |
| 52–64s | State icon appears; signed agreement connects eligible shareholders to a future timeline; bank ownership arrows slowly change direction | Pullback to display years **1983 → 1985/1988/1991** as future points | `המדינה נטלה התחייבויות לפדיון עתידי ולהצלת היציבות` | S01a; S02; future timing explicit. |
| 64–70s | Fade to actor quadrangle and closing question | Camera rise + fade to slide 10 | `מי הרוויח? מי פיקח? ומי נשא במחיר?` | Interpretation / course discussion. |

## Design/accuracy rules

- A noticeable **depth cue** (parallax when camera moves) and at least three lighted 3D objects should make it technically incontrovertible that the film uses 3D geometry.
- Numerical 'stock prices' must be **absent**, or synthetic indices clearly labeled as such. A decreasing capacity bar must be marked `המחשה בלבד`.
- Use generic bank façades, never modern 2026 bank branding presented as authentic 1983 signage.
- In the final film, mark both at beginning and end: `שחזור סכמטי באנימציית תלת־ממד; אינו תיעוד מצולם של אירועי 1983`.
- Final output must be playable **with browser audio disabled**; text captions carry all information. Add Hebrew captions and separate accessible subtitles if possible.
- Export one MP4 and preserve a documented reproducible method to record the original Three.js camera path. Rendering the live interactive scene is an optional extra, not a substitute.

## Suggested visual assets and source controls

- Preferred: code-generated low-poly buildings, embossed but fictional share tokens, original SVG overlays and date typography.
- Optional: genuine archival newspaper photos *only after* permissions / license check and caption verification; preserve provenance in media credits.
- Add stills from film to the README only after the implementation exists; never insert illustrative stock images pretending to be screenshots of our project.

## Playback QA (build phase)

1. In Chrome and Edge, open Flask-served presentation and verify slide 9 video playback, pause, scrub, replay, mute and captions.
2. Check no live internet connection is required for playback (store the video locally and dependencies as allowed).
3. Check media file is not accidentally omitted from Git because of binary-size limits.
4. Verify Hebrew captions/axis labels read right-to-left, and numerals like `1983` retain left-to-right order.
5. Read through entire narration for the historical 'do not confuse' rules in `research/historical-timeline.md`.
