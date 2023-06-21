def reverse_key(**kwargs):
    temp = {}
    for key, value in kwargs.items():
        if not isinstance(value, str):
            value = str(value)
        temp[value] = key
    return temp


print(reverse_key(asd=[150, 500, -200], abc=[150, 500, -200], cab=[850, 500, -200]))
