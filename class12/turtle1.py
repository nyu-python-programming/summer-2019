import turtle

turtle.color('red', 'yellow')
turtle.begin_fill()


for i in range(4):   
    turtle.forward(200)
    turtle.left(90)
    
    print(turtle.pos())
    position = turtle.pos()
    x = position[0]
    y = position[1]
    

turtle.end_fill()
turtle.done()



