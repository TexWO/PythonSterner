# Tjekker om CPR-nummer er validt

kontrol_numre = [4,3,2,7,6,5,4,3,2,1]

New_list = []

def check_cpr(person_nr):
    for j,i in enumerate(person_nr):
        i = int(i)
        n = kontrol_numre[j] * i
        New_list.append(n)
    
    if sum(New_list) % 11 == 0:
        print("CPR-nummeret er validt")
    else:
        print("CPR-nummeret er ikke validt")

cpr_nummer = input("Indtast dit CPR-nummer: ")
check_cpr(cpr_nummer)