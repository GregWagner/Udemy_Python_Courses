import time
import datetime

print("The epoch on this system starts at " + time.strftime("%c", time.gmtime(0)))
print("The current timezone is {} with an offset of {}".format(time.tzname[0],
                                                               time.timezone))
if time.daylight != 0:
    print("\tDaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])    # only if daylight = 1
else:
    print("\tThe non DST timezone is " + time.tzname[0])

print("Local time is: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("UTC time is:   " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

print('-' * 50)
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
