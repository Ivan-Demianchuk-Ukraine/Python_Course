import datetime


start_date = datetime.date(2022, 10, 17)
class_time = datetime.time(19, 15)
num_lectures = 32

lecture_dates = []
current_date = start_date
while len(lecture_dates) < num_lectures:
    if current_date.weekday() == 0 or current_date.weekday() == 3:
        lecture_dates.append(current_date)
    current_date += datetime.timedelta(days=1)

for i, lecture_date in enumerate(lecture_dates):
    lecture_time = datetime.datetime.combine(lecture_date, class_time)
    print(f"Lecture {i+1:2d}: {lecture_date.strftime('%d %b %Y')} {lecture_time.strftime('%H:%M')}")
