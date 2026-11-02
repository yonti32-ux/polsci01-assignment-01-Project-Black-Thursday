# Three-dimensional film — source, rendering and reproducibility

## What is real

`scene.html` and `scene.js` contain a real WebGL object-based 3D scene: mesh vertex positions (X, Y, Z), normals, perspective and view/model matrices, depth testing, directional lighting and camera movement. The 72-second seven-shot timeline is driven by actual time. A separate 2D canvas provides Hebrew caption compositing for the video export. This is **real 3D**, not a CSS perspective animation or static-image video.

The included local MP4 is rendered from equivalent original 3D mesh primitives with `render_movie.py` using a **CPU 3D software renderer** (perspective projection, surface normals, lights, depth sorting) in an environment where headless Chromium had no WebGL. This is a separate recording pipeline from the browser WebGL preview. Do not falsely claim the MP4 was captured by Three.js or that the WebGL preview rendered successfully in this environment. The seven scenes and editorial sequence match.

## Files

- `animation/scene.html`, `animation/scene.js`: inspectable real WebGL scene with timeline and browser MediaRecorder button.
- `animation/render_movie.py`: offline CPU-based 3D video export (NumPy, OpenCV, Pillow and FFmpeg needed to re-render, **not** to play).
- `media/video/crisis-animation.mp4`: embedded H.264 video with Hebrew captions rendered into frames; the video tag supplies native play, pause and scrub controls.
- `media/images/video-poster.png`: poster frame derived from the actual renderer, not an AI-generated archival image.

## How to regenerate

From project root, with FFmpeg installed and `numpy`, `opencv-python`, `Pillow` available:

```bash
python animation/render_movie.py --fps 20 --duration 72
```

The file is exported in MP4 with H.264, 1280×720, 20 FPS, `yuv420p`, faststart. No external assets, copyrighted news images or services are required. Sound intentionally absent: Hebrew captions make it self-contained.

To preview the browser WebGL scene, run the local server, open `/animation/scene.html` and enable WebGL in your browser. The exported MP4 does not require WebGL. Browser MediaRecorder recording can export a separate WebM when supported. The browser preview is not the file embedded in slide 09.

The film is **a schematic illustration**. Its city, bars, coins, dates and flow are symbolic; none are historical trading values, actual buildings or archival recordings.
