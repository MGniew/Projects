'''Alarm Clock - A simple clock where it plays a sound \
after X number of minutes/seconds or at a particular time.'''
import argparse
from datetime import datetime
import time
import os


class TimeException(Exception):
    pass


def alarm(hour, minute):

    dt1 = datetime.now()
    dt2 = dt1.replace(hour=hour, minute=minute)
    wait = (dt2 - dt1).total_seconds()

    if (wait < 0):
        dt2 = dt2.replace(day=dt2.day + 1)
        wait = (dt2 - dt1).total_seconds()

    print("alarm set to " + dt2.ctime())

    time.sleep(wait)

    print("ALARM!")
    os.system('play --no-show-progress --null \
               --channels 1 synth 0.5 sine 540; \
               sleep 0.5;' * 3)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('time', type=str)

    try:
        a = parser.parse_args().time.split(":")
        a = [int(x) for x in a]
        if (a[0] < 0 or a[0] > 23 or a[1] < 0 or a[1] > 59):
            raise TimeException
    except (ValueError, TimeException):
            print("Please type proper time")
            return

    alarm(a[0], a[1])


if __name__ == "__main__":
    main()
