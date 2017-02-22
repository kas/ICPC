# password

from decimal import *

getcontext().prec = 6

def calculate_attempts(passwords):
    attempts = 0

    for x in range(1, (len(passwords) + 1)):
        # print('{}*{}'.format(passwords[x - 1], x))
        attempts += Decimal(passwords[x - 1]) * Decimal(x)

    return attempts

passwords = []
num_passwords = input()
for x in range(0, int(num_passwords)):
    passwords.append(float(input().split()[1]))

print(str(calculate_attempts(passwords)))