import datetime
from datetime import date
current_date = date.today()
current_year = int(current_date.strftime("%Y"))


def day():
  dayborn = int(input("Please enter the day (in numbers) you were born:\t"))
  while dayborn < 1 or dayborn > 31:
    print("The day you enter was outside of the allowed range")
    dayborn = int(input("Please enter the day (in numbers) you were born:\t"))
  return dayborn

def month():
  monthborn = int(input("Please enter the month (in numbers) you were born:\t"))
  while monthborn < 1 or monthborn > 12:
    print("The day you enter was outside of the allowed range")
    monthborn = int(input("Please enter the month (in numbers) you were born:\t"))
  return monthborn

def year():
  yearborn = int(input("Please enter the year (in numbers) you were born:\t"))
  while yearborn < 1850 or yearborn > current_year:
    print("The year you enter was outside of the allowed range\n(aren't you dead?)")
    yearborn = int(input("Please enter the year (in numbers) you were born:\t"))
  return yearborn

dayborn = day()
monthborn = month()
yearborn = year()

birthday = datetime.date(yearborn, monthborn, dayborn)
print(f"You were born on {birthday.strftime('%A')}")
