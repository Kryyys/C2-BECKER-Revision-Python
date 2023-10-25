nombre = int(input("Veuillez rentrer un nombre :"))

def factorielle(nombre):
    if nombre == 0:
        return 1
    else:
        return nombre * factorielle(nombre-1)

resultat = factorielle(nombre)

print(resultat)