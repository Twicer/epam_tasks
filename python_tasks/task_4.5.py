def remember_result(func):
    last_result = None

    def inner(*args, **kwargs):
        nonlocal last_result
        print(f"Last result = {last_result}")
        last_result = func(*args, **kwargs)
        return last_result
    return inner


@remember_result
def sum_list(*args):
    result = args[0]
    for item in args[1:]:
        result += item
    print(f"Current result = {result}")
    return result


if __name__ == "__main__":
    sum_list(5, 6)
    sum_list(7, 5)
    sum_list("asd", "dasd")