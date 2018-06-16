from turtle import *
shape("turtle")
speed(-1)

def draw_square(s_le, s_col):
    color(s_col)
    for i in range(4):
        forward(s_le)
        left(90)
    
draw_square(100 , "green")

mainloop()