from pygaze import libscreen, eyetracker
import time
import argparse
import csv
import matplotlib.pyplot as plt
from numpy import mean, std

parser = argparse.ArgumentParser(description='A small test for pygaze using tobii eyetracker')
parser.add_argument('-c', '--no_calibrate', default=False, action='store_true', help='skip calibration')
parser.add_argument('-d', '--no_data', default=False, action='store_true', help='skip data acquisition')
args = parser.parse_args()

if not args.no_data:
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

print('##################\n# analyzing data #\n##################')

tsv_list = []
with open('default_TOBII_output.tsv', 'rb') as tsv_file:
    tsv_in = csv.reader(tsv_file, delimiter='\t')
    for row in tsv_in:
        tsv_list.append(row)

data_list = []
time_list = []
if args.no_calibrate:
    data_start = 8
else:
    data_start = 18
for row in tsv_list[data_start:]:
    time = float(row[0])
    if time_list:
        data_list.append(time-time_list[-1])
    time_list.append(time)

time_mean = mean(data_list)
time_std = std(data_list)
print('mean of time difference: '+str(time_mean))
print('standard diviation of time difference: '+str(time_std))

plt.plot(time_list[1:], data_list, label='durian')
plt.xlabel('Experiment time (ms)')
plt.ylabel('Time difference (ms)')
plt.grid(True)

plt.savefig('plot_time_diffence')
plt.show()
