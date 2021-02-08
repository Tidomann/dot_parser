import re
import os
import time

'''User Notes -> Requires Python 3x

Will clear log file everytime it is run, this will interrupt a parser if running.
Comment out the f.truncate below for it to not clear log

Change log_file_path below to your eq base directory so it can find your log.

'''


_dir = os.getcwd()
_char_name = 'Burrito'


log_file_path = 'D:\\Program Files (x86)\\Everquest Classless\\Logs\\eqlog_Burrito_classless.txt'
f = open(log_file_path, 'r+')


# Commend out this if you don't want it to clear log
f.truncate(0)

# constants, don't change


d = {}
avgd = {}

while True:
    try:

        # Don't change this block
        line = ''
        while len(line) == 0 or line[-1] != '\n':
            tail = f.readline()
            if tail == '':
                time.sleep(0.1)
                continue
            line += tail

        if "damage from your" in line:
            dot = re.search(r'(?<=from your ).*$', line)
            dmg = re.search(r'[0-9]{3,9}\s', line)

            dot = dot.group(0)
            dmg = dmg.group(0)

            if dot not in d.keys():
                d[dot] = [int(dmg)]

            if dot in d.keys():
                d[dot].append(int(dmg))

            for x, y in d.items():
                z = 0
                # sum of values
                for n in y:
                    z += n
                # average
                avg = round(z / len(y), 0)
                # add to dict format [avg, numticks parses]
                avgd[x] = [avg, len(y)]

            print(avgd)

    except Exception as e:
        print("Something Failed")
        print(e)
        break
        pass
