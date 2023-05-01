#Givet to tekststrenge. Overvej forskellige måder til at undersøge om den ene er et plagiat af den anden.


def plagiat(text1, text2):
    if text1 == text2:
        print("Plagiat")
    else:
        print("Ikke plagiat")

plagiat("Hej", "Hej")

# Den tjekker om teksten er ens, hvis den er, så er det plagiat, hvis den ikke er, så er det ikke plagiat.