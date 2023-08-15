if __name__ == '__main__':
    ages = [15, 21, 30, 36, 90, 101]

    range_of_ages = range(len(ages))  # lazy

    print(range_of_ages)
    for i in range_of_ages:
        print(i, ages[i])

    ages_enum = enumerate(ages)  # lazy, list of tuples (index, value)
    print(ages_enum)
    for i, age in ages_enum:  # unpacking tuple
        print(i, age)
