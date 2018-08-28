import os
import subprocess


counter = 0
fd_out = '/media/pi/02F0-F0FD1/'

while True:
    fout = fd_out + 'fly_tracker_1280_960_' + str(counter) +  '.h264'
    print('save: ' + fout)
    cmd = 'raspivid -t 60000 -w 1280 -h 960 -fps 30 -ex auto -rf gray -b 1200000 -p 200,200,1280,960 -o ' + fout

    os.system(cmd)
    counter = counter + 1