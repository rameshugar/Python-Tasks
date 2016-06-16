def nest_tuple(tup1, tup2):
    result = []
    for i in tup1:
        result.append((i, tup2[tup1.index(i)]))
    return result
