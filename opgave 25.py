"""
1. Skriv et program, der sorterer en liste af tal vha. bubblesort-algoritmen.

2. Skriv et program, der sorterer en liste af tal vha. mergesort-algoritmen.

3. Afprøv dine sorteringsalgoritmer på lister med mange tusinde tal. Hvilken en af algoritmerne
er mon hurtigst?

"""

def bubblesort(liste):
    # Iterere igennem listen
    for i in range(len(liste)):
        # Iterere igennem listen igen men finder indexet af det næste tal
        for j in range(len(liste)-1):
            # Tjekker om det næste tal er større end det nuværende tal
            if liste[j] > liste[j+1]:
                # Hvis det er større, så bytter de plads
                liste[j], liste[j+1] = liste[j+1], liste[j]
    # Returnere listen
    return liste


data = [5, 1, 4, 2, 8, 6]
#print(bubblesort(data))


def Mergesort(liste):
    # Hvis listen kun har et element, så returner listen
    if len(liste) <= 1:
        return liste
    # Finder midten af listen
    midten = len(liste) // 2
    # Splitter listen i to
    venstre = liste[:midten]
    højre = liste[midten:]
    # Kaldes på igen med de to nye lister
    venstre = Mergesort(venstre)
    højre = Mergesort(højre)
    # Returnere listen
    liste = venstre + højre

Mergesort(data)
