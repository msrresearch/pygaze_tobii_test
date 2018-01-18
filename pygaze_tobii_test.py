from pygaze import libscreen, eyetracker
import time
import argparse
import csv

parser = argparse.ArgumentParser(description='A small test for pygaze using tobii eyetracker')
parser.add_argument('-c', '--no_calibrate', default=False, action='store_true', help='skip calibration')
args = parser.parse_args()

display = libscreen.Display()
screen = libscreen.Screen()
eyetracker = eyetracker.EyeTracker(display)

if not args.no_calibrate:
    eyetracker.calibrate()

eyetracker.start_recording()

for i in range (60, 0, -1):
    screen = libscreen.Screen()
    screen.draw_text('Recording data for {} seconds'.format(i))
    display.fill(screen)
    display.show()
    time.sleep(1)

eyetracker.stop_recording()

display.close()
