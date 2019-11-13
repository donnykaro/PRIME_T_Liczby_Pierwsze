import sys

max_range = 10000
max_number_of_cases = 100000

number_of_cases = int(input())
if number_of_cases >= max_number_of_cases:
    sys.exit(0)


def check_if_prime(number):
    if number == 1:
        return "NIE"
    elif number == 2:
        return "TAK"

    for divide_by in range(2, number):
        if number != divide_by and number % divide_by == 0:
            return "NIE"
    return "TAK"


numbers_to_check = []
for i in range(0, number_of_cases):
    user_number = int(input())
    if user_number < 1 or user_number > max_range:
        sys.exit(0)
    else:
        numbers_to_check.append([user_number, check_if_prime(user_number)])

for i in range(0, len(numbers_to_check)):
    print(numbers_to_check[i][1])
