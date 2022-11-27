def number_check(a: float):
    if a == 2:
        return 'Yes'
    elif a != 2 and a > 2:
        pass
        return number_check(a / 2)
    else:
        return 'No'


print(number_check(64))
