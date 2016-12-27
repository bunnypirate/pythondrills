#####
# PyDrill_Datetime_27_idle version2
#

from datetime import datetime, timedelta
# below requires pip install pytz from command line
from pytz import timezone
import pytz

def open_or_closed(time): 
    if ((time.hour >= 9 and time.minute >= 0) and (time.hour < 21)) :
       return 'OPEN'
    else :
        if (time.hour == 21 and time.minute == 0) :
            return 'OPEN'
        else :
            return 'CLOSED'

def getTime(time_zone):
    local_timezone = timezone('US/Pacific')
    local_datetime = datetime.now(local_timezone)

    converted_time = local_datetime.astimezone(time_zone) 
    return converted_time
    
def printInfo(branches):
    print ("Branch")
    print ("--------------------------------------------------------------")
    for b in sorted (branches):
        print (b + '\t' + branches[b])

def main():

    #Timezones of branches
    portland_timezone = timezone('US/Pacific')
    nyc_timezone = timezone('US/Eastern')
    london_timezone = timezone ('Europe/London')

    format = '%Y-%m-%d %H:%M:%S %Z%z'

    #Dictionary of Branches
    branches = {
        '1. Portland     HQ : ' : getTime(portland_timezone).strftime(format) + '\t' + open_or_closed(getTime(portland_timezone)),
        '2. NYC      Branch : ' : getTime(nyc_timezone).strftime(format) + '\t' + open_or_closed(getTime(nyc_timezone)),
        '3. London   Branch : ' : getTime(london_timezone).strftime(format) + '\t' + open_or_closed(getTime(london_timezone))
        }
    printInfo (branches)

main()
