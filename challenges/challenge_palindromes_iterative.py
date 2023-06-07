def is_palindrome_iterative(word):
    if type(word) != str or word == "":
        return False
    word = word.lower()
    if word == word[::-1]:
        return True
    return False
    raise NotImplementedError