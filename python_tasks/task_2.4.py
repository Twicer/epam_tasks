def split_by_index(s, indexes):
    len_s = len(s)
    new_indexes = [indexes[0]]
    for i in range(len(indexes))[1:]:
        current_index = indexes[i]
        if len_s - 1 < current_index:
            break
        if current_index >= new_indexes[-1]:
            new_indexes.append(current_index)
    new_indexes = list(set([0] + new_indexes + [len_s]))
    return [s[new_indexes[i]:new_indexes[i+1]] for i in range(len(new_indexes)-1)]


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
