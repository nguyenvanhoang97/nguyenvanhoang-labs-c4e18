from random import choice

def calc(x , y , op):
    # x = 3
    # y = 7
    # op = choice(["+" , "-" , "*" , "/"])

    res = 0

    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y
    elif op == "/":
        res = x / y
    
    return res
    # print(result)

result = calc(1 , 2 , "+")
print(result)