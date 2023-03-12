# Task: Write a function that takes an integer - number. The function must return 'yes' if number is a power of 2,
# otherwise 'no'. It is forbidden to use the exponentiation function or operator.

def number_check(a: float):
    if a == 2:
        return 'Yes'
    elif a != 2 and a > 2:
        pass
        return number_check(a / 2)
    else:
        return 'No'


print(number_check(12))
