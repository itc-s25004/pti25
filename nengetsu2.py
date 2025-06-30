print("今日は何年？")
year = int(input())
print("今日は何月？")
mon = int(input())

import calendar
print(calendar.month(year,mon))
