fichierLecture = open("texte.txt", "r")

lecture = fichierLecture.read()

mots = lecture.split()
nombre = len(mots)
nombrestr = str(nombre)

print("Nombre de mots dans la phrase : " + nombrestr)

fichierEcriture = open("resultat.txt", "a")
fichierEcriture.write("Nombre de mots : " + nombrestr)

fichierLecture.close()