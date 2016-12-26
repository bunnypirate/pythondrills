#####
# Python 2.7
# Author: Renee Woznick
#
# PyDrill_Datetime_27_idle
#
# below requires pip install pytz from command line

from datetime import datetime, timedelta
# below requires pip install pytz from command line
from pytz import timezone
import pytz

pacific = timezone('US/Pacific')
eastern = timezone('US/Eastern')
london = timezone ('Europe/London')

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

local_dt = datetime.now(pacific)
#Hardcoded time to test logic
#local_dt = pacific.localize(datetime(2016, 12, 24, 21, 1, 0, 0))

if ((local_dt.hour >= 9 and local_dt.minute >= 0) and (local_dt.hour < 21)) :
   print 'Portland HQ       Open  : ', local_dt.strftime(fmt)
else :
    if (local_dt.hour == 21 and local_dt.minute == 0) :
        print 'Portland HQ       Open  : ', local_dt.strftime(fmt)
    else :
        print 'Portland HQ       Closed: ', local_dt.strftime(fmt)
   
eastern_dt = local_dt.astimezone(eastern)
if ((eastern_dt.hour >= 9 and eastern_dt.minute >= 0) and (eastern_dt.hour < 21)) :
   print 'NYC      Branch   Open  : ', eastern_dt.strftime(fmt)
else :
    if (eastern_dt.hour == 21 and eastern_dt.minute == 0) :
        print 'NYC      Branch   Open  : ', eastern_dt.strftime(fmt)
    else :
        print 'NYC      Branch   Closed: ', eastern_dt.strftime(fmt)

london_dt = local_dt.astimezone(london)
if ((london_dt.hour >= 9 and london_dt.minute >= 0) and (london_dt.hour < 21)) :
   print 'London   Branch   Open  : ', london_dt.strftime(fmt)
else :
    if (london_dt.hour == 21 and london_dt.minute == 0) :
        print 'London   Branch   Open  : ', london_dt.strftime(fmt)
    else :
        print 'London   Branch   Closed: ', london_dt.strftime(fmt)
