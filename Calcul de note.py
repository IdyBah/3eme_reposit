A=float(input("Donner la note1: "))
B=float(input("Donner la note2: "))
C=float(input("Donner la note3: "))
Tot=A+B+C
Moy=Tot/3
print("La Moyenne est: ",Moy)
if Moy<12 and Moy>0:
    print("Vous avez eu la mention passable: ")
elif Moy<14 and Moy>=12:
    print("Vous avez eu la mention Assez-Bien: ")
elif Moy<16 and Moy>=14:
    print("Vous avez eu la mention Bien: ")
elif Moy<18 and Moy>=16:
    print("Vous avez eu la mention Très-Bien: ")
elif Moy<=20 and Moy>=18:
    print("Vous avez eu la mention Excellent: ")
else:
    print("Erreur sur la prise de notes")
