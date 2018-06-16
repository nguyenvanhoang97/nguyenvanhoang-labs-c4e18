from turtle import *

shape("turtle")
speed(0)
color("green")

def draw_star(x , y , s_le):
    penup()
    setpos(x , y)
    pendown()
    left(36)

    for i in range(5):
        left(144)
        forward(s_le)


draw_star(10 , 10 , 100)


mainloop()