import math
import time

hour = input("How long should your timer be in hours?")
min = input("How long should your timer be in minutes?")
sec = input("How long should your timer be in seconds?")

hour = int(hour)
min = int(min)
sec = int(sec)

hour = (hour * 60) * 60
min = min * 60

timer = hour + min + sec

for i in range(timer):
    time.sleep(1)
    timer = timer - 1
    print(f"This many seconds left, {timer}")
    if sec == 0:
        print("Time is up!")