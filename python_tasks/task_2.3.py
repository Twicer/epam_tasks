def my_split(s, c):
    if isinstance(s, str) is False:
        print("First argument not a string")
        return None
    if isinstance(c, str) is False:
        print("Second argument not a string")
        return None
    new_list = []
    tmp_s = ""
    for _c in s:
        if _c == c:
            new_list.append(tmp_s)
            tmp_s = ""
        else:
            tmp_s += _c
    new_list.append(tmp_s)
    return new_list


if __name__ == "__main__":
    string = "Aassd f sddfsd fsd fsd fsd fsd"
    print(string.split("a"))
    print(my_split(string, "a"))
