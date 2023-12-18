NB_NOTES = 3

nb_students = int(input("Quants alumnes evaluarem: "))
alumnes = [None] * nb_students
avg_upper_seven = []
more_than_eight = []

for i in range(nb_students):
    name = input("Nom de l'alumne: ")
    surname = input("Cognom de l'alumne: ")
    age = int(input("Edat de l'alumne: "))
    notes = [None] * NB_NOTES
    for j in range(NB_NOTES):
        notes[j] = int(input(f"Nota {j} de l'alumne: "))
    alumnes[i] = (name, surname, age, notes[0], notes[1], notes[2])

for alumne in alumnes:
    avg = alumne[3] * 0.3 + alumne[4] * 0.4 + alumne[5] * 0.3
    if avg > 7:
        avg_upper_seven.append(alumne)
    if alumne[3] > 8 or alumne[4] > 8 or alumne[5] > 8:
        more_than_eight.append(alumne)

print("Mitjana Superior a 7")
for alumne in avg_upper_seven:
    print("\tNom:", end=" ")
    print(alumne[0], end=" ")
    print("Cognom:", end=" ")
    print(alumne[1], end=" ")
    print("Edat:", end=" ")
    print(alumne[2], end=" ")
    print("Nota 1:", end=" ")
    print(alumne[3], end=" ")
    print("Nota 2:", end=" ")
    print(alumne[4], end=" ")
    print("Nota 3:", end=" ")
    print(alumne[5])

print("Alguna nota superior a 8")
for alumne in more_than_eight:
    print("\tNom:", end=" ")
    print(alumne[0], end=" ")
    print("Cognom:", end=" ")
    print(alumne[1], end=" ")
    print("Edat:", end=" ")
    print(alumne[2], end=" ")
    print("Nota 1:", end=" ")
    print(alumne[3], end=" ")
    print("Nota 2:", end=" ")
    print(alumne[4], end=" ")
    print("Nota 3:", end=" ")
    print(alumne[5])