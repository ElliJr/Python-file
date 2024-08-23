from turtle import *
    
spiral = Turtle()
spiral.pencolor("white")
bgcolor("black")

for i in range(40):
    spiral.forward(i * 10)
    spiral.right(100)

done()