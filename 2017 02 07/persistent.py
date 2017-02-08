# kattis, id: persistent

nums = []
out_nums = []

while True:
    num = input()
    if (int(num) == -1):
        break
    else:
        nums.append(int(num))

for num in nums:
    for x in range(10, 1000000):
        product = int(str(x)[0])
        for i, char_digit in enumerate(str(x)):
            if (i != 0):
                product = product * int(char_digit)
        if (product == num):
            out_nums.append(x)
            break
        elif (x == 1000000 - 1):
            print('nope')
            out_nums.append('There is no such number.')

for out_num in out_nums:
    print(out_num)
