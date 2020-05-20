import time

def time_waster(s):
    time.sleep(s)
    print("Done waiting %ss" % s)
    return "I've wasted %ss of your life!" % s

time_waster(5)
