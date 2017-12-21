import math
from turtle import *
ht()
global lines
global shape
speed(0)
tracer(0, 0)
lines=[[0,1],[0,3],[0,4],[2,1],[2,3],[2,6],[5,1],[5,4],[5,6],[7,3],[7,4],[7,6]]          
shape= [[100,100,100],[100,-100,100],[-100,-100,100],[-100,100,100],[100,100,-100],[100,-100,-100],[-100,-100,-100],[-100,100,-100]]
def dotat( x, y ):
    pu()
    goto(x,y)
    dot()
    pd
def line(x1,y1,x2,y2):
    pu()
    goto(x1,y1)
    pd()
    goto(x2,y2)
def render():
   ct=0
   while(ct<len(shape)):
       dotat(x=shape[ct][0],y=shape[ct][1])
       ct+=1
   ct=0
   while(ct<len(lines)):
       l1=lines[ct][0]
       l2=lines[ct][1]
       x1=shape[l1][0]
       y1=shape[l1][1]
       x2=shape[l2][0]
       y2=shape[l2][1]
       line(x1,y1,x2,y2)
       ct+=1
def rotatez(an):
    sin=math.sin(math.radians(an))
    cos=math.cos(math.radians(an))
    rct=0
    while(rct<len(shape)):
        x=shape[rct][0]
        y=shape[rct][1]
        shape[rct][0]=(x*cos)-(y*sin)
        shape[rct][1]=(y*cos)+(x*sin)
        rct+=1 
def rotatex(an):
    sin=math.sin(math.radians(an))
    cos=math.cos(math.radians(an))
    rct=0
    while(rct<len(shape)):
        y=shape[rct][1]
        z=shape[rct][2]
        shape[rct][1]=(y*cos)-(z*sin)
        shape[rct][2]=(z*cos)+(y*sin)
        rct+=1   
def rotatey(an):
    sin=math.sin(math.radians(an))
    cos=math.cos(math.radians(an))
    rct=0
    while(rct<len(shape)):
        x=shape[rct][0]
        z=shape[rct][2]
        shape[rct][0]=(x*cos)-(z*sin)
        shape[rct][2]=(z*cos)+(x*sin)
        rct+=1   
render()
while(1):
    update()
    ax=input("Axis of rotation?(x/y/z)\n")
    ang=float(input("Angle of rotation? "))
    if(ax=='z'):
        print("Rotating around Z axis...")
        rotatez(ang)
        clear()
        render()
    elif(ax=='x'):
        print("Rotating around X axis...")
        rotatex(ang)
        clear()
        render()
    elif(ax=='y'):
        print("Rotating around Y axis...")
        rotatey(ang)
        clear()
        render()  
               
