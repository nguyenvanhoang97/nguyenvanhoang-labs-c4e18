def get_even_list(list_numb):
    day_c = []
    for i in range(len(list_numb)):
        if list_numb[i] % 2 == 0:
            day_c.append(list_numb[i])
    return day_c

lis = [1 , 4 , 5 , -1 , 10]

result = get_even_list(lis)

print(result)