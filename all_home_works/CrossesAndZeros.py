import sys

a = ['1', '2', '3']
b = ['4', '5', '6']
c = ['7', '8', '9']


def validation():
    if a == ['x', 'x', 'x']:
        print('X-player Won!!!')
        sys.exit()
    if a == ['0', '0', '0']:
        print('0-player Won!!!')
        sys.exit()
    if b == ['x', 'x', 'x']:
        print('X-player Won!!!')
        sys.exit()
    if b == ['0', '0', '0']:
        print('0-player Won!!!')
        sys.exit()
    if c == ['x', 'x', 'x']:
        print('X-player Won!!!')
        sys.exit()
    if c == ['0', '0', '0']:
        print('0-player Won!!!')
        sys.exit()
    if a[0] == 'x' and b[0] == 'x' and c[0] == 'x':
        print('X-player Won!!!')
        sys.exit()
    if a[0] == '0' and b[0] == '0' and c[0] == '0':
        print('0-player Won!!!')
        sys.exit()
    if a[1] == 'x' and b[1] == 'x' and c[1] == 'x':
        print('X-player Won!!!')
        sys.exit()
    if a[1] == '0' and b[1] == '0' and c[1] == '0':
        print('0-player Won!!!')
        sys.exit()
    if a[2] == 'x' and b[2] == 'x' and c[2] == 'x':
        print('X-player Won!!!')
        sys.exit()
    if a[2] == '0' and b[2] == '0' and c[2] == '0':
        print('0-player Won!!!')
        sys.exit()
    if a[0] == 'x' and b[1] == 'x' and c[2] == 'x':
        print('X-player Won!!!')
        sys.exit()
    if a[0] == '0' and b[1] == '0' and c[2] == '0':
        print('0-player Won!!!')
        sys.exit()
    if a[2] == 'x' and b[1] == 'x' and c[0] == 'x':
        print('X-player Won!!!')
        sys.exit()
    if a[2] == '0' and b[1] == '0' and c[0] == '0':
        print('0-player Won!!!')
        sys.exit()


d = str(input('Please enter your value(1-9):'))
answers = []
if d == '1':
    answers.append(d)
    a[0] = 'x'
elif d == '2':
    answers.append(d)
    a[1] = 'x'
elif d == '3':
    answers.append(d)
    a[2] = 'x'
elif d == '4':
    answers.append(d)
    b[0] = 'x'
elif d == '5':
    answers.append(d)
    b[1] = 'x'
elif d == '6':
    answers.append(d)
    b[2] = 'x'
elif d == '7':
    answers.append(d)
    c[0] = 'x'
elif d == '8':
    answers.append(d)
    c[1] = 'x'
elif d == '9':
    answers.append(d)
    c[2] = 'x'

print(*a)
print(*b)
print(*c)

d = str(input('Please enter your value(1-9):'))
if d == '1' and d not in answers:
    answers.append(d)
    a[0] = '0'
elif d == '2' and d not in answers:
    answers.append(d)
    a[1] = '0'
elif d == '3' and d not in answers:
    answers.append(d)
    a[2] = '0'
elif d == '4' and d not in answers:
    answers.append(d)
    b[0] = '0'
elif d == '5' and d not in answers:
    answers.append(d)
    b[1] = '0'
elif d == '6' and d not in answers:
    answers.append(d)
    b[2] = '0'
elif d == '7' and d not in answers:
    answers.append(d)
    c[0] = '0'
elif d == '8' and d not in answers:
    answers.append(d)
    c[1] = '0'
elif d == '9' and d not in answers:
    answers.append(d)
    c[2] = '0'
else:
    print('Incorrect value. Start game again please.')
    sys.exit()
print(*a)
print(*b)
print(*c)

d = str(input('Please enter your value(1-9):'))
if d == '1' and d not in answers:
    answers.append(d)
    a[0] = 'x'
elif d == '2' and d not in answers:
    answers.append(d)
    a[1] = 'x'
elif d == '3' and d not in answers:
    answers.append(d)
    a[2] = 'x'
elif d == '4' and d not in answers:
    answers.append(d)
    b[0] = 'x'
elif d == '5' and d not in answers:
    answers.append(d)
    b[1] = 'x'
elif d == '6' and d not in answers:
    answers.append(d)
    b[2] = 'x'
elif d == '7' and d not in answers:
    answers.append(d)
    c[0] = 'x'
elif d == '8' and d not in answers:
    answers.append(d)
    c[1] = 'x'
elif d == '9' and d not in answers:
    answers.append(d)
    c[2] = 'x'
else:
    print('Incorrect value. Start game again please.')
    sys.exit()
print(*a)
print(*b)
print(*c)


d = str(input('Please enter your value(1-9):'))
if d == '1' and d not in answers:
    answers.append(d)
    a[0] = '0'
elif d == '2' and d not in answers:
    answers.append(d)
    a[1] = '0'
elif d == '3' and d not in answers:
    answers.append(d)
    a[2] = '0'
elif d == '4' and d not in answers:
    answers.append(d)
    b[0] = '0'
elif d == '5' and d not in answers:
    answers.append(d)
    b[1] = '0'
elif d == '6' and d not in answers:
    answers.append(d)
    b[2] = '0'
elif d == '7' and d not in answers:
    answers.append(d)
    c[0] = '0'
elif d == '8' and d not in answers:
    answers.append(d)
    c[1] = '0'
elif d == '9' and d not in answers:
    answers.append(d)
    c[2] = '0'
else:
    print('Incorrect value. Start game again please.')
    sys.exit()
print(*a)
print(*b)
print(*c)

d = str(input('Please enter your value(1-9):'))
if d == '1' and d not in answers:
    answers.append(d)
    a[0] = 'x'
elif d == '2' and d not in answers:
    answers.append(d)
    a[1] = 'x'
elif d == '3' and d not in answers:
    answers.append(d)
    a[2] = 'x'
elif d == '4' and d not in answers:
    answers.append(d)
    b[0] = 'x'
elif d == '5' and d not in answers:
    answers.append(d)
    b[1] = 'x'
elif d == '6' and d not in answers:
    answers.append(d)
    b[2] = 'x'
elif d == '7' and d not in answers:
    answers.append(d)
    c[0] = 'x'
elif d == '8' and d not in answers:
    answers.append(d)
    c[1] = 'x'
elif d == '9' and d not in answers:
    answers.append(d)
    c[2] = 'x'
else:
    print('Incorrect value. Start game again please.')
    sys.exit()
print(*a)
print(*b)
print(*c)
validation()

d = str(input('Please enter your value(1-9):'))
if d == '1' and d not in answers:
    answers.append(d)
    a[0] = '0'
elif d == '2' and d not in answers:
    answers.append(d)
    a[1] = '0'
elif d == '3' and d not in answers:
    answers.append(d)
    a[2] = '0'
elif d == '4' and d not in answers:
    answers.append(d)
    b[0] = '0'
elif d == '5' and d not in answers:
    answers.append(d)
    b[1] = '0'
elif d == '6' and d not in answers:
    answers.append(d)
    b[2] = '0'
elif d == '7' and d not in answers:
    answers.append(d)
    c[0] = '0'
elif d == '8' and d not in answers:
    answers.append(d)
    c[1] = '0'
elif d == '9' and d not in answers:
    answers.append(d)
    c[2] = '0'
else:
    print('Incorrect value. Start game again please.')
    sys.exit()
print(*a)
print(*b)
print(*c)
validation()

d = str(input('Please enter your value(1-9):'))
if d == '1' and d not in answers:
    answers.append(d)
    a[0] = 'x'
elif d == '2' and d not in answers:
    answers.append(d)
    a[1] = 'x'
elif d == '3' and d not in answers:
    answers.append(d)
    a[2] = 'x'
elif d == '4' and d not in answers:
    answers.append(d)
    b[0] = 'x'
elif d == '5' and d not in answers:
    answers.append(d)
    b[1] = 'x'
elif d == '6' and d not in answers:
    answers.append(d)
    b[2] = 'x'
elif d == '7' and d not in answers:
    answers.append(d)
    c[0] = 'x'
elif d == '8' and d not in answers:
    answers.append(d)
    c[1] = 'x'
elif d == '9' and d not in answers:
    answers.append(d)
    c[2] = 'x'
else:
    print('Incorrect value. Start game again please.')
    sys.exit()
print(*a)
print(*b)
print(*c)
validation()

d = str(input('Please enter your value(1-9):'))
if d == '1' and d not in answers:
    answers.append(d)
    a[0] = '0'
elif d == '2' and d not in answers:
    answers.append(d)
    a[1] = '0'
elif d == '3' and d not in answers:
    answers.append(d)
    a[2] = '0'
elif d == '4' and d not in answers:
    answers.append(d)
    b[0] = '0'
elif d == '5' and d not in answers:
    answers.append(d)
    b[1] = '0'
elif d == '6' and d not in answers:
    answers.append(d)
    b[2] = '0'
elif d == '7' and d not in answers:
    answers.append(d)
    c[0] = '0'
elif d == '8' and d not in answers:
    answers.append(d)
    c[1] = '0'
elif d == '9' and d not in answers:
    answers.append(d)
    c[2] = '0'
else:
    print('Incorrect value. Start game again please.')
    sys.exit()
print(*a)
print(*b)
print(*c)
validation()

d = str(input('Please enter your value(1-9):'))
if d == '1' and d not in answers:
    answers.append(d)
    a[0] = 'x'
elif d == '2' and d not in answers:
    answers.append(d)
    a[1] = 'x'
elif d == '3' and d not in answers:
    answers.append(d)
    a[2] = 'x'
elif d == '4' and d not in answers:
    answers.append(d)
    b[0] = 'x'
elif d == '5' and d not in answers:
    answers.append(d)
    b[1] = 'x'
elif d == '6' and d not in answers:
    answers.append(d)
    b[2] = 'x'
elif d == '7' and d not in answers:
    answers.append(d)
    c[0] = 'x'
elif d == '8' and d not in answers:
    answers.append(d)
    c[1] = 'x'
elif d == '9' and d not in answers:
    answers.append(d)
    c[2] = 'x'
else:
    print('Incorrect value. Start game again please.')
    sys.exit()
print(*a)
print(*b)
print(*c)
validation()
print('No winners! Love is won!')
