# Exercise 1:
# The user enters a word, if this word is a polyndrom, then output '+', otherwise '-'
a = str(input('Your Word: '))
if a == a[::-1]:
    print('+')
else:
    print('-')

# Task 2:
# The user enters the text and the word to be found, if this word is in the text, output 'YES', otherwise 'NO'
a, b = str(input('Your Text: ')), str(input('Your Word: '))
if b in a:
    print('YES')
else:
    print('NO')

# Task 3:
# The user enters a string. If it starts with 'abc', then replace them with 'www', otherwise add 'zzz' to the end of
# the string.
a = str(input('Your Word: '))
if a[0:3:1] == 'abc':
    a = a.replace(a[0:3:1], 'www', 1)
else:
    a = a + 'zzz'
print(a)

# Task 4:
# The user enters text, remove all numbers in the text, and output a string to the user.
a, b = str(input('Your Word: ')), ''
for i in a:
    if i.isalpha() or i.isspace():
        b += i
    else:
        pass
print('Result: ' + b)

# Task 5:
# Write a validator for mail. The user enters the mail, and the program must check that the mail contains the character
# '@' and '.', and if so, then print "YES", otherwise "NO"a = str(input('Your Mail: '))
if '@' in a and "." in a:
    print('YES')
else:
    print('NO')
