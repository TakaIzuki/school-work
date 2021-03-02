sample = [10,20,30,20,10,50,60,40,80,50,40]

def findDuplicates(items):
    duplicates = set()
    uniques = []

    for i in items:
        if i not in duplicates:
            duplicates.add(i)
            uniques.append(i)
    
    return duplicates

print(findDuplicates(sample))
