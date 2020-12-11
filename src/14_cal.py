"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

x = input("Enter mm/yyyy: ")


def cal():
    global x
    if x == "":
        today = datetime.today()
        print(f"{today.month}/{today.year} ")
    if len(x) == 2 and int(x) >= 1 and int(x) <= 12:
        year = datetime.now().year
        print(calendar.month(year, int(x)))
    if len(x) == 7 and x[2] == "/":
        month = int(x[:2])
        year = int(x[3:])

        if month >= 1 and month <= 12:
            print(calendar.month(year, month))
    else:
        print("Please enter a corect format. MM/YYYY")


cal()
