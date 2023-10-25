dictionnaire = {
    "Alex" : 0,
    "Yassine" : 16,
    "Marine" : 20, 
    "Elsa" : 14,
    "Soriya" : 6,
    "JF" : 19
}

meilleur = max(
    dictionnaire, 
    key=lambda eleve: dictionnaire[eleve]
)

print("L'élève avec la meilleure note est :", meilleur)
