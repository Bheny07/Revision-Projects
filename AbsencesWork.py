def record_absences():
    absences = []
    while True:
        name = input("Enter employee name (or $ to end): ")
        if name == '$':
            break
        days_absent = int(input("Enter number of days absent: "))
        absences.append((name, days_absent))
    return absences


def calculate_average(absences):
    total_days = sum(days for _, days in absences)
    return total_days / len(absences)


def find_most_absent(absences):
    most_absent = max(absences, key=lambda x: x[1])
    return most_absent[0]


def find_never_absent(absences):
    all_names = [name for name, _ in absences]
    all_names.sort()
    never_absent = [name for name in all_names if all_names.count(name) == 1]
    return never_absent


def above_average_absences(absences, average):
    above_average = [(name, days) for name, days in absences if days > average]
    above_average.sort(key=lambda x: x[0])  # Sort alphabetically by name
    return above_average


def main():
    print("Enter employee names and days absent. Enter $ to end.")
    absences = record_absences()

    if not absences:
        print("No data entered.")
        return

    average = calculate_average(absences)
    print("Average number of days absent per year:", average)

    most_absent = find_most_absent(absences)
    print("Employee with most days absent:", most_absent)

    never_absent = find_never_absent(absences)
    print("Employees who were never absent:", never_absent)

    above_average = above_average_absences(absences, average)
    print("Employees with absences above average:")
    for name, days in above_average:
        print(name, "-", days, "days")


if __name__ == "__main__":
    main()
