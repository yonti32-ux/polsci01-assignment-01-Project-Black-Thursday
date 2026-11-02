"""Black Thursday v3: source-backed 82-second abstract financial documentary.

Re-renders the existing original 3D object geometry via draw_scene(), WITHOUT
any of its old overlapping caption overlays, then builds smoothly animated
infographic / governmental-oversight graphics. No historical market path is
fabricated. All historical numbers (8.6%, -57.5%, $1.06b) are sourced to the
1984 State Comptroller report and recorded in EXPORT_v3.md.

Recommended full export: python animation/export_v3.py
For one reproducible scene preview: python animation/render_movie_v3.py --sample 30
For chunked frame exports: python animation/render_movie_v3.py --start-at 0 --stop-at 8 --frames-dir /tmp/frames
Dependencies for rendering only: pillow, numpy, opencv-python, ffmpeg.
No extra dependencies needed to play finished video in the presentation.
"""
from pathlib import Path
from functools import lru_cache
import argparse, math, os, subprocess
import numpy as np
import cv2
from render_movie import draw_scene as draw_original_3d_scene
from PIL import Image, ImageDraw, ImageFont

APP = Path(__file__).resolve().parents[1]
ORIGINAL = APP / 'media/video/crisis-animation.mp4'
OUT = APP / 'media/video/crisis-animation-v3.mp4'
POSTER = APP / 'media/images/video-poster-v3.png'
W, H = 1280, 720
DURATION = 82.0
SCENES = [(0,11), (11,23), (23,37), (37,49), (49,60), (60,72), (72,82)]
COLORS = {
    'ink': '#1c242c', 'gold': '#c19d43', 'beige': '#d3cebe',
    'navy': '#1f3c58', 'blue': '#8ab9ee', 'slate': '#7a8694',
    'white': '#e7eef4', 'yellow': '#f5cb39', 'red': '#ed1c16',
}
C = {k: tuple(bytes.fromhex(v.lstrip('#'))) for k, v in COLORS.items()}
HE_FONT = os.environ.get('BT_HE_FONT', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
HE_BOLD = os.environ.get('BT_HE_BOLD', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
LAT_FONT = os.environ.get('BT_LAT_FONT', '/usr/share/fonts/opentype/inter/InterDisplay-Regular.otf')
LAT_BOLD = os.environ.get('BT_LAT_BOLD', '/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf')
# Allow independent Windows users to regenerate, optionally specifying font paths.
if not Path(HE_FONT).exists():
    HE_FONT = str(Path(os.environ.get('WINDIR','C:/Windows')) / 'Fonts' / 'arial.ttf')
if not Path(HE_BOLD).exists():
    HE_BOLD = str(Path(os.environ.get('WINDIR','C:/Windows')) / 'Fonts' / 'arialbd.ttf')
if not Path(LAT_FONT).exists(): LAT_FONT = HE_FONT
if not Path(LAT_BOLD).exists(): LAT_BOLD = HE_BOLD

@lru_cache(maxsize=70)
def font(size, lang='he', bold=False):
    return ImageFont.truetype((HE_BOLD if bold else HE_FONT) if lang=='he' else (LAT_BOLD if bold else LAT_FONT), size)

def clamp(v, lo=0, hi=1): return max(lo,min(hi,v))
def smooth(x):
    x = clamp(x)
    return x*x*(3-2*x)
def intro(p): return smooth(p/.14)
def outward(p): return smooth((1-p)/.08)
def alpha_transition(p): return intro(p)*outward(p)
def col(key, a=255): return C[key]+(int(a),)
def mix(a,b,t): return tuple(round(a[i]*(1-t)+b[i]*t) for i in range(3))

def puttext(d, xy, txt, size=24, color='beige', lang='he', bold=False, anchor='mm', stroke=0):
    # Anchor mm + RAQM ensures Hebrew remains visually centered in its containing card.
    d.text(xy, txt, font=font(size, lang, bold), fill=col(color), anchor=anchor,
           direction='rtl' if lang=='he' else 'ltr', stroke_width=stroke, stroke_fill=col('ink') if stroke else None)

def rounded(d, box, fill='navy', outline='slate', radius=18, ow=1, opacity=245):
    d.rounded_rectangle(box, radius=radius, fill=col(fill,opacity), outline=col(outline,145) if outline else None, width=ow)

def line(d, pts, c='gold', width=2, a=255, joint='curve'):
    d.line(pts, fill=col(c,a), width=width, joint=joint)

def dot(d,x,y,r,color='gold',alpha=255):
    d.ellipse((x-r,y-r,x+r,y+r), fill=col(color,alpha))

def arrow(d, start, end, color='blue', progress=1, alpha=240, direction=1):
    x1,y1=start; x2,y2=end
    end_x=x1+(x2-x1)*progress; end_y=y1+(y2-y1)*progress
    line(d, [(x1,y1),(end_x,end_y)],color,3,alpha)
    if progress>.65:
        a=math.atan2(y2-y1,x2-x1)
        side=9
        p=(end_x,end_y)
        d.polygon([p,(end_x-side*math.cos(a-.5),end_y-side*math.sin(a-.5)),(end_x-side*math.cos(a+.5),end_y-side*math.sin(a+.5))],fill=col(color,alpha))

def base_static():
    """Baseline frame with exact palette, source footer, and clean layout rails."""
    a=Image.new('RGBA',(W,H),col('ink'));d=ImageDraw.Draw(a)
    for y in range(H):
        t=y/H
        rgb=mix(C['ink'], C['navy'], 0.18+0.26*t)
        d.line(((0,y),(W,y)), fill=rgb+(255,),width=1)
    # Vertical guide highlights and quiet architecture grid (all within palette)
    for x in range(0,W,80):
        d.line(((x,140),(x,616)),fill=col('slate',12),width=1)
    for y in range(146,616,78):
        d.line(((48,y),(1232,y)),fill=col('slate',11),width=1)
    d.rectangle((0,0,W,119),fill=col('ink',250))
    d.rectangle((0,630,W,720),fill=col('ink',254))
    d.rectangle((54,31,59,87),fill=col('gold'))
    puttext(d,(78,42),'BLACK THURSDAY    /    1983',18,'gold','en',True,'lm')
    puttext(d,(1214,48),'יום חמישי השחור',30,'beige',bold=True,anchor='rm')
    puttext(d,(1214,88),'משבר מניות הבנקים בישראל  |  כלכלה פוליטית',17,'slate',anchor='rm')
    line(d,[(55,118),(1225,118)],'gold',2,150)
    # subtle panels, background 3D image inserted under these (more prominent on scenic scenes)
    rounded(d,(53,150,782,606),'navy','slate',22,1,232)
    rounded(d,(807,150,1227,606),'ink','gold',22,2,250)
    line(d,[(55,628),(1225,628)],'slate',1,90)
    puttext(d,(62,668),'ILLUSTRATIVE 3D  /  VERIFIED HISTORICAL FIGURES',13,'slate','en',False,'lm')
    puttext(d,(1219,696),'אנימציית הסבר סכמטית • אינה צילום ארכיוני או שחזור מדדי מסחר',15,'beige',anchor='rm')
    return a

BASE=base_static()

# Source note + section panel copy. Every card line is centered inside the card.
COPY=[
 {'num':'01 / 07','title':['שוק שנראה יציב'],
  'body':['במשך שנים תמכו בנקים','בשערי מניותיהם, גם כאשר','הציבור ביקש למכור.'],
  'source':'מבקר המדינה (1984), עמ׳ 7–9'},
 {'num':'02 / 07','title':['כך עבד הוויסות'],
  'body':['גופים הקשורים לבנקים','רכשו מניות כדי לתמוך','בשערים לאורך זמן.'],
  'source':'מבקר המדינה (1984), עמ׳ 8, 22–24'},
 {'num':'03 / 07','title':['מגמות מנוגדות'],
  'body':['תשואה ריאלית מצטברת','בין ינואר לספטמבר 1983.','לא מדד יומי של יום המשבר.'],
  'source':'מבקר המדינה (1984), לוח 1.3, עמ׳ 19'},
 {'num':'04 / 07','title':['יכולת התמיכה נשחקה'],
  'body':['מלאי המניות שנרכשו','לצורכי ויסות הלך וגדל.','המקורות לרכישות נוספות אזלו.'],
  'source':'מבקר המדינה (1984), עמ׳ 7, 10'},
 {'num':'05 / 07','title':['נקודת השבר'],
  'body':['המסחר בבורסה בתל אביב','הופסק בעקבות המשבר.','הבורסה עצמה לא חדלה להתקיים.'],
  'source':'מבקר המדינה (1984), עמ׳ 7, 10'},
 {'num':'06 / 07','title':['המדינה מתערבת'],
  'body':['ההסדר העניק למחזיקים','הזכאים זכות לפדיון עתידי.','לא כל הכסף שולם בשנת 1983.'],
  'source':'מבקר המדינה (1984), עמ׳ 7, 11'},
 {'num':'07 / 07','title':['שאלת האחריות'],
  'body':['האזהרות היו ידועות','עוד לפני קריסת הוויסות.','מי פיקח — ומי נשא בסיכון?'],
  'source':'מבקר המדינה (1984), עמ׳ 11–13'},
]

def scene_panel(d,scene,p):
    k=COPY[scene]
    cx=(807+1227)//2
    puttext(d,(cx,197),k['num'],18,'gold','en',True)
    line(d,[(847,221),(1185,221)],'gold',1,115)
    for i,txt in enumerate(k['title']):
        puttext(d,(cx,280+43*i),txt,32,'beige',bold=True)
    for i,txt in enumerate(k['body']):
        puttext(d,(cx,369+40*i),txt,23,'beige')
    d.rounded_rectangle((829,540,1203,582),radius=11,fill=col('navy',255))
    puttext(d,(cx,563),k['source'],15,'beige')

# In visual data panel use dynamic shapes and fixed, centered label cells.
def label(d,box,txt,color='beige',size=19,border='slate',background='ink',bold=False):
    rounded(d,box,background,border,13,1,240)
    puttext(d,((box[0]+box[2])/2,(box[1]+box[3])/2),txt,size,color,bold=bold)

def arc_3d(d,cx,cy,rx,ry,t,n=100,alpha=100):
    pts=[]
    for i in range(n+1):
        th=2*math.pi*i/n+t
        pts.append((cx+rx*math.cos(th),cy+ry*math.sin(th)))
    line(d,pts,'slate',2,alpha)
    px=cx+rx*math.cos(t*1.4+2);py=cy+ry*math.sin(t*1.4+2)
    dot(d,px,py,5,'gold',200)

def graphic_0(d,t,p):
    # Financial scene with original abstract 3D in background and elegant banks/price support.
    title='הצמיחה שנראתה בטוחה'
    puttext(d,(421,197),title,25,'beige',bold=True)
    progress=smooth((p-.12)/.70)
    arc_3d(d,421,405,285,105,t*.15,alpha=85)
    for i, x in enumerate([175,268,361,454,547,640]):
        height=(70+[0,25,52,34,69,42][i])*progress
        xx=x + 3*math.sin(t*.35+i)
        d.polygon([(xx-27,479),(xx+26,479),(xx+26,479-height),(xx-27,479-height)],fill=col('navy'))
        d.polygon([(xx+26,479),(xx+36,467),(xx+36,467-height),(xx+26,479-height)],fill=col('slate',160))
        d.polygon([(xx-27,479-height),(xx-17,467-height),(xx+36,467-height),(xx+26,479-height)],fill=col('gold',180))
        for j in range(int(height//28)):
            y0=458-j*26
            line(d,[(xx-16,y0),(xx+15,y0)],'blue',2,130)
    label(d,(174,513,666,563),'מחירי מניות נתמכו לאורך זמן','beige',21,'gold')
    puttext(d,(421,589),'המחשה סכמטית — לא מחירי מניות בפועל',14,'slate')

def graphic_1(d,t,p):
    puttext(d,(419,195),'כאשר גובר היצע המכירה',25,'beige',bold=True)
    boxes=[(535,267,718,354),(316,267,499,354),(97,267,280,354)]
    captions=['משקיעים מוכרים','רכישות תומכות','יציבות מדומה']
    for i,(box,name) in enumerate(zip(boxes,captions)):
        label(d,box,name,'beige',20,'gold' if i==1 else 'slate','navy',i==1)
    arrow(d,(522,310),(505,310),'blue',smooth((p-.06)/.22))
    arrow(d,(302,310),(285,310),'gold',smooth((p-.28)/.22))
    # in-flight highlights behind the three stages: not 'stock price' points
    for i in range(3):
        a=(p*2.4+i*.34)%1
        x=691-a*570
        if 180<x<681:
            dot(d,x,390,4,'blue' if i==0 else 'gold',200)
    label(d,(114,429,701,511),'הביקוש שיצרה המערכת השפיע על מחיר המניה','beige',20,'slate','ink')
    puttext(d,(419,558),'החצים מייצגים מנגנון מוסדי — לא עסקאות בודדות',15,'slate')

def graphic_2(d,t,p):
    # True, mathematically proportional bars: x mapping from -60% to +20%; no faked curve.
    puttext(d,(417,193),'תשואה ריאלית · ינואר–ספטמבר 1983',24,'beige',bold=True)
    left,right=113,727
    min_v,max_v=-60.,20.
    v_to_x=lambda v: left+(v-min_v)/(max_v-min_v)*(right-left)
    zero=v_to_x(0)
    # Vertical grid: every 20 pct points with correctly proportional spacing
    for v in [-60,-40,-20,0,20]:
        x=v_to_x(v)
        line(d,[(x,266),(x,515)],'gold' if v==0 else 'slate',2 if v==0 else 1,165 if v==0 else 55)
        puttext(d,(x,550),('+' if v>0 else '')+str(v)+'%',15,'beige','en')
    puttext(d,(421,242),'שתי קבוצות — בסיס השוואה זהה',18,'beige')
    puttext(d,(415,304),'מניות כל הבנקים המסחריים',20,'beige')
    puttext(d,(415,424),'מניות שאינן בנקאיות',20,'beige')
    bank=8.6;other=-57.5
    anim=smooth((p-.02)/.22)
    # actual length = absolute measured return / span * total chart width
    by=334;oy=454
    d.rounded_rectangle((zero,by,v_to_x(bank*anim),by+30),radius=5,fill=col('blue'))
    d.rounded_rectangle((v_to_x(other*anim),oy,zero,oy+30),radius=5,fill=col('red'))
    # Colors strictly use Liron's positive blue and negative red.
    puttext(d,(min(735,v_to_x(bank)+58),349),'+8.6%',26,'blue','en',True)
    puttext(d,(204,508),'−57.5%',26,'red','en',True)
    puttext(d,(419,583),'מקור: מבקר המדינה (1984), לוח 1.3, עמ׳ 19',14,'beige')

def graphic_3(d,t,p):
    puttext(d,(420,195),'מלאי הוויסות ערב המשבר',25,'beige',bold=True)
    # Stacked abstract bank-share holdings. No numeric y-axis; explicitly illustration.
    for i in range(12):
        j=i%4;k=i//4
        x=230+j*100;y=406-k*58
        start=(i*.042+.10)
        q=smooth((p-start)/.28)
        if q<=0:continue
        w=60*q
        d.polygon([(x,y),(x+w,y),(x+w+17,y-13),(x+17,y-13)],fill=col('gold',195))
        d.polygon([(x,y),(x+w,y),(x+w,y+23),(x,y+23)],fill=col('navy'))
        d.polygon([(x+w,y),(x+w+17,y-13),(x+w+17,y+10),(x+w,y+23)],fill=col('blue',185))
        line(d,[(x,y+23),(x+w,y+23)],'gold',2,180)
    label(d,(144,457,700,524),'מלאי ויסות: כ־1.06 מיליארד דולר','beige',26,'gold','ink',True)
    puttext(d,(422,562),'ליום 6.10.1983  |  אינו עלות החילוץ הממשלתי',18,'beige')
    puttext(d,(422,586),'ערימות המניות הן המחשה, אינן כמויות מדודות',14,'slate')

def graphic_4(d,t,p):
    puttext(d,(422,193),'יום חמישי · הפסקת המסחר',26,'beige',bold=True)
    rounded(d,(142,238,692,401),'ink','gold',16,2,252)
    puttext(d,(418,302),'06.10.1983',59,'yellow','en',True)
    puttext(d,(418,368),'המסחר בבורסה הופסק',26,'beige',bold=True)
    # abstract shutter; never depict TASE building physically destroyed
    q=smooth((p-.23)/.55)
    for i in range(8):
        x=197+i*66
        dh=24+60*q
        yy=453+20*(i%2)
        d.rounded_rectangle((x,yy,x+42,yy+dh),radius=7,fill=col('navy'),outline=col('red',170),width=2)
    puttext(d,(419,571),'לא התמוטטות של מבנה הבורסה — עצירת מסחר',18,'beige')

def graphic_5(d,t,p):
    puttext(d,(416,194),'הסדר 1983: התחייבות לאורך זמן',23,'beige',bold=True)
    y=373;start=126;end=718
    line(d,[(start,y),(end,y)],'slate',3,190)
    yrs=[1983,1985,1987,1988,1989]
    for i,yv in enumerate(yrs):
        x=start+(yv-1983)/6*(end-start)
        q=smooth((p-i*.09)/.25)
        dot(d,x,y,10*q,'blue' if i>0 else 'gold',230)
        if q>.02:
            puttext(d,(x,y-39),str(yv),17,'gold' if i==0 else 'blue','en',True)
            if i>0:
                line(d,[(x,y+17),(x,y+43)],'blue',2,int(165*q))
    label(d,(160,246,686,311),'פדיון עתידי לבעלי מניות זכאים','beige',22,'gold','ink',True)
    label(d,(217,463,628,520),'אחריות והתחייבות ציבורית','beige',22,'slate','navy')
    puttext(d,(418,570),'מרווחי הזמן על הציר משקפים שנים — לא תשלומים בפועל',15,'beige')

def graphic_6(d,t,p):
    puttext(d,(416,190),'הפיקוח היה מודע לסכנה',25,'beige',bold=True)
    q=smooth((p-.08)/.35)
    rounded(d,(132,239,702,344),'navy','gold',16,1,240)
    puttext(d,(222,293),'1981',39,'blue','en',True)
    puttext(d,(501,291),'אזהרות לרשויות הפיקוח',21,'beige',bold=True)
    arrow(d,(420,359),(420,433),'gold',q)
    rounded(d,(132,445,702,551),'ink','red',16,1,244)
    puttext(d,(222,498),'1983',39,'red','en',True)
    puttext(d,(509,493),'המשבר והסדר המדינה',21,'beige',bold=True)
    puttext(d,(418,580),'השאלה הפוליטית: מי ידע, מי פעל ומי שילם?',17,'beige')

GRAPHICS=[graphic_0,graphic_1,graphic_2,graphic_3,graphic_4,graphic_5,graphic_6]

def top_scene_progress(d,t,i):
    bar_left=58;bar_right=1223;y=623
    line(d,[(bar_left,y),(bar_right,y)],'slate',2,90)
    line(d,[(bar_left,y),(bar_left+(bar_right-bar_left)*t/DURATION,y)],'gold',3,235)
    for s,(a,b) in enumerate(SCENES):
        x=bar_left+(bar_right-bar_left)*a/DURATION
        dot(d,x,y,3,'gold' if s<=i else 'slate')


def frame(t, footage=None):
    idx=next((i for i,(a,b) in enumerate(SCENES) if a<=t<b),6)
    start,end=SCENES[idx]
    p=clamp((t-start)/(end-start))
    img=BASE.copy()
    # Genuine moving 3D originally rendered from 3D objects, subdued in a dedicated
    # center-stage area. Reuse original film as backing layer, not as real archival footage.
    if footage is not None:
        cut=footage.crop((70,50,1200,670)).resize((696,382),Image.Resampling.BILINEAR)
        cut.putalpha(62)
        img.alpha_composite(cut,(70,170))
        # darken to ensure intentional abstract background, graphic overlays stay legible
        sh=Image.new('RGBA',(696,382),col('ink',48));img.alpha_composite(sh,(70,170))
    layer=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(layer)
    GRAPHICS[idx](d,t,p)
    scene_panel(d,idx,p)
    top_scene_progress(d,t,idx)
    scene_alpha=alpha_transition(p)
    layer.putalpha(layer.getchannel('A').point(lambda v: int(v*scene_alpha)))
    img.alpha_composite(layer)
    return img.convert('RGB')


def render(draft=False,fps=24,output=None,max_frames=None,start_at=0,stop_at=None,frames_dir=None):
    if not Path(HE_FONT).exists():raise RuntimeError('No Hebrew font. Set BT_HE_FONT and BT_HE_BOLD.')
    if output is None:output=OUT
    ff=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}',
        '-r',str(fps),'-i','pipe:','-an','-c:v','libx264','-preset','ultrafast',
        '-crf','24' if draft else '20','-pix_fmt','yuv420p','-movflags','+faststart',str(output)]
    if frames_dir is not None:
        frames_dir=Path(frames_dir);frames_dir.mkdir(parents=True,exist_ok=True)
        proc=None
    else:
        proc=subprocess.Popen(ff,stdin=subprocess.PIPE)
    start_frame=int(round(start_at*fps))
    stop_frame=int(round((stop_at if stop_at is not None else DURATION)*fps))
    if max_frames is not None: stop_frame=min(stop_frame,start_frame+max_frames)
    total=stop_frame-start_frame
    # Re-render a clean caption-free 3D scene as the subdued abstract background.
    source=None
    for n in range(total):
        t=(n+start_frame)/fps
        if n % 3 == 0 or source is None:
            bgr, _shot = draw_original_3d_scene(t * 72 / DURATION)
            source=Image.fromarray(cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)).convert('RGBA')
        frm=frame(t,source)
        if n==int(6*fps):
            POSTER.parent.mkdir(parents=True,exist_ok=True)
            frm.save(POSTER)
        if frames_dir is not None:
            # Video is encoded separately. This avoids decoder/encoder pipe stalls.
            frm.save(frames_dir/f'frame_{n+start_frame:05d}.jpg',quality=93,subsampling=0)
        else:
            try:proc.stdin.write(frm.tobytes())
            except BrokenPipeError:break
        if n%(fps*10)==0:print(f'  time {t:.0f}s / {DURATION:.0f}s',flush=True)
    if frames_dir is not None:
        print('Created frame images:',frames_dir,flush=True)
        return
    proc.stdin.close();r=proc.wait()
    if r:raise RuntimeError(f'ffmpeg exited with {r}')
    print('Created:',output,'size',Path(output).stat().st_size,'bytes',flush=True)


def sample_frame(t,outpath):
    bgr,_shot=draw_original_3d_scene(t*72/DURATION)
    source=Image.fromarray(cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)).convert('RGBA')
    frame(t,source).save(outpath)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--fps',type=int,default=20)
    ap.add_argument('--draft',action='store_true')
    ap.add_argument('--max-frames',type=int,default=None)
    ap.add_argument('--start-at',type=float,default=0)
    ap.add_argument('--stop-at',type=float,default=None)
    ap.add_argument('--frames-dir',type=Path,default=None)
    ap.add_argument('--sample',type=float,help='Render one PNG at this timestamp, not entire film')
    ap.add_argument('--out',type=Path,default=None)
    arg=ap.parse_args()
    if arg.sample is not None:
        path=arg.out or Path('/tmp/black-thursday-v3-sample.png')
        sample_frame(arg.sample,path)
        print('Sample:',path)
    else:render(arg.draft,arg.fps,arg.out,arg.max_frames,arg.start_at,arg.stop_at,arg.frames_dir)
