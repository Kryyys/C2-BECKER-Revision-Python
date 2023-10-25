liste = [22, 54, 644, 87, 2, 65, 35, 47, 824, 1023]

maxValue= None
minValue= None

for max in liste:
    if maxValue is None or max >= maxValue:
        maxValue = max

print("Le nombre le plus haut est : ", maxValue)

for min in liste:
    if minValue is None or min <= minValue:
        minValue = min

print("Le nombre le plus bas est : ", minValue)

print(sum(liste))
