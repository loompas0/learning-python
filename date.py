# some methods towork with dates type
"""import datetime # to work with date import datetime module

birthDate :datetime.date

print (datetime.datetime.now()) # today date and time "a bit complex"
print (datetime.date.today()) # today date "a bit complex"
print (datetime.datetime.now().time()) # today time "very complex"
"""
# simpler way with today 

from datetime import date
from datetime import datetime

print (datetime.now())
print (datetime.now().time())
print (datetime.now().year)
print (datetime.now().day)
print (date.today())

# format a date day-month-year
print (date.today().strftime("%A the %dth of %B %Y"))
print (date.today().strftime("%a the %dth of %b %Y"))
print (datetime.now().strftime (" %d %m %Y , %H h %M min %S seconds"))
