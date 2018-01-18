from pygaze import libscreen, eyetracker
import time
import argparse

parser = argparse.ArgumentParser(description='A small test for pygaze using tobii eyetracker')
parser.add_argument('-c', '--no_calibrate', default=False, action='store_true', help='skip calibration')
args = parser.parse_args()

display = libscreen.Display()
screen = libscreen.Screen()
eyetracker = eyetracker.EyeTracker(display)
screen.draw_text(text='this is just a test')
display.fill(screen)
display.show()

time.sleep(2)

if not args.no_calibrate:
    eyetracker.calibrate()

display.close()
