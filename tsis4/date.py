#Write a Python program to subtract five days from current date.

import datetime

from datetime import date

tod = date.today()
tod  = tod.replace(day = tod.day -5)
print (tod) 



#Write a Python program to print yesterday, today, tomorrow.
import datetime

from datetime import date

tod = date.today()
yes  = tod.replace(day = tod.day -1)
tom = tod.replace(day = tod.day +1)
print (yes , tod , tom)

#Write a Python program to drop microseconds from datetime.

import datetime

with_microseconds = datetime.datetime.now()
without_microseconds = with_microseconds.replace(microsecond=0)
print(without_microseconds)

#Write a Python program to calculate two date difference in seconds.
import datetime

newtime= datetime.datetime.today()
oldtime = datetime.datetime(2020, 1, 26)
diff = newtime - oldtime
print(diff.total_seconds())