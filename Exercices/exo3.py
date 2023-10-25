nombre1 = int(input("Veillez taper un nombre : "))
nombre2 = int(input("Veillez taper un deuxième nombre : "))
operateur = input("Veuillez taper un opérateur : ")

def addition(nombre1, nombre2):
    return nombre1 + nombre2

def soustraction(nombre1, nombre2):
    return nombre1 - nombre2

def multiplication(nombre1, nombre2):
    return nombre1 * nombre2

def division(nombre1, nombre2):
    if nombre2 == 0:
        return "Erreur "
    return nombre1 / nombre2

operations = {
    '+': addition,
    '-': soustraction,
    '*': multiplication,
    '/': division
}

resultat = operations[operateur](nombre1, nombre2)
print(resultat)
