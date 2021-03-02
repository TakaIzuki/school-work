sample = ["abc", "xyz", "aba", "1221"]

def stringCounter(items):
    amount = 0
    for i in items:
        if len(i) >= 2 and i[0] == i[-1]:
            amount += 1
    return amount

print("The amount of string that meet the criteria is:",stringCounter(sample))