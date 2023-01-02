# Triangle №1
n = int(input('Enter width triangle:'))
i = '*'
if n > len(i):
    while n >= len(i):
        print(n * '*')
        n -= 1
else:
    print('Incorrect value')

# Triangle №2
n = int(input('Enter width triangle:'))
z = '*'
if z < n * '*':
    while z <= n * '*':
        print(z)
        z += '*'
else:
    print('Incorrect value')

# Triangle №3
n = int(input('Enter width triangle:'))
i = '*'
s = ""
if n > len(i):
    while n >= len(i):
        print(s + (n * '*'))
        n -= 1
        s += ' '
else:
    print('Incorrect value')

# Triangle №4
n = int(input('Enter width triangle:'))
i = '*'
b = n
if n > len(i):
    while n >= len(i):
        b -= 1
        print(b * ' ' + i)
        i += '*'
