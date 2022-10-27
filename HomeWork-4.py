# Triangle №1
n = int(input('Enter width triangle:'))
i = '*'
while n >= len(i):
    print(n * '*')
    n -= 1

# Triangle №2
n = int(input('Enter width triangle:'))
z = '*'
while z <= n * '*':
    print(z)
    z += '*'

# Triangle №3
n = int(input('Enter width triangle:'))
i = '*'
s = ""
while n >= len(i):
    print(s + (n * '*'))
    n -= 1
    s += ' '

# Triangle №4
n = int(input('Enter width triangle:'))
i = '*'
b = n
while n >= len(i):
    b -= 1
    print(b * ' ' + i)
    i += '*'
