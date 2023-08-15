from collections import defaultdict, Counter


def creating_dictionaries():
    words = {
        "Gabriel": 1,
        "Jessica": 3
    }
    print(words["Gabriel"])
    print(words.get("Gabs", "Gabriel"))

    another_dict = dict({
        "Gabriel": 1,
        "Jessica": 3
    })
    print(another_dict["Gabriel"])
    print(another_dict.get("Gabs", "Gabriel"))


def iterating():
    words = {
        "Gabriel": 1,
        "Jessica": 3
    }
    print(words)
    words["Gabriel"] = 2
    del words["Gabriel"]
    print("Gabriel" in words)
    words["Gabriel"] = 2
    print(words)
    for value in words:
        print(value)
    for key in words.keys():
        print(key)
    for value in words.values():
        print(value)
    for key, value in words.items():
        print(key, value)


if __name__ == '__main__':
    # creating_dictionaries()
    # iterating()
    text = "Welcome my name is gabriel i am studying python i have a couple dogs" \
           " and i really like dogs i also play guitar"
    text = text.lower()

    words_count_dict = {}
    for word in text.split():
        until_now = words_count_dict.get(word, 0)  # words_count_dict[word] would fail the first attempt
        words_count_dict[word] = until_now + 1

    print(words_count_dict)

    words_count_dict = defaultdict(int)
    for word in text.split():
        words_count_dict[word] += 1

    print(words_count_dict)

    words_count_dict = Counter(text.split())
    print(words_count_dict)
