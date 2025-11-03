#!/bin/python3
import subprocess
import sys

pid = 0
searchid = sys.argv[1]
windows = subprocess.check_output(["hyprctl","clients"],text=True).split("\n\n")
for i in windows :
    i = i.split('\n')
    if searchid in i[0]:
        for j in i :
            if "pid" in j :
                pid = int(j.split(':')[1])
                break
        break
if pid :
    print(pid)
    subprocess.run(["hyprctl", "dispatch", "focuswindow", "pid:"+str(pid)])
    sys.exit(0)
else :
    sys.exit(1)
