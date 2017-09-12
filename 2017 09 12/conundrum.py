input_string = input()

days = 0

per = ['P', 'E', 'R']
i = 0

for j in range(0, len(input_string)):
    if input_string[j] != per[i]:
        days += 1

    i += 1
    if i > (len(per) - 1):
        i = 0

print(days)

