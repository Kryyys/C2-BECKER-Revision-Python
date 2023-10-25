# Datetime est un MODULE (et le deuxième Datetime une CLASS)
from datetime import datetime

ajd = datetime.now()

dateEurope = ajd.strftime("%d/%m/%Y %H:%M:%S")

print("Date et Heure d'aujourd'hui =", dateEurope)


