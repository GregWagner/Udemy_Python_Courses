import pytz
import datetime

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

for timezone in pytz.all_timezones:
    print(timezone)

print('=' * 50)

for x in sorted(pytz.country_names):
    print(f"{x}: {pytz.country_names[x]}")
    # not all countries have timezones defined
    if x in pytz.country_timezones:
        # some countries have multiple timezones
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t{}: {}".format(zone, local_time))
    else:
        print("\tNo time zone defined")
