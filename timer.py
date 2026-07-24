import math
import time

hour = input("How long should your timer be in hours?(next will ask minutes) - ")
min = input("How long should your timer be in minutes?(next will ask seconds) - ")
sec = input("How long should your timer be in seconds? - ")

hour = int(hour)
min = int(min)
sec = int(sec)

hour = (hour * 60) * 60
min = min * 60

timer = hour + min + sec

while timer>0:
    hour1 = timer//3600
    min1 = (timer%3600)//60
    sec1 = timer%60
    print(f"\rHow many seconds left --> {hour1:02}:{min1:02}:{sec1:02}", end="")
    time.sleep(1)
    timer -= 1
print("\nTime is up!")
