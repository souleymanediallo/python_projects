import random

nombre_mystere = random.randint(0, 10)
nombre = input("Quel est le nombre mystere ? : ")

if nombre.isdigit():
    nombre = int(nombre)
    if nombre > nombre_mystere:
        print(f"Le nombre mystere est plus petit que {nombre}")
    elif nombre < nombre_mystere:
        print(f"Le nombre mystere est plus grand que {nombre}")
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
else:
    print("SVP, entrez un nombre valide.")


    