"""
    Sets:
    - Unordered by default
    - Ignore duplicated elements
"""


def with_lists_to_set():
    data_science_users = [15, 23, 43, 56]
    machine_learning_users = list([13, 23, 56, 42])

    all_users = data_science_users.copy()
    all_users.extend(machine_learning_users)

    all_users_set = set(all_users)

    print(all_users_set)
    print(len(set(all_users)))
    print(len(all_users))


def set_common_operators():
    data_science_users = {15, 23, 43, 56}
    machine_learning_users = {13, 23, 56, 42}
    all_single_users = data_science_users | machine_learning_users  # union of 2 sets, A or B
    print(all_single_users)
    all_users_in_both = data_science_users & machine_learning_users  # intersection of 2 sets, A and B
    print(all_users_in_both)
    data_science_users_not_in_ml = data_science_users - machine_learning_users  # A not B
    print(data_science_users_not_in_ml)
    # exclusive OR (XOR), A not B OR B not A
    data_science_not_in_ml_and_ml_not_in_data_science = data_science_users ^ machine_learning_users
    print(data_science_not_in_ml_and_ml_not_in_data_science)


if __name__ == '__main__':
    # with_lists_to_set()
    # set_common_operators()
    users = {1, 2, 4, 10, 7, 28, 30, 99, 9}
    users.add(31)
    immutable_users = frozenset(users)
    # immutable_users.add(1) # Won't work
