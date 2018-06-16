def is_inside(point , hcn):

    a = hcn[0] + hcn[2]
    b = hcn[1] + hcn[3]

    if hcn[0] <= point[0] <= a and hcn[1] <= point[1] <= b:
        print("inside")
        return True

po = [200 , 120]
hinh = [140, 60, 100, 200]

result = is_inside(po , hinh)

print(result)