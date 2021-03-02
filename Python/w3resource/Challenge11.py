sample_1 = [1, 5, 2, 65, 7]
sample_2 = [3, 4, 6, 65, 9]

def sameNum(item_1, item_2):
    same_number = False

    for i in item_1:
        for f in item_2:
            if i == f:
                same_number = True
    return same_number

print(sameNum(sample_1, sample_2))