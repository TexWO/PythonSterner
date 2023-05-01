#LIX finder
text = "Artificial intelligence is shaping the future of humanity across nearly every industry."


L = 0
for x in text.split():
    if (len(x) >= 6):
        L = L + 1


O = len(text.split())


P = text.count(".")

LIX = O/P + L+100/O

round(LIX)

if LIX >= 55:
    print("Meget svær, faglitteratur på akademisk niveau, lovtekster.")

if LIX >= 45:
    print("Svær, f.eks. saglige bøger, populærvidenskabelige værker, akademiske udgivelser.")

if LIX >= 35:
    print("Middel, f.eks. dagblade og tidsskrifter.")

if LIX >= 25:
    print("Let for øvede læsere, f.eks. ugebladslitteratur og skønlitteratur for voksne.")

if LIX < 25:
    print("Let tekst for alle læsere, f.eks. børnelitteratur.")
