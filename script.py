import time
import sys

seconds = int(sys.argv[1])

def time_waster():
    time.sleep(seconds)
    print("Done waiting %ss" % seconds)

time_waster()
sys.exit(1)
