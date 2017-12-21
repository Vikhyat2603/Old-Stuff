import math,time,str_ops
from turtle import *
###########################################################################################################
global lines,node,dx,dy,rot,locx,locy
rot=0
dx=-710
dy=-375
locx=dx
locy=dy
lines=[ [2,0] , [2,6] , [6,7] , [7,3] , [3,1] , [1,5] , [5,4] , [4,0] ,[2,8],[8,9],[9,3]]          
node=[ [-800,-350] , [-800,-400] , [-700,-350] , [-700,-400] , [-815,-365] , [-815,-385] , [-705,-365] , [-705,-385],[-695,-365] , [-695,-385]]
###########################################################################################################
def dotat( x, y ):
          goto(x,y)
          dot()
def line(x1,y1,x2,y2):
          goto(x1,y1)
          pd()
          goto(x2,y2)
          pu()
def render(obj):
          clear()
          if (obj=="all")|(obj=="cannon"):
                    ct=0
                    while ct<len(lines):
                              line1=node[lines[ct][0]]
                              line2=node[lines[ct][1]]
                              line(line1[0],line1[1],line2[0],line2[1])
                              ct+=1
          if(obj=="all"):
                    global locx,locy
                    goto(locx,locy)
                    dot(35,"black")
          update()
def rotate(an):
          global dx,dy,locx,locy,rot
          rot+=an
          rot%=360
          sin=math.sin(math.radians(an))
          cos=math.cos(math.radians(an))
          ct=0
          while ct<len(node):
                    x=node[ct][0]+807.5
                    y=node[ct][1]+375
                    node[ct][0]=x*cos-y*sin-807.5
                    node[ct][1]=y*cos+x*sin-375
                    ct+=1
          dx2=dx+807.5
          dy2=dy+375
          dx=dx2*cos-dy2*sin-807.5
          dy=dy2*cos+dx2*sin-375
          locx=dx
          locy=dy
          render("cannon")
def shoot(power):
          global rot,locx,locy
          goto(dx,dy)
          locx=dx
          locy=dy
          if(power>100):
                    print("Power is greater than 100\n")
                    return
          if(power<0):
                    print("Power is smaller than 0\n")
                    return
          xvel=float(math.cos(math.radians(rot)))*power
          yvel=float(math.sin(math.radians(rot)))*power
          render("all")
          while (locy>-374):
                    locx+=xvel
                    locy+=yvel
                    yvel-=0.2
                    goto(locx,locy)      
                    render("all")
                    time.sleep(0.01)
          time.sleep(0.25)
          render("cannon")
def clearball():
          clear()
          render("cannon")                    
def right():
          global done
          done=0
          rotate(-2)
          done=1
def left():
          global done
          done=0
          rotate(2)
          done=1
def initshoot():
          shoot(15)
###########################################################################################################
title("The Cannon Game")
setup(1920, 1040)
ht()
pu()
speed(0)
tracer(0, 0)
bgcolor("orange")
render("cannon")
onkeypress(right, "Right")
onkey(initshoot,"space")
onkeypress(left, "Left")
listen()
mainloop()
