def count_letters(string):
    result_dict = {}
    for char in string:
        current_count = result_dict.get(char)
        if current_count:
            result_dict.update({char: current_count + 1})
        else:
            result_dict.update({char: 1})
    return result_dict


if __name__ == "__main__":
    print(count_letters("stringsample"))
