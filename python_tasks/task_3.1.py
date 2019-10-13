import string


def func_1(*strings):
    sets_of_chars = [set(string) for string in strings]
    result_chars = (sets_of_chars[0])
    for set_of_chars in sets_of_chars[1:]:
        result_chars = result_chars.intersection(set_of_chars)
    return list(result_chars)


def func_2(*strings):
    all_chars = []
    for string in strings:
        for c in list(string):
            all_chars.append(c)
    return list(set(all_chars))


def func_3(*strings):
    result_chars = func_1(strings[0], strings[-1])
    for i in range(len(strings)-1):
        result_chars += (func_1(strings[i], strings[i + 1]))
    return list(set(result_chars))


def func_4(*strings):
    alphabet = set(string.ascii_lowercase)
    return alphabet.difference(func_2(strings))


if __name__ == "__main__":
    test_strings = ["hello", "world", "python"]
    print(func_4(*test_strings))
    print(func_3(*test_strings))
    print(func_2(*test_strings))
    print(func_1(*test_strings))
