sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n):
    return n[-1]

def tupleSort(items):
    sorted_items = sorted(items, key=last)
    return sorted_items

print(tupleSort(sample))