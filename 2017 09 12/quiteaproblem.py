while True:
    try:
        input_string = input()
    except EOFError:
        break

    if 'problem' in input_string.lower():
        print('yes')
    else:
        print('no')

