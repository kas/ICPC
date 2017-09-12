input_string = input()

input_list = input_string.split()

hours = int(input_list[0])
minutes = int(input_list[1])

output_hours = None
output_minutes = None

difference = minutes - 45

if difference < 0:
    # subtract 1 from hours
    additional_subtraction = abs(difference)

    output_minutes = 60 - additional_subtraction

    output_hours = hours - 1

    if output_hours < 0:
        output_hours = 24 + output_hours
else:
    output_hours = hours
    output_minutes = difference

print('{} {}'.format(output_hours, output_minutes))

