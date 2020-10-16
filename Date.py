# get date
from datetime import date
d = date(2013, 8, 22)
print(d.year)
print(d.month)
print(d.day)
print(d.strftime("%Y %m %d"))


# get time
from datetime import time
t = time(11, 16, 45)
print(t.hour)
print(t.minute)
print(t.second)
print(t.strftime("%H: %M: %S:"))

from datetime import datetime, timedelta
dt = datetime(2020, 10, 16, 11, 21, 40)
# get datetime after 5 days
add_dt = dt + timedelta(days=5)
print(add_dt.strftime("%m-%d-%Y %H: %M: %S:"))

# get datetime 5 days in past
sud_dt = dt - timedelta(days=5)
print(sud_dt.strftime("%m-%d-%Y %H: %M: %S:"))

# get 14 dates difference is a week(14 days)
# Looping while
from datetime import datetime, timedelta
dt = datetime(2020, 10, 16, 11, 21, 40)
Y = 0
while Y < 10:
    print(dt)
    dt = dt + timedelta(days=14)
    Y = Y + 1
