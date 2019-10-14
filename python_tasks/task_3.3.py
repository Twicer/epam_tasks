def count_letters(s: str):
    result_dict = {}
    for c in s:
        current_count = result_dict.get(c)
        if current_count:
            result_dict.update({c: current_count + 1})
        else:
            result_dict.update({c: 1})
    return result_dict


if __name__ == "__main__":
    print(count_letters("stringsample"))
