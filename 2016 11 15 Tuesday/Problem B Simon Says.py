import itertools

output = []

x = input()

for _ in itertools.repeat(None, int(x)):
    line = input()
    if "Simon says " in line:
        output.append(line[10:])

for line in output:
    print(line)
