def remove_dollar_sign(s):
    new_str = s.replace("$","")
    return new_str

result = remove_dollar_sign("$$$$KAK$$AKA$$$$")

print(result)