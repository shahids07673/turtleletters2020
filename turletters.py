import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.fd(40)
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(60)
    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	tur.setheading(0)
        tur.left(90)
        tur.fd(100)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(40)
        tur.left(180)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(100)
        tur.right(90)
        tur.fd(50)
    elif letter == "C":
	t = turtle.Turtle()
	tur.up()
	tur.bk(180)
	tur.left(90)
	tur.down()
	tur.fd(180)
	tur.right(90)
	tur.fd(180)
	tur.bk(180)
	tur.right(90)
	tur.fd(180)
	tur.left(90)
	tur.fd(180)
	tur.bk(180)
	tur.left(90)
	tur.fd(180)
	tur.right(90)
	tur.fd(180)
    elif letter == "D":
	turtle.fd(50)
	turtle.left(90)
	turtle.fd(100)
	turtle.left(90)
	turtle.fd(50)
	turtle.left(90)
	turtle.fd(100)
	turtle.left(90)
    elif letter == "E":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.pd()
        tur.fd(40)
        tur.right(270)
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(35)
    elif letter == "F":
	tur.setheading(0)
        tur.pd()
        tur.left(90)
        tur.fd(100)
        tur.right(90)
        tur.fd(50)
        tur.bk(50)
        tur.right(90)
        tur.fd(50)
        tur.left(90)
        tur.fd(25)
    elif letter == "G":
	t = turtle.Turtle()
	tur.up()
	tur.bk(180)
	tur.left(90)
	tur.down()
	tur.fd(180)
	tur.right(90)
	tur.fd(180)
	tur.bk(180)
	tur.right(90)
	tur.fd(180)
	tur.left(90)
	tur.fd(180)
	tur.bk(180)
	tur.left(90)
	tur.fd(180)
	tur.bk(180)
	tur.right(90)
	tur.fd(180)
	tur.left(90)
	tur.fd(90)
	tur.left(90)
	tur.forward(90)
	tur.bk(90)
	tur.right(90)
	tur.bk(90)
	tur.left(90)
	tur.forward(180)
	tur.right(90)
	tur.fd(180)
	tur.right(90)
	tur.fd(180)
    elif letter == "H":
	import turtle
	tur = turtle.Turtle()
	tur.down()
	tur.left(90)
	tur.fd(100)
	tur.bk(50)
	tur.right(90)
	tur.fd(50)
	tur.right(90)
	tur.fd(50)
	tur.bk(100)
	tur.left(90)
	tur.up()
    elif letter == "I":
	tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.left(90)
        tur.pd()
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.pd()
        tur.fd(40)
        tur.pu()
        tur.right(90)
        tur.fd(15)
        tur.right(180)
        tur.pd()
        tur.fd(30)
        tur.pu()
        tur.fd(5)
        tur.left(90)
        tur.fd(50)
        tur.right(90)
    elif letter == "J":
	import turtle
	tur. = turtle.Turtle()
	tur.down()
	tur.left(90)
	tur.bk(45)
	tur.right(90)
	tur.fd(90)
	tur.left(90)
	tur.fd(190)
	tur.left(90)
	tur.fd(90)
	tur.left(180)
	tur.fd(180)
    elif letter == "K":
	tur.pendown()
	tur.left(90)
	tur.fd(50)
	tur.bk(20)
	tur.right(50)
	tur.bk(30)
	tur.right(80)
	tur.fd(30)
	tur.bk(30)
	tur.left(80)
	tur.left(80)
	tur.penup()
	tur.fd(50)
	tur.right(45)
	tur.penup()
    elif letter == "L":
	tur.setheading(0)
        tur.pd()
        tur.fd(50)
        tur.bk(50)
        tur.left(90)
        tur.fd(100)
    elif letter == "M":
	turtle.left(90)
	turtle.forward(100)
	turtle.right(150)
	turtle.forward(50)
	turtle.left(120)
	turtle.forward(50)
	turtle.right(150)
	turtle.forward(100)
    elif letter == "N":
	turtle.left(90)
	turtle.forward(100)
	turtle.right(150)
	turtle.forward(110)
	turtle.left(150)
	turtle.forward(100)    
    elif letter == "O":
	tur.setheading(0)
        tur.pd()
        tur.circle(50)
        tur.pu()
        tur.left(90)
        tur.fd(120)
        tur.right(90)
        tur.fd(60)
    elif letter == "P":
	 tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.forward(30)
        tur.right(180)
        tur.forward(30)
        tur.right(90)
        tur.circle(-10, 180)
        tur.pu()
        tur.right(180)
        tur.forward(20)
        tur.left(90)
        tur.forward(25)
        tur.right(90)
        tur.pd()
    elif letter == "Q":
	tur.setheading(0)
        tur.pd()
        tur.circle(50)
        tur.pu()
        tur.left(45)
        tur.fd(30)
        tur.pd()
        tur.right(75)
        tur.fd(40)
        tur.pu()
        tur.left(120)
        tur.fd(140)
        tur.right(90)
    elif letter == "R":
	tur.setheading(0)
        tur.pd()
        tur.left(90)
        tur.fd(100)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.left(135)
        tur.fd(75)
        tur.bk(75)
        tur.left(135)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
    elif letter == "S":
	tur.setheading(0)
        tur.fd(50)
        tur.left(90)
        tur.fd(50)
        tur.left(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
    elif letter == "T":
	tur.setheading(0)
        tur.pd()
        tur.left(90)
        tur.fd(50)
        tur.left(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(40)
        tur.pu()
    elif letter == "U":
	tur.setheading(0)
        tur.pd()
        tur.left(90)
        tur.fd(50)
        tur.right(180)
        tur.fd(50)
        tur.left(90)
        tur.fd(40)
        tur.left(90)
        tur.fd(50)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
    elif letter == "V":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(30)
        tur.forward(30)
        tur.left(120)
        tur.forward(30)
        tur.pu()
        tur.forward(6)
        tur.right(60)
        tur.forward(3)
        tur.pd()
    elif letter == "W":
	tur.setheading(0)
        tur.pd()
        tur.right(70)
        tur.fd(40)
        tur.left(150)
        tur.fd(20)
        tur.right(150)
        tur.fd(20)
        tur.left(150)
        tur.fd(40)
    elif letter == "X":
	 tur.right(45)
        tur.fd(40)
        tur.left(135)
        tur.pu()
        tur.fd(30)
        tur.left(90)
        tur.pd()
        tur.left(45)
        tur.fd(40)
    elif letter == "Y":
	tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(30)
        tur.forward(30)
        tur.left(120)
        tur.forward(30)
        tur.pu()
        tur.right(60)
        tur.pu()
        tur.left(150)
        tur.pd()
        tur.left(90)
        tur.fd(30)
    elif letter == "Z":	
	tur.fd(30)
	tur.right(135)
	tur.fd(40)
	tur.right(225)
	tur.fd(30) 

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
