def split_by_index(s, indexes):
    if isinstance(s, str) is False:
        print("First argument not a string")
        return None
    if isinstance(indexes, list) is False:
        print("Second argument not a list")
        return None
    len_s = len(s)
    if isinstance(indexes[0], int) is False:
        print("List has not int item")
        return None
    new_indexes = [indexes[0]]
    for i in range(len(indexes))[1:]:
        if isinstance(indexes[i], int) is False:
            print("List has not int item")
            return None
        current_index = indexes[i]
        if len_s - 1 < current_index:
            break
        if current_index >= new_indexes[-1]:
            new_indexes.append(current_index)
    new_indexes = list(set([0] + new_indexes + [len_s]))
    return [s[new_indexes[i]:new_indexes[i+1]] for i in range(len(new_indexes)-1)]


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
