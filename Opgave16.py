

def IsPalindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return IsPalindrome(word[1:-1])
    else:
        return False
    
print(IsPalindrome("racecar"))