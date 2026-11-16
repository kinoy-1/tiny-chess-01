import os
from json import*
from urllib.request import*
O=os.environ['MAKEFUN_ENV_URL']
V=[0,100,320,330,500,900,0]
T=['','22222222<<<<<<<<44688644334774332226622231022013344..44322222222','(*,,,,*(*.2222.*,245542,,356653,,256652,,345543,*.2332.*(*,,,,*(','.000000.022222200234432003344330024444200444444003222230.000000.','2'*64,'2'*64,'2'*64]
KN=[31,33,14,18,-31,-33,-14,-18]
DG=[15,17,-15,-17]
OR=[16,1,-16,-1]
I=10**6
N=[Z:=0]
C=20000
class A(Exception):pass
def P(a,b):
 return load(urlopen(Request(O+a,dumps(b).encode(),{'content-type':'application/json'})))
def F(f):
 p=f.split();b=[0]*128;r=7;f=0
 for c in p[0]:
  if c=='/':r-=1;f=0
  elif c.isdigit():f+=int(c)
  else:b[r*16+f]=('PNBRQK'.find(c.upper())+1)*(2*(c<'a')-1);f+=1
 w=p[1]=='w'
 c=sum(1<<i for i,z in enumerate('KQkq') if z in p[2])
 e=-1
 if p[3]!='-':e=(int(p[3][1])-1)*16+ord(p[3][0])-97
 return b,w,c,e
def H(b,s,q):
 for o,v in((((15,17),(-15,-17))[q],1),(KN,2),(DG+OR,6)):
  for d in o:
   t=s+d
   if not t&0x88 and b[t]==(v if q else -v):return 1
 for j,d in enumerate(DG+OR):
  t=s+d
  while not t&0x88:
   x=b[t]
   if x:
    if(x>0)==q and(abs(x)==(3 if j<4 else 4)or abs(x)==5):return 1
    break
   t+=d
 return 0
def K(b,w):
 return b.index(6 if w else -6)
def G(b,w,c,e):
 m=[];g=1 if w else -1
 def A(s,t):
  r=t>>4
  if(w and r==7)or(not w and r==0):
   for q in(5,4,3,2):m.append(s|(t<<7)|(q<<14))
  else:m.append(s|(t<<7))
 for s,p in enumerate(b):
  if s&0x88 or p*g<=0:continue
  a=abs(p)
  if a==1:
   d=16 if w else -16;t=s+d
   if not t&0x88 and b[t]==0:
    A(s,t)
    if(s>>4)==(1 if w else 6):
     u=s+2*d
     if b[u]==0:m.append(s|(u<<7))
   for z in(d-1,d+1):
    t=s+z
    if not t&0x88 and(b[t]*g<0 or t==e):A(s,t)
  else:
   for d in(KN if a==2 else DG if a==3 else OR if a==4 else DG+OR):
    t=s+d
    while not t&0x88:
     x=b[t]
     if x*g>0:break
     m.append(s|(t<<7))
     if x or a==2 or a==6:break
     t+=d
 for r,k,q,j in((1,4,1,3),(2,4,-1,4),(4,116,1,3),(8,116,-1,4)):
  if c&r and b[k+q]==0 and b[k+2*q]==0 and(j==3 or b[k+3*q]==0) and not(H(b,k,not w)or H(b,k+q,not w)or H(b,k+2*q,not w)):m.append(k|((k+2*q)<<7))
 return m
def D(b,m,w,c,e):
 f=m&127;t=(m>>7)&127;q=m>>14;p=b[f];y=b[t];z=t
 if abs(p)==1 and t==e and y==0:
  z=t-16 if w else t+16;y=b[z];b[z]=0
 b[t]=q*(1 if w else -1) if q else p;b[f]=0
 a=-1;d=-1
 if abs(p)==6 and abs(t-f)==2:
  a,d=(t+1,t-1)if t>f else(t-2,t+1)
  b[d]=b[a];b[a]=0
 for s in(f,t):c&=~{0:2,7:1,4:3,112:8,116:12,119:4}.get(s,0)
 k=-1
 if abs(p)==1 and abs(t-f)==32:k=(f+t)//2
 return y,z,a,d,c,k
def U(b,m,w,u):
 y,z,a,d,c,k=u;f=m&127;t=(m>>7)&127;q=m>>14;p=b[t]
 if q:p=1 if w else -1
 b[f]=p;b[t]=0
 if y:b[z]=y
 if a>=0:b[a]=b[d];b[d]=0
def E(b,w):
 s=0
 for i,x in enumerate(b):
  if x:
   a=abs(x);r=i>>4;f=i&7
   v=V[a]+(ord(T[a][f+8*(7-r) if x>0 else f+8*r])-50)*5
   if a==6:v-=6*max(0,(r-1)if x>0 else(6-r))
   s+=v if x>0 else -v
 return s if w else -s
def S(b,m):
 f=m&127;t=(m>>7)&127;q=m>>14;x=b[t]
 s=10*V[abs(x)]-V[abs(b[f])]//10 if x else 0
 return s+9*V[q] if q else s
def R(b,w,c,e,d,a,l,y):
 global Z;N[0]+=1
 if N[0]>C:raise A
 q=d<=0
 if q:
  p=E(b,w)
  if p>=l:return l
  if p>a:a=p
 ms=G(b,w,c,e)
 if q:ms=[m for m in ms if b[(m>>7)&127]!=0 or(m>>14) or((m>>7)&127)==e]
 ms.sort(key=lambda m:-S(b,m))
 t=-I;o=0
 for m in ms:
  u=D(b,m,w,c,e);nc,ne=u[4],u[5]
  if H(b,K(b,w),not w):U(b,m,w,u);continue
  o+=1
  s=-R(b,not w,nc,ne,d-1,-l,-a,y+1)
  U(b,m,w,u)
  if s>t:t=s;Z=m if y==0 else Z
  if s>a:a=s
  if a>=l:break
 if o==0:return a if q else(-100000+y if H(b,K(b,w),not w) else 0)
 return a if q else t
def B(f):
 b,w,c,e=F(f);ms=[]
 for m in G(b,w,c,e):
  u=D(b,m,w,c,e)
  if not H(b,K(b,w),not w):ms.append(m)
  U(b,m,w,u)
 ms.sort(key=lambda m:-S(b,m))
 z=ms[0];d=0
 while d<30:
  d+=1;N[0]=0
  try:R(b,w,c,e,d,-I,I,0);z=Z
  except A:break
 return z
def W(m):
 f=m&127;t=(m>>7)&127;q=m>>14
 s=chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)
 if q:s+='nbrq'[q-2]
 return s
while(g:=P('/game',{}))['status']!='done':
 while g['status']=='your_move':g=P('/move',{'game':g['game'],'move':W(B(g['fen']))})