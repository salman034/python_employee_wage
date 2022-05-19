import random


def check_employee(random_number):
    if random_number == 0:
        return "Absent"
    else:
        return "Present"


if __name__ == "__main__":
    random = random.randint(0, 1)
    attendence = check_employee(random)
    print(attendence)