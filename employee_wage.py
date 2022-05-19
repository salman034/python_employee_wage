import random


def employee_wage(random_number):
    if random_number == 0:
        daily_wage = 8 * 20
    else:
        daily_wage = 0

    return daily_wage


if __name__ == "__main__":
    random = random.randint(0, 1)
    daily_employee_wage = employee_wage(random)
    print(daily_employee_wage)