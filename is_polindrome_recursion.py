def is_polindrome(word):
    if len(word)== 0 or len(word) == 1:
        return True
    else:
     return word[0] == word[-1] and is_polindrome(word[1:-1])

print(is_polindrome("eee"))
