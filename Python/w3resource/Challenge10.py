sample = "The quick brown fox jumps over the lazy dog"

def wordLen(length, item):
    long_words = []
    split_item = item.split(" ")

    for i in split_item:
        if len(i) > length:
            long_words.append(i)
    return long_words

print(wordLen(3, sample))