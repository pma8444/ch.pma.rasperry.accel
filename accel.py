import datetime
import time


while True:
    with open("accel.dat","a+") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    time.sleep(30)
