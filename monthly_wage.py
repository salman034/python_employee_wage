import random


def monthly_wage():
    daily_wage_list = []
    daily_wage = present_days = working_hours = i = 0

    while present_days != 20 and working_hours != 100:
        random_number = random.randint(0, 2)
        if random_number == 0 or random_number == 1:
            daily_wage += (8 * 20)
            present_days += 1
            working_hours += 8
            i += 1
            daily_wage_list.append(8 * 20)
        else:
            daily_wage += 0
            daily_wage_list.append(0)

    return daily_wage, daily_wage_list


if __name__ == "__main__":
    wage, wage_list = monthly_wage()
    for i in range(len(wage_list)):
        print("day ", i, wage_list[i])
    print("monthly wage: ", wage)