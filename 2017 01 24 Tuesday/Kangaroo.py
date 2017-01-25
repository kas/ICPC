# PASSES 1 OUT OF 2 TEST CASES

import sys

x1,v1,x2,v2 = input().strip().split(' ')
x1,speed_one,x2,speed_two = [int(x1),int(v1),int(x2),int(v2)]

pos_one = []
pos_two = []

meet = False

for x_one in range(x1, 10001):
    pos_one.append(x_one)
    x_one += speed_one

for x_two in range(x2, 10001):
    pos_two.append(x_two)
    x_two += speed_two

if (len(pos_one) < len(pos_two)):
    upper_range = len(pos_one)
else:
    upper_range = len(pos_two)

for idx in range(0, upper_range):
    if (pos_one[idx] == pos_two[idx]):
        meet = True
        break

if meet:
    print('YES')
else:
    print('NO')
