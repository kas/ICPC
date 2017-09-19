import sys

total_test_cases = None
current_test_case = None

total_snowflakes = None
current_snowflake = None

encountered_snowflakes = set()

current_count = 0
longest_count = 0

for line in sys.stdin:
    if not total_test_cases:
        total_test_cases = int(line)
        current_test_case = 1

        continue

    if not total_snowflakes:
        total_snowflakes = int(line)
        current_snowflake = 1

        continue

    if current_snowflake >= total_snowflakes:
        total_snowflakes = None
        current_test_case += 1

        print(longest_count)

        continue

    if current_count > longest_count:
        longest_count = current_count

    if int(line) in encountered_snowflakes:
        encountered_snowflakes = set()
        encountered_snowflakes.add(int(line))

        current_count = 1
    else:
        current_count += 1
        current_snowflake += 1

