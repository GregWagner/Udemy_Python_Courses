import time
from time import perf_counter as my_timer
# use process_time to measure CPU time
import random

input('Press enter to start')
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input('Press enter end')
end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print(f"Your reaction time was {end_time - start_time} seconds")
