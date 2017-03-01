def validate(n, a, b):
    successful = False

    if (int(n) % 2) == 0:
        if a == b:
            successful = True
    else:
        new = ''

        for d_c in a: # digit_char in string a
            if d_c == '0':
                new += '1'
            else:
                new += '0'
        
        if new == b:
            successful = True

    if successful:
        return 'Deletion succeeded'
    else:
        return 'Deletion failed'

n = input()
a = input()
b = input()

print(validate(n, a, b))