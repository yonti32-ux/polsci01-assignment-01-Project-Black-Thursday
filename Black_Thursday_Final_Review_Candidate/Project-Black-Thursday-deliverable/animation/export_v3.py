"""Robust cross-platform exporter for the 82-second v3 film.

Splits rasterization into <=10-second jobs to prevent long-running frame-pipe
stalls, then performs one offline FFmpeg encoding pass. All generated frame
images are temporary and excluded from Git. Rendered movie and poster remain.
Run from repository/application root: python animation/export_v3.py
Prerequisites: pip install -r animation/requirements-render.txt ; FFmpeg in PATH.
"""
import subprocess,sys,tempfile,shutil
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
FILM=ROOT/'media/video/crisis-animation-v3.mp4'
FPS=20
DURATION=82

def main():
    ff=shutil.which('ffmpeg')
    if not ff:raise RuntimeError('ffmpeg is required for re-export; playback does not require it')
    with tempfile.TemporaryDirectory(prefix='black-thursday-v3-') as d:
        frames=Path(d)
        for a in range(0,DURATION,8):
            b=min(DURATION,a+8)
            print(f'[v3] Rendering {a:02d}–{b:02d}s',flush=True)
            cmd=[sys.executable,str(HERE/'render_movie_v3.py'), '--fps',str(FPS),
                 '--start-at',str(a),'--stop-at',str(b),'--frames-dir',str(frames)]
            subprocess.run(cmd,check=True)
        n=len(list(frames.glob('frame_*.jpg')))
        if n!=FPS*DURATION:raise RuntimeError(f'Incomplete export: {n} frames instead of {FPS*DURATION}')
        FILM.parent.mkdir(exist_ok=True,parents=True)
        subprocess.run([ff,'-y','-loglevel','error','-framerate',str(FPS),
                        '-i',str(frames/'frame_%05d.jpg'),'-c:v','libx264',
                        '-preset','veryfast','-crf','18','-vf','scale=in_range=pc:out_range=tv,format=yuv420p','-color_range','tv','-pix_fmt','yuv420p',
                        '-movflags','+faststart',str(FILM)],check=True)
    if not FILM.is_file() or FILM.stat().st_size<100000:
        raise RuntimeError('Export failed')
    print(f'[v3] Completed: {FILM}, {FILM.stat().st_size:,} bytes')

if __name__=='__main__':main()
