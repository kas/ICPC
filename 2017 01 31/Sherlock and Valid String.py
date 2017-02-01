stdin = input()

substr = None

substrs = []
numbers = []

for i in range(0, (len(stdin) - 1)):
    char = stdin[i]

    if substr:
        if (char == substr[0]):
            substr += char
        else:
            substrs.append(substr)
            substr = char
    else:
        substr = char

    if (i == (len(stdin) - 2)):
        substr += stdin[i+1]
        substrs.append(substr)

for substr in substrs:
    numbers.append(len(substr))

past_numbers = []

chances = 1

for i in range(0, (len(numbers) - 1)):
    if past_numbers:
        for past_number in past_numbers:
            if (numbers[i] > past_number):
                if (chances > 0):
                    print('subtract 1')
                    chances -= 1
                    numbers[i] -= 1
                    past_numbers.append(numbers[i])
                else:
                    print('NO')
    else:
        past_numbers.append(numbers[i])
        if (numbers[i+1] > numbers[i]):
            if (chances > 0):
                chances -= 1
                numbers[i+1] -= 1

if (chances >= 0):
    print('YES')
