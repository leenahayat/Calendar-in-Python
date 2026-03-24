#calendar

import calendar

year = 2026

# Create a TextCalendar object, starting the week on Sunday (0=Monday, 6=Sunday)
cal = calendar.TextCalendar(calendar.SUNDAY)


# w=2 (width of each day column)
# l=1 (lines per week)
# c=6 (spaces between month columns)
# m=3 (months per row)
yearly_calendar = cal.formatyear(year, w=2, l=2, c=6, m=3)


print(yearly_calendar)



# import calendar
# yy = 2026
# mm = 1
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 2
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 3
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 4
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 5
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 6
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 7
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 8
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 9
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 10
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 11
# print(calendar.month(yy, mm))

# import calendar
# yy = 2026
# mm = 12
# print(calendar.month(yy, mm))




