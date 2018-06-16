from random import randint , choice
# from eval import calc
import eval

x = randint(1 , 10)
y = randint(1 , 10)

ops = ["+" , "-" , "*" , "/"]
op = choice(ops)

res = eval.calc(x , y , op)

err = choice([-1 , 0 , 1])

display_res = res + err

print("*" * 20)
print("{0} {1} {2} = {3}".format(x , op , y , display_res))
print("*" * 20)

u_choice = input("Y/N? ").upper()

if err == 0:
    if u_choice == "Y":
        print("Yay")
    elif u_choice == "N":
        print("You're wrong")
else:
    if u_choice == "Y":
        print("You're wrong")
    elif u_choice == "N":
        print("Yay")