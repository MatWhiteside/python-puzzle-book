#Vanishing Point Perspective - 101computing.net/vanishing-point-perspective/
import turtle
myPen = turtle.Turtle()
#myPen.shape("arrow")
myPen.hideturtle()

myPen.color("purple")
# myPen.tracer(0)
myPen.speed(0)

x_vanishingPoint=0
y_vanishingPoint=150
y_horizon=100

xBottomLeft = -200
yBottomLeft = -200
xBottomRight = 200
yBottomRight = -200
xTopLeft=-1 #Will be calculated later on in the program
yTopLeft=y_horizon
xTopRight=-1 #Will be calculated later on in the program
yTopRight=y_horizon

numberOfCols = 5
numberOfRows = 12
rowHeight = 40

a1=0
a2=0
b1=0
b2=0

#Draw Vertical Vanishing Lines
for i in range(0,numberOfCols+1):
    xFrom=xBottomLeft +(xBottomRight - xBottomLeft)/numberOfCols*i
    yFrom=yBottomLeft
    #Line Equation: y=ax+b
    if xFrom!=x_vanishingPoint:
      a=(yFrom-y_vanishingPoint)/(xFrom-x_vanishingPoint)
      b=y_vanishingPoint - (a*x_vanishingPoint)
      x_horizon = (y_horizon - b)/a
    else:
      x_horizon = xFrom
    myPen.penup()
    myPen.goto(xFrom,yFrom)
    myPen.pendown()
    myPen.goto(x_horizon,y_horizon)
    if i==0:
      xTopLeft = x_horizon
      a1=a
      b1=b
    elif i==numberOfCols:
      xTopRight= x_horizon
      a2=a
      b2=b
      
ratio = 0.8
numberOfRows+=1 #Number of lines to draw
rowHeight = (y_horizon-yBottomLeft)*(ratio-1)/((ratio**(numberOfRows-1))-1)

#Draw Horizontal Lines 
yFrom=yBottomLeft
yTo=yBottomLeft
for i in range(0,numberOfRows):
  xFrom=(yFrom-b1)/a1
  xTo=(yTo-b2)/a2
  myPen.penup()
  myPen.goto(xFrom,yFrom)
  myPen.pendown()
  myPen.goto(xTo,yTo)  
  yFrom+=rowHeight
  yTo+=rowHeight
  rowHeight*=ratio
  
#draw Horizon Line
#myPen.penup()
#myPen.goto(-200,y_horizon)
#myPen.pendown()
#myPen.goto(200,y_horizon)  
    

myPen.getscreen().update()    
myPen.exitonclick()