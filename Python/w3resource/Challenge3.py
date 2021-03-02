def findLarge(items):
    sorted_items = sorted(items)
    return sorted_items[-1]

print(findLarge([76,12,98,3]))