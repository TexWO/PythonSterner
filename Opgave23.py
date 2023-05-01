

def FindBestemtBogstav(string, letter):
    dict = {}
    string = string.lower()
    letter = letter.lower()
    count = 0
    for i in string:
        if i == letter:
            count += 1
    dict[letter] = count
    return dict


print(FindBestemtBogstav("Allesammen", "e"))