import time

def time_waster(s):
    time.sleep(s)
    print("Done waiting %ss" % s)

time_waster(5)
