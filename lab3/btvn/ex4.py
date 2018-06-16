from turtle import *
shape("turtle")
speed(-1)

def draw_square(s_le, s_col):
    color(s_col)
    for i in range(4):
        forward(s_le)
        left(90)
    

for i in range(30):
    draw_square(i * 5, 'red')

    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()