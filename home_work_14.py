from datetime import timedelta

import datetime
t_year = timedelta()
t1 = timedelta(days=3)
t2 = timedelta(days=4)
c = datetime.datetime(2022, 10, 17, 19, 15)
count = 1
print('Lecture  1: ', c)
for i in range(16):
    if count < 9:
        count += 1
        c = c + t1
        print(f'Lecture  {count}: ', c)
        count += 1
        c = c + t2
        print(f'Lecture  {count}: ', c)
    else:
        count += 1
        c = c + t1
        print(f'Lecture {count}: ', c)
        count += 1
        c = c + t2
        if count == 33:
            pass
        else:
            print(f'Lecture {count}: ', c)
