#BMR udregner

#Giver nogle variable værdier som vi senere ændre
Vægt = 0
Alder = 0
Højde = 0

#Indtast om du er mand eller kvinde
Køn = input("Indtast venligst hvilket køn du er M/K: ")
Køn.lower()



#Ændre variablerne vi lavede i starten til brugerens input
if Køn == "m" or "k":
    Vægt = int(input("Indtast din vægt i kg: "))
    Alder = int(input("Indtast din alder: "))
    Højde = int(input("Indtast din højde i cm: "))

#Formel for BMR
BMR_M = 66.5 + (13.76*Vægt) + (5.003*Højde) - (6.755*Alder)
BMR_K = 655 + (9.563*Vægt) + (1.850*Højde) - (4.676*Alder)

round(BMR_M)
round(BMR_K)
Køn.lower()


#Viser det tal der er bestemt for dit køn
if Køn == "m":
    print("Dit BMR tal som mand er: " + str(BMR_M))

if Køn == "k":
    print("Dit BMR tal som kvinde er: " + str(BMR_K))