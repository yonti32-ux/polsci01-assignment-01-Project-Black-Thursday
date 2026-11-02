# Film v2 — export method and provenance

- **File:** `media/video/crisis-animation-v2.mp4` (actual 72 seconds at 1280×720; no audio; Hebrew captions in video)
- **Source:** existing genuine 3D filmed geometry at `media/video/crisis-animation.mp4`, preserved unchanged.
- **3D origin:** original `render_movie.py` CPU 3D renderer; original WebGL scene remains `scene.js`. Film v2 is a re-edited version **rather than an independently re-rendered Three.js film**.
- **New materials:** timestamped Hebrew info cards, seven labeled stages, TASE halt scene, measured Jan–Sep 1983 comparison (all commercial-bank shares **+8.6%** vs nonbank shares **−57.5%** real returns, **not a bank index or daily price curve**), correct future-obligation captions, branded color palette supplied by Liron.
- **Authoritative factual source:** Comptroller (1984), *דו"ח על מניות הבנקים — משבר אוקטובר 1983*, particularly printed p. 19 table 1.3, pp. 7–13 for mechanism, share-support inventory, closure, rescue and regulatory warnings. See application bibliography `S10`.
- **Reproduction:** Install Pillow and FFmpeg **only for editing**. Run `python animation/render_movie_v2.py` from application root; script generates temporary `animation/generated-v2-overlays` images and 7 clip segments, and assembles MP4 and poster. To only **play** the finished MP4 no export dependencies or internet are needed.
- **Captions:** Embedded visibly in frames; additional timed VTT can be added in future if users need language-switch/assistive tech.
- **Original preserved:** `crisis-animation.mp4`, `render_movie.py`, `scene.js` to maintain auditability and offer rollback.
- **Known limitations:** Original background camera shots and geometry are inherited, so film v2 improves clarity/editorial sequencing but is **not** an entirely redesigned 3D film. Audio intentionally absent. The 14-versus-18-day reporting discrepancy is avoided by not showing an exact closure-duration count within the movie.
