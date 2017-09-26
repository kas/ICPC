import sys

capacity = None
stops = None

count = 0
passengers = 0

failed = False


for line in sys.stdin:
    line = line.split()

    if not capacity and not stops:
        capacity = int(line[0])
        stops = int(line[1])
        continue

    count += 1

    off = int(line[0])
    on = int(line[1])
    waiting = int(line[2])

    # if (count == 1) and (off > 0):
        # failed = True
        # print('impossible')
        # break

    passengers -= off
    passengers += on

    if (passengers > capacity) or (passengers < 0) or (waiting > 0):
        failed = True
        print('impossible')
        break

    if count == stops:
        if passengers != 0:
            failed = True
            print('impossible')
        break

if not failed:
    print('possible')
