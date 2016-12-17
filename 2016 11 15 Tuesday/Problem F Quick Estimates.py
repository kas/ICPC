import itertools

output = []

x = input()

for _ in itertools.repeat(None, int(x)):
    line = input()
    output.append(len(line))

for line in output:
    print(line)
