"""Offline, reproducible 3D animation *video* exporter.

This is a genuine object-based three-dimensional software renderer: cuboid and
cylindrical meshes have X/Y/Z geometry; each shot has a 3D perspective camera,
per-face normal/directional lighting, depth sorting and moving 3D objects.
The still image and Hebrew caption layers are composited into final video frames.
This is an alternative to Three.js/WebGL when unavailable in the export environment.

Needs: numpy, opencv-python, Pillow, ffmpeg installed.
Usage: python animation/render_movie.py [--fps 24] [--duration 72]
"""
from pathlib import Path
from dataclasses import dataclass
import math,subprocess,argparse
import numpy as np
import cv2
from PIL import Image,ImageDraw,ImageFont

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'media/video/crisis-animation.mp4'
POSTER=ROOT/'media/images/video-poster.png'
SRC_W,SRC_H=960,540
DURATION=72
SHOTS=[(0,9,'01 / התמיכה','שנים של תמיכה','במשך שנים תמכו בנקים בשערי מניותיהם.'),
 (9,20,'02 / הוויסות','ביקוש שנוצר במערכת','רכישות תומכות יצרו ביקוש וסייעו להחזיק את השערים.'),
 (20,31,'03 / המנגנון','מארג של אינטרסים','הפעולות השתלבו במערכת מורכבת של תמריצים וניגודי עניינים.'),
 (31,43,'04 / מגבלת משאבים','יכולת מוגבלת','כשהמכירות גברו, היכולת להמשיך ולתמוך נשחקה.'),
 (43,53,'05 / נקודת השבר','6 באוקטובר 1983','המסחר בבורסה הופסק למשך 18 ימים.'),
 (53,65,'06 / ההתערבות','הסדר ציבורי ארוך־טווח','המדינה קיבלה התחייבויות פדיון עתידיות שנשאו עלויות ציבוריות.'),
 (65,72,'07 / השאלה הפוליטית','מי נושא בסיכון?','מי פיקח? מי קיבל החלטות? ומי נדרש לשלם?')]
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
C={'ink':(8,21,34),'gold':(217,174,104),'aqua':(100,188,168),'crisis':(212,107,104),'stone':(64,92,111),'tower':(38,71,91),'steel':(112,133,143),'dark':(20,45,64)}
LIGHT=np.array([-.5,.9,.6]);LIGHT/=np.linalg.norm(LIGHT)
CUBE=np.array([[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]],dtype=float)
FACES=[[4,5,6,7],[1,0,3,2],[5,1,2,6],[0,4,7,3],[7,6,2,3],[0,1,5,4]]

def ease(x):return min(1,max(0,x))
def norm(a):return a/(np.linalg.norm(a)+1e-9)
@dataclass
class Box:
 pos:tuple
 size:tuple
 color:str
 angle:float=0

class Scene:
 def __init__(self,eye):
  self.eye=np.array(eye,dtype=float);self.at=np.array([0,1,0],dtype=float);z=norm(self.eye-self.at);self.r=norm(np.cross([0,1,0],z));self.u=np.cross(z,self.r);self.back=z;self.polys=[]
 def camera_project(self,pts):
  relative=pts-self.eye;xx=relative@self.r;yy=relative@self.u;zz=-relative@self.back
  if np.any(zz<=.1):return None
  f=SRC_H*1.05
  return np.column_stack([SRC_W/2+f*xx/zz,SRC_H*.51-f*yy/zz])
 def box(self,obj):
  x,y,z=obj.pos; sx,sy,sz=obj.size;ca,sa=math.cos(obj.angle),math.sin(obj.angle)
  rot=np.array([[ca,0,sa],[0,1,0],[-sa,0,ca]])
  pts=(CUBE*np.array([sx,sy,sz]))@rot.T+np.array([x,y,z]);
  for face in FACES:
   vert=pts[face];normal=norm(np.cross(vert[1]-vert[0],vert[2]-vert[0]));
   if np.dot(normal,self.eye-vert[0])<=0:continue
   proj=self.camera_project(vert)
   if proj is None:continue
   illumination=.28+.72*max(0,np.dot(normal,LIGHT))
   col=np.array(C[obj.color])*illumination
   distance=np.linalg.norm(self.eye-vert.mean(axis=0))
   self.polys.append((distance,np.int32(np.round(proj)),tuple(int(v) for v in col[::-1])))
 def coin(self,x,y,z,r,color,angle=0):
  # Actual six-sided 3D prism, not a circular sprite.
  for i in range(8):
   theta=2*math.pi*i/8+angle
   self.box(Box((x+r*.72*math.cos(theta),y,z+r*.72*math.sin(theta)),(.17,.1,.17),color,theta))
  self.box(Box((x,y,z),(r*.67,.1,r*.67),color,angle))
 def render(self):
  frame=np.zeros((SRC_H,SRC_W,3),dtype=np.uint8)
  frame[:]=tuple(C['ink'][::-1]);yy=np.arange(SRC_H,dtype=np.float32)[:,None]
  frame[:,:,0]=np.clip(frame[:,:,0]+yy/SRC_H*5,0,255).astype(np.uint8)
  frame[:,:,1]=np.clip(frame[:,:,1]+yy/SRC_H*9,0,255).astype(np.uint8)
  for _,points,col in sorted(self.polys,key=lambda a:-a[0]):
   cv2.fillConvexPoly(frame,points,col,lineType=cv2.LINE_AA)
  return frame

def draw_scene(t):
 shot=next(i for i,s in enumerate(SHOTS) if s[0]<=t<s[1]);st,en,*_=SHOTS[shot];local=t-st
 theta=.43+.14*math.sin(t*.052)+.006*local
 scene=Scene((math.sin(theta)*13,7.3+.4*math.sin(t*.037),math.cos(theta)*17))
 scene.box(Box((0,-.5,0),(7.5,.2,5),'dark'))
 for i in range(-6,7):scene.box(Box((i,-.27,0),(.015,.015,4.9),'stone'))
 for i in range(-4,5):scene.box(Box((0,-.27,i),(7.4,.015,.015),'stone'))
 if shot==0:
  for i,(x,z,h) in enumerate([(-5,1,3.2),(-3,2.4,4.7),(-1,1.5,5.5),(1,1.4,4.4),(3,2.7,6.4),(5,1.8,3.5)]):
   scene.box(Box((x,h/2-.18,z),(.68,h/2,.64),'tower'))
   scene.box(Box((x,h-.1,z),(.65,.11,.65),'gold'))
   for j in range(1,int(h*2)):
    scene.box(Box((x,h-.35-j*.35,z+.69),(.5,.035,.008),'gold'))
  for i in range(14):scene.coin(-5+(i%5)*2.5,.27+.19*math.sin(i+t),-1+int(i/5)*2,.21,'aqua' if i%3==0 else 'gold',t*.4)
 elif shot==1:
  for x,color in [(-4,'tower'),(3.9,'stone')]:
   scene.box(Box((x,1,0),(1.1,1.3,1.2),color));scene.box(Box((x,2.4,0),(1.05,.1,1.05),'gold'))
  for i in range(17):
   p=((local*1.08+i*.27)%5)/5
   scene.coin(-4+7.9*p,.65+1.2*math.sin(p*math.pi),-.8+(i%3)*.72,.21,'gold',t*.5)
  for i in range(7):scene.box(Box((4, .3+i*.35,2),(.35,.14,.4),'aqua' if i<5 else 'crisis'))
 elif shot==2:
  points=[(-3,0),(-1,3),(3,2),(3,-2),(-1,-3)]
  for i,(x,z) in enumerate(points):
   scene.box(Box((x,.7,z),(.8,.85,.8),'stone' if i%2 else 'tower'))
   scene.coin(x,1.8,z,.45,'aqua' if i%2 else 'gold',t)
  for i in range(27):
   a=i/27*math.pi*2+t*.58;r=2.5
   scene.coin(r*math.sin(a),.4+.12*math.sin(2*a+t),r*math.cos(a),.14,'aqua' if i%2 else 'gold',t)
 elif shot==3:
  rem=max(0,1-local/12)
  scene.box(Box((-3.6,.6,0),(1.2,1.1,1.2),'tower'))
  if rem>.015:scene.box(Box((-3.6,1.2+rem*1.5,0),(1,rem*1.5,1),'aqua'))
  for i in range(23):
   p=((local*.52+i*.21)%4)/4
   scene.coin(5.8-8.8*p,.35+(i%4)*.23,-1.7+(i%5)*.9,.17,'crisis',t)
  for i in range(8):scene.box(Box((1.5+i*.4,.3+i*.15,0),(.12,.14+i*.08,.12),'crisis'))
 elif shot==4:
  for i in range(-4,5):scene.box(Box((i,.65,2),(.42,.9,.4),'stone'))
  closure=ease(local/5)
  for i in range(9):scene.box(Box((-4+i,2.65-1.35*closure,-.6),(.45,1.4*closure+.08,.32),'crisis'))
  scene.box(Box((0,2.5,-.6),(5,.14,.5),'gold'))
  for i in range(8):scene.coin(-3.5+i,.25,3,.22,'crisis',t)
 elif shot==5:
  for x,col in [(-4,'tower'),(0,'gold'),(4,'aqua')]:scene.box(Box((x,.95,0),(.95,1.25,1),col))
  for i in range(19):
   p=((local*.5+i*.13)%5.5)/5.5
   scene.coin(-4+8*p,.5+.7*math.sin(math.pi*p),.1,.15,'aqua' if p>.6 else 'gold',t)
  for i in range(7):scene.box(Box((-2.5+i*.82,.3+i*.1,-2),(.2,.15+i*.055,.19),'gold'))
 else:
  for i,color in enumerate(['gold','aqua','stone','crisis']):
   a=i/4*math.pi*2+t*.15
   scene.box(Box((3.2*math.cos(a),1.2,3.2*math.sin(a)),(.7,1.25,.7),color,a))
  scene.coin(0,1.1,0,.62,'gold',t*.45)
  for i in range(12):
   a=i/12*2*math.pi;scene.coin(4.4*math.cos(a),.35,4.4*math.sin(a),.13,'gold',t)
 return scene.render(),shot

def text_line(draw,xy,body,size,color,bold=False,anchor='ra'):
 font=ImageFont.truetype(BOLD if bold else FONT,size)
 draw.text(xy,body,font=font,fill=color,anchor=anchor,direction='rtl')

def make_overlay(shot):
 layer=Image.new('RGBA',(SRC_W,SRC_H),(0,0,0,0));draw=ImageDraw.Draw(layer)
 # Gradient lower panel and header, preserving footage center.
 for yy in range(0,130):
  alpha=round(135*(1-yy/130));draw.line([(0,yy),(SRC_W,yy)],fill=(2,8,14,alpha),width=1)
 for yy in range(342,SRC_H):
  a=round(225*(yy-342)/(SRC_H-342));draw.line([(0,yy),(SRC_W,yy)],fill=(2,8,14,a),width=1)
 _,_,k,title,caption=SHOTS[shot]
 draw.text((40,33),'BLACK THURSDAY  /  1983',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12),fill=C['gold']+(255,))
 text_line(draw,(SRC_W-37,33),'המחשה סכמטית — לא נתוני מסחר או צילום ארכיון',14,(245,240,230,255))
 text_line(draw,(SRC_W-44,370),k,18,C['gold']+(255,),True)
 text_line(draw,(SRC_W-44,423),title,36,(245,240,230,255),True)
 text_line(draw,(SRC_W-44,463),caption,19,(216,230,231,255))
 draw.rectangle((43,502,SRC_W-43,504),fill=(112,133,143,100))
 draw.text((43,517),'OBJECT-BASED 3D RENDER / NOT ARCHIVAL FOOTAGE',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',11),fill=(207,217,222,230))
 return np.array(layer)

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--fps',type=int,default=24);parser.add_argument('--duration',type=float,default=72);args=parser.parse_args()
 fps=args.fps;duration=args.duration
 overlays=[make_overlay(i) for i in range(7)]
 # ffmpeg receives RGB frame bytes, upscales to final 1280x720, then H.264, yuv420p, faststart.
 command=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-vcodec','rawvideo','-pix_fmt','bgr24','-s',f'{SRC_W}x{SRC_H}','-r',str(fps),'-i','-','-an','-vf','scale=1280:720:flags=lanczos','-c:v','libx264','-preset','veryfast','-crf','22','-pix_fmt','yuv420p','-movflags','+faststart',str(OUTPUT)]
 p=subprocess.Popen(command,stdin=subprocess.PIPE)
 frames=int(round(duration*fps))
 for f in range(frames):
  t=min(DURATION-.01,f/fps)
  frame,shot=draw_scene(t)
  layer=overlays[shot];alpha=layer[:,:,3:4].astype(np.float32)/255
  frame=(frame.astype(np.float32)*(1-alpha)+layer[:,:,:3][:,:,::-1].astype(np.float32)*alpha).astype(np.uint8)
  # Actual timeline progress marker overlaid inside every output frame.
  cv2.rectangle(frame,(43,501),(43+int((SRC_W-86)*t/DURATION),504),C['gold'][::-1],-1)
  if f==6:cv2.imwrite(str(POSTER),cv2.resize(frame,(1280,720),interpolation=cv2.INTER_LANCZOS4))
  try:p.stdin.write(frame.tobytes())
  except BrokenPipeError:break
  if f%240==0:print(f'{f}/{frames} frames',flush=True)
 p.stdin.close();ret=p.wait()
 if ret:raise RuntimeError('ffmpeg failed: '+str(ret))
 print('OUTPUT',OUTPUT,OUTPUT.stat().st_size,'bytes')
if __name__=='__main__':main()
