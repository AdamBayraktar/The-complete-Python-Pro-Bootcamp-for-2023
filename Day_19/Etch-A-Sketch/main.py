from turtle import Turtle, Screen

adam = Turtle(shape="turtle")
screen = Screen()
# screen.exitonclick()
screen.listen()

def main():
    adam.color('pink')
    adam.speed(0)
    screen.onkeypress(forward, "Up")
    screen.onkeypress(backward, "Down")
    screen.onkeypress(left, "Left")
    screen.onkeypress(right, "Right")
    screen.onkey(reset, "c")
    screen.exitonclick()
    

def forward():
    adam.fd(10)

def backward():
    adam.bk(10)

def left():
    adam.lt(10)

def right():
    adam.rt(10)

def reset():
    adam.clear()
    adam.up()
    adam.home()
    adam.down()



if __name__ == "__main__":
    main()
