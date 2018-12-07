entries = sorted(open("day4.input", "r").read().rstrip().split("\n"))

sleep_totals = {}
minute_count = {}

cur_guard = -1
last_time = 0
for entry in entries:
    day = entry[1:11]
    words = entry.split(" ")
    if words[2] == "Guard":
        cur_guard = words[3]
        if cur_guard not in minute_count:
            minute_count[cur_guard] = [0 for m in range(0, 60)]
        if cur_guard not in sleep_totals:
            sleep_totals[cur_guard] = 0
    elif words[2] == "falls":
        last_time = int(words[1][3:5])
    elif words[2] == "wakes":
        sleep_totals[cur_guard] += int(words[1][3:5]) - last_time
        for t in range(last_time, int(words[1][3:5])):
            minute_count[cur_guard][t] += 1

sleepiest_guard = list(sleep_totals.keys())[list(sleep_totals.values()).index(max(list(sleep_totals.values())))]
sleepiest_minute = minute_count[sleepiest_guard].index(max(minute_count[sleepiest_guard]))

print int(sleepiest_guard[1:]) * sleepiest_minute
