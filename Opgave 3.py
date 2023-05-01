# Definer et nummer som skal bruges til tabellen
nummer = int(input("Skriv et nummer du gerne ville have tabellen på: "))

# Tabellen fra 1-10
tabel = range(1,11)


# Et loop der ganger vores nummer med tabellen
for x in tabel:
     result = x * nummer
     print(result)