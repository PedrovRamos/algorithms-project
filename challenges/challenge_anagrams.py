def sort(arr):
    if len(arr) <= 1:
        return arr
    center = arr[len(arr) // 2]
    right = [x for x in arr if x > center]
    left = [x for x in arr if x < center]
    middle = [x for x in arr if x == center]
    return sort(left) + middle + sort(right)


def is_anagram(first_string, second_string):
    word1 = first_string.lower()
    word2 = second_string.lower()
    if not word1 and not word2:
        return word1, word2, False
    sorted1 = ''.join(sort(list(word1)))
    sorted2 = ''.join(sort(list(word2)))

    if sorted1 == sorted2:
        return sorted1, sorted2, True
    else:
        return sorted1, sorted2, False