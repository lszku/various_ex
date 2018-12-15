list1 = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]


def count_freq(l: list) -> dict:
    freq = {}
    for value in l:
        if value in freq.keys():
            freq[value] += 1
        else:
            freq[value] = 1
    return freq


print(count_freq(list1))
