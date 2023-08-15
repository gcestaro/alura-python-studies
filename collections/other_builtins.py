def _range():
    global i
    range_of_ages = range(len(ages))  # lazy
    print(range_of_ages)
    for i in range_of_ages:
        print(i, ages[i])


def _enumerate():
    global i
    ages_enum = enumerate(ages)  # lazy, list of tuples (index, value)
    print(ages_enum)
    for i, age in ages_enum:  # unpacking tuple
        print(i, age)


if __name__ == '__main__':
    ages = [15, 21, 45, 30, 54, 78, 36, 90, 101]

    # _range()
    # _enumerate()

    print(sorted(ages))
    print(sorted(ages, reverse=True))
    print(ages)
