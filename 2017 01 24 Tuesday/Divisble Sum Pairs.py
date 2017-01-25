first = input().split()
second = input().split()

n = first[0]
k = first[1]

num = 0

for first_idx, first_num in enumerate(second):
    for second_idx, second_num in enumerate(second):
        if (first_idx < second_idx):
            if (((first_num + second_num) % k) == 0):
                num += 1
