import datetime as dt
data1, data2 = input().split()
data3 = input()
rapid = int(input())
trebofania = int(input())
rezylt = []
day, month, year = data1.split('-')
d_start = dt.date(int(year), int(month), int(day))  # начало каникул
day, month, year = data2.split('-')
d_end = dt.date(int(year), int(month), int(day))  # конец каникул
day, month, year = data3.split('-')
maximum = dt.date(int(year), int(month), int(day))  # День максимальной активности

y_format = "%b/%m/%Y"
d_next = maximum + dt.timedelta(days=rapid)  # берём следующую дату после даты после даты с максимельной активности
weekends = [5, 6]
while len(rezylt) < trebofania:
    if (d_start < d_next < d_end) or d_next.weekday() in weekends:
        print(d_next.strftime(y_format))
        rezylt.append(d_next)
    d_next = d_next + dt.timedelta(days=rapid)
