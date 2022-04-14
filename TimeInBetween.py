#GIVE TWO TIMES AND TELLS U THE TIME IN BETWEEN
from datetime import datetime
import datetime

#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

print("Give me two times, and I'll tell you the time in between. Don't mind the order.")

FMT = "%H:%M:%S"

time1 = input("Format H:M:S -> ")
time2 = input("Format H:M:S -> ")

datetime1 = datetime.datetime.strptime(time1,FMT)
datetime2 = datetime.datetime.strptime(time2,FMT)

if datetime1 > datetime2:
    time_difference = datetime1 - datetime2
    print(time_difference)
elif datetime2 > datetime1:
    time_difference = datetime2 - datetime1
    print(time_difference)
else:
    print("Datetime sets are the same :)")