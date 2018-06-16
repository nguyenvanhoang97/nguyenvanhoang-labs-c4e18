from random import *
from eval import calc

def generate_quiz():
    x = randint(1 , 10)
    y = randint(1 , 10)

    ops = ["+" , "-" , "*" , "/"]
    op = choice(ops)

    result = calc(x , y , op)

    err = choice([-1 , 0 , 1])

    return [x , y , op , result + err]

def check_answer(x, y, op, display_result, user_choice):
    result = calc(x , y ,op)
    if result == display_result:
        if user_choice == True:
            return True
        else:
            return False
    else:
        if user_choice == True:
            return False
        else:
            return True