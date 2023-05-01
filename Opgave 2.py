text1 = "Der var engang "
text2 = "en mand som "
text3 = "boede i en spand. Spanden var af ler"

# Printer første tekst
print(text1 + text2 + text3)

# Finder længden af hver tekst
Længde_text1 = len(text1.split())
Længde_text2 = len(text2.split())
Længde_text3 = len(text3.split())

#Printer længden af teksterne
print(Længde_text1)
print(Længde_text2)
print(Længde_text3)


# Printer det andet bogstav i teksterne
Anden_bogstav1 = print("This is second bogstav in text1: " + text1[1])
Anden_bogstav2 = print("This is second bogstav in text2: " + text2[1])
Anden_bogstav3 = print("This is second bogstav in text3: " + text3[1])

# Tjekker om teksterne er ens
if text1 == text2:
    print("text1 and text2 are the same")
else:
    print("None of the texts are the same")

#Printer hele teksten i uppercase
text1 = text1.upper()
text2 = text2.upper()
text3 = text3.upper()

# Ny tekst i uppercase
print(text1 + text2 + text3)

#Laver bare teksten lowercase igen
text1 = text1.lower()
text2 = text2.lower()
text3 = text3.lower()


# Substring af tekst 1
Substring = text1
print(Substring[0:5])

# Sammenfletning af de tre tekster hvor man tager første bogstav fra første tekst og anden bogstav fra anden tekst osv...
print(text1[0] + text2[1] + text3[2])

# Tjekker hvor mange gange bogstavet "e" forekommer i teksten
E_counter = 0
text_full = text1 + text2 + text3 

for x in text_full:
    if x == "e":
        E_counter = E_counter + 1

print(E_counter)