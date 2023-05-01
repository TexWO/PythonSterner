

def FindBestemtBogstav(string, letter):
    string = string.lower()
    letter = letter.lower()
    count = 0
    for i in string:
        if i == letter:
            count += 1
    return count

    
print(FindBestemtBogstav("Allesammen", "a"))