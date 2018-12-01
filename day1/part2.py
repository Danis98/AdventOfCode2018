seq = [int(e) for e in open("day1.input", "r").read().split()]

seen = {}

freq = 0
seen[freq] = True

ind = 0
while True:
    freq += seq[ind%len(seq)]
    ind += 1
    if freq in seen:
        print freq
        break
    seen[freq] = True
