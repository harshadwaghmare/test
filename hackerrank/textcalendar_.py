import calendar

#print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

days = {0 : 'MONDAY', 1 : 'TUESDAY', 2 : 'WEDNESDAY', 3 : 'THURSDAY', 
        4 : 'FRIDAY', 5 : 'SATURDAY', 6 : 'SUNDAY'}

dd1 = input()

dd = dd1.split()

print(days[calendar.weekday(int(dd[2]),int(dd[0]),int(dd[1]))])
