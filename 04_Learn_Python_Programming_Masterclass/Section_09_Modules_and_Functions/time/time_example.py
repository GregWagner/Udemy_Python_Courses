import time

print(time.gmtime(0))       # epouch time
print(time.localtime())     # current local time
print(time.time())          # seconds since epouch

# time_here will be a named tuple
time_here = time.localtime()
print(time_here)

# 2 different ways to access the different fields in a time
print("Year: ", time_here[0], time_here.tm_year)
print("Month: ", time_here[1], time_here.tm_mon)
print("Day: ", time_here[2], time_here.tm_mday)
