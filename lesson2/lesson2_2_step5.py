import datetime


a = input()
b = input()

# a="2016 4 20"
# b="14"

year, month, day = a.split()

date = datetime.date(int(year), int(month), int(day))

date_new = date + datetime.timedelta(int(b))

# print(date_new.year, date_new.month, date_new.day)
print(date_new.strftime("%Y %-m %-d"))
