import functools


def func(start_list):
    if isinstance(start_list, list) is False:
        print("It's not a list")
        return None
    try:
        full_product = functools.reduce(lambda a, b: a*b, start_list)
    except TypeError:
        print("List has not int item")
        return None
    return [full_product // i for i in start_list]


if __name__ == "__main__":
    print(func([1, 2, 3, 4, 5]))
