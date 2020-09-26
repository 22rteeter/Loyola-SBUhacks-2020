
from processing import *



#speed of ball
level=5
platformsp=0
slopeVar=0
layers=8

#how blocks work
class Block:
  def __init__(self,xcord,ycord,alive):
    self.xcord=xcord
    self.ycord=ycord
    self.alive=alive
  def draw(self):
    rect(self.xcord,self.ycord,25,5)

class Ball:
  def __init__(self,xcord,ycord,xsp,ysp):
    self.xcord=xcord
    self.ycord=ycord
    self.ysp=ysp
    self.xsp=xsp
    self.alive=True
  
  #update position
  def move(self):
    self.xcord+=self.xsp
    self.ycord+=self.ysp
  
  #collisions
  def collideX(self):
    self.xsp=-1*self.xsp
  def collideY(self):
    self.ysp=-1*self.ysp

#create initial ball
ball=Ball(250,200,3,level)

class Platform:
  def __init__(self, xcord,ycord):
    self.xcord=xcord
    self.ycord=ycord
    #rect(self.xcord,self.ycord,100,10)
  def draw(self):
    rect(self.xcord,self.ycord,100,10)
  #couldnt figure out key pressing
  def moveRight(self):
    self.xcord+=4
  def moveLEft(self):
    self.ycord+=4

#create platform
platform=Platform(200,290)



#frame number is useful for draw
frameCount=0



def setup():
  #radius of ball
  frameRate(100)
  strokeWeight(10)
  size(500,300)
  #creates all blocks as objects in a list
  global blocks
  blocks=[]
  i=0
  while i<20*layers:
    blocks+=[Block(i%20*25,5*floor(i/20)+10,True)]
    i+=1



def draw():
  background(255)
  text("Brick🧱 Breaker", 200,10)
  strokeWeight(0.01)
  #global is used because these variables were defined outside the draw function
  global frameCount
  global blocks
  global ball
  global platform
  global slopeVar
  global platformsp
  #blocks[frameCount].alive=False
  #print(frameCount)
  
  
  #drawing the blocks that are alive
  frameCount+=1
  i=0
  stroke(255)
  while i<len(blocks):
    #coloring blocks
    if i==0:
      fill(255,40,40)
    if i==20:
      fill(223,35,35)
    if i==40:
      fill(191,30,30)
    if i==60:
      fill(159,25,25)
    if i==80:
      fill(127,20,20)
    if i==100:
      fill(95,15,15)
    if i==120:
      fill(63,10,10)
    if i==140:
      fill(31,5,5)
    
    
    if blocks[i].alive == True:
      blocks[i].draw()
    
    i+=1
  
  strokeWeight(10)
  #draws the ball
  stroke(10,10,255)
  if ball.alive:
    point(ball.xcord,ball.ycord)
    ball.move() 
  
  #collisions
  if ball.ycord>platform.ycord-10 and ball.xcord>platform.xcord and ball.xcord<platform.xcord+100:
    ball.collideY()
    ball.xsp=ball.xsp/2+platformsp/2
  if ball.xcord-10<0:
    ball.collideX()
  if ball.xcord+10>500:
    ball.collideX()
  if ball.ycord-10<0:
    ball.collideY()
  #with blocks
  i=0
  while i<len(blocks):
    y=blocks[i].ycord
    x=blocks[i].xcord
    #           collision with top of block
    if blocks[i].alive and ball.ycord-10<y and ball.xcord>x and ball.xcord<x+25:
      ball.ysp=-1*(ball.ysp)
      blocks[i].alive=False
    i+=1
  
  stroke(0)
  #platform stuff
  #changing ball's x speed based on how the platform moves
  slopeVar=platform.xcord
  platform.xcord=mouseX-50
  platformsp=platform.xcord-slopeVar
  platform.draw()
  
  if ball.ycord>300:
    print("GAME OVER")
    ball.alive=False

  


run()
