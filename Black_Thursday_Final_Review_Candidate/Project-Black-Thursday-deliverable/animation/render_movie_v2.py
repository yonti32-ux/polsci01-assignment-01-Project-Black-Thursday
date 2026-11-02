"""Re-edit the project's *genuine pre-rendered 3D footage* into Liron's 72s v2.

One-pass offline re-edit with clear Hebrew source-backed captions. No new 3D
rendering pass is required; the original source 3D scene and renderer remain
inspectable in scene.js and render_movie.py. The base MP4 is itself a 3D render.

Requirements for re-export only: Pillow (with Hebrew shaping) and FFmpeg.
Run: python animation/render_movie_v2.py
"""
from pathlib import Path
import subprocess, os, shutil
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
IN=ROOT/'media/video/crisis-animation.mp4'
OUT=ROOT/'media/video/crisis-animation-v2.mp4'
POSTER=ROOT/'media/images/video-poster-v2.png'
LAYERS=ROOT/'animation/generated-v2-overlays'
W,H=1280,720
PALETTE={
 'ink':'#1c242c','gold':'#c19d43','cream':'#d3cebe','ocean':'#1f3c58','sky':'#8ab9ee',
 'muted':'#7a8694','paper':'#e7eef4','yellow':'#f5cb39','red':'#ed1c16'
}
def rgb(name):
  s=PALETTE[name].lstrip('#');return tuple(int(s[i:i+2],16) for i in (0,2,4))
def rgba(name,alpha=255):return rgb(name)+(alpha,)
REG=Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
BOLD=Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
if not REG.exists():REG=Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts/arial.ttf'
if not BOLD.exists():BOLD=Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts/arialbd.ttf'
def f(sz,bold=False):return ImageFont.truetype(str(BOLD if bold else REG),sz)
def he(d,x,y,s,sz,color='paper',bold=False):d.text((x,y),s,font=f(sz,bold),fill=rgba(color),direction='rtl',anchor='ra')
def en(d,x,y,s,sz,color='gold',bold=False):d.text((x,y),s,font=f(sz,bold),fill=rgba(color),anchor='la')
def card(d,box,border='gold',bg=(16,33,48,247)):
 d.rounded_rectangle(box,fill=bg,outline=rgba(border),width=2,radius=21)

# Timing is precisely aligned to the original 72s 7-shot 3D film.
CHAPTERS=[
 (0,9,'01 / תחילת הסיפור','הבנקים ושוק המניות','שערי מניות הבנקים נתפסו כיציבים יחסית לאורך זמן.','מבקר המדינה, דו״ח משבר 1983 (1984), עמ׳ 7–9'),
 (9,20,'02 / המנגנון','כך פעל ויסות המניות','גופים קשורים רכשו מניות כדי לתמוך במחיריהן.','מבקר המדינה (1984), עמ׳ 7–8, 22–24'),
 (20,31,'03 / נתוני אמת','שתי קבוצות, מגמות שונות','תשואה ריאלית מצטברת, ינואר–ספטמבר 1983.','מבקר המדינה (1984), עמ׳ 19, לוח 1.3'),
 (31,43,'04 / התנפחות הסיכון','כשהציבור התחיל למכור','הבנקים רכשו מניות נוספות, עד שמקורות המימון אזלו.','מבקר המדינה (1984), עמ׳ 7, 10'),
 (43,53,'05 / המשבר','6 באוקטובר 1983','הבורסה בתל אביב הפסיקה את המסחר; לא חדלה להתקיים.','מבקר המדינה (1984), עמ׳ 7, 10'),
 (53,65,'06 / תגובת המדינה','הסדר מניות הבנקים','המדינה התחייבה לפדיון עתידי; לא כל הכסף שולם ב־1983.','מבקר המדינה (1984), עמ׳ 7, 11'),
 (65,72,'07 / השאלה הציבורית','מי ידע — ומי פיקח?','אזהרות מ־1981 קדמו למשבר. אחריות ציבורית נבחנת גם בזמן.', 'מבקר המדינה (1984), עמ׳ 11–13'),
]

def overlay(i):
 img=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(img)
 st,en_t,code,title,desc,source=CHAPTERS[i]
 # Opaque editorial rails override small original caption rail, preserve 3D
 d.rectangle((0,0,W,143),fill=rgba('ink',246))
 d.rectangle((0,486,W,H),fill=rgba('ink',251))
 d.rectangle((1264,0,1279,144),fill=rgba('gold'))
 d.line((42,142,1240,142),fill=rgba('gold'),width=3)
 en(d,44,28,'BLACK THURSDAY   /   1983',20,'yellow',True)
 he(d,1220,46,'משבר מניות הבנקים בישראל',35,'paper',True)
 he(d,1220,109,'המחשה תלת־ממדית סכמטית — אינה תיעוד מצולם',17,'muted')
 # headline not crowded; marked stage and transitions
 he(d,1215,522,code,21,'gold',True)
 he(d,1215,583,title,42,'paper',True)
 he(d,1215,631,desc,23,'cream')
 he(d,1215,680,source,16,'muted')
 en(d,43,666,'3D DOCUMENTARY / EDUCATIONAL RECONSTRUCTION',13,'sky')
 for k in range(7):
  d.rounded_rectangle((45+k*30,117,65+k*30,125),radius=4,fill=rgba('yellow') if k<=i else rgba('muted',125))
 # Chapter-specific prominent explanation in the clear center of stage.
 if i==0:
  card(d,(58,186,575,437),'sky')
  he(d,543,251,'מניות הבנקים',34,'yellow',True)
  he(d,543,304,'נסחרו בבורסה בתל אביב',26,'paper',True)
  he(d,543,357,'אך המחירים לא שיקפו תמיד',20,'cream')
  he(d,543,395,'את הביקוש החופשי בשוק',20,'cream')
 elif i==1:
  card(d,(54,181,570,440),'gold')
  he(d,539,245,'מניה מוצעת למכירה',26,'paper')
  he(d,539,309,'↓',45,'sky',True)
  he(d,539,350,'רכישה בידי גורם קשור',28,'yellow',True)
  he(d,539,403,'תמיכה מלאכותית בשער',23,'cream')
 elif i==2:
  card(d,(55,171,1110,462),'sky')
  he(d,1078,214,'תשואות ריאליות • ינואר–ספטמבר 1983',27,'paper',True)
  zero=700
  d.line((zero,263,zero,444),fill=rgba('paper'),width=3)
  he(d,1045,277,'מניות כל הבנקים המסחריים',26,'cream')
  he(d,1045,381,'מניות אחרות (לא בנקאיות)',26,'cream')
  # A diverging zero-axis bar is proportional to both measured returns.
  # This is NOT a drawn 'bank index' or a fabricated daily market-price path.
  d.rounded_rectangle((zero,293,zero+86,325),fill=rgba('gold'),radius=7)
  d.rounded_rectangle((zero-575,399,zero,431),fill=rgba('red'),radius=7)
  en(d,zero+99,294,'+8.6%',29,'yellow',True)
  en(d,140,396,'-57.5%',30,'paper',True)
  he(d,1068,452,'השוואת קבוצות — לא מדדי מחירים ביום הקריסה',15,'muted')
 elif i==3:
  card(d,(60,192,676,443),'red')
  he(d,642,257,'מלאי הוויסות',34,'paper',True)
  he(d,642,323,'כ־1.06 מיליארד דולר',38,'yellow',True)
  he(d,642,384,'נכון ל־6.10.1983',26,'cream',True)
  he(d,642,420,'זה אינו סכום עלות החילוץ',20,'muted')
 elif i==4:
  card(d,(54,181,756,440),'red')
  en(d,90,212,'06 / 10 / 1983',53,'yellow',True)
  he(d,713,336,'הבורסה בתל אביב',38,'paper',True)
  he(d,713,405,'המסחר הופסק',43,'red',True)
 elif i==5:
  card(d,(56,179,717,447),'gold')
  he(d,687,238,'הסדר פדיון עתידי',38,'paper',True)
  en(d,89,288,'1985   /   1987   /   1988   /   1989',26,'yellow',True)
  he(d,687,382,'המדינה נטלה סיכון והתחייבויות',25,'cream')
  he(d,687,418,'החזרת מניות — לא תשלום מיידי',19,'muted')
 elif i==6:
  card(d,(56,174,701,447),'gold')
  en(d,95,214,'1981',48,'yellow',True)
  he(d,664,249,'הגורמים המפקחים הוזהרו',27,'paper')
  en(d,95,319,'1983',48,'red',True)
  he(d,664,359,'המשבר פרץ למרות האזהרות',25,'paper')
  he(d,664,423,'שאלת המחקר: מי אחראי לכך?',23,'cream')
 return img

def main():
 if not IN.is_file():raise FileNotFoundError(f'Missing original 3D-rendered source MP4: {IN}')
 if not shutil.which('ffmpeg'):raise RuntimeError('FFmpeg missing from PATH')
 LAYERS.mkdir(exist_ok=True)
 for i in range(len(CHAPTERS)):
  overlay(i).save(LAYERS/f'overlay_{i+1:02}.png')
 segments=[]
 for i,(start,end,*_) in enumerate(CHAPTERS):
  segment=LAYERS/f'segment_{i+1:02}.mp4'
  dur=end-start
  cmd=['ffmpeg','-y','-loglevel','error','-ss',str(start),'-t',str(dur),'-i',str(IN),'-loop','1','-framerate','20','-i',str(LAYERS/f'overlay_{i+1:02}.png'),'-filter_complex','[0:v][1:v]overlay=0:0:format=auto:shortest=1[v]','-map','[v]','-r','20','-an','-c:v','libx264','-preset','veryfast','-crf','21','-pix_fmt','yuv420p','-t',str(dur),str(segment)]
  subprocess.run(cmd,check=True)
  segments.append(segment)
  print(f'Chapter {i+1}/{len(CHAPTERS)} rendered: {dur}s',flush=True)
 playlist=LAYERS/'concat.txt'
 playlist.write_text(''.join(f"file '{x.as_posix()}'\n" for x in segments),encoding='utf-8')
 subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(playlist),'-c','copy','-movflags','+faststart',str(OUT)],check=True)
 subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','24','-i',str(OUT),'-frames:v','1',str(POSTER)],check=True)
 print('Created',OUT,OUT.stat().st_size,'bytes',flush=True)

if __name__=='__main__':main()
