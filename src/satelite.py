altitudi= float(input ("Introduzca la altitud inicial del satelite (en kilometros): "))
coeficientei= float(input("Introduzca el coeficiente de arrastre que actua sobre el satelite (valor decimal pequeño): "))
altitud_m = float(input("Introduzca la altitud mínima de seguridad (en kilómetros): "))

altituda=altitudi
coeficiente= coeficientei
orbitas= 0

while True : 
    altitud_p= coeficientei * altituda 
    altituda -= altitud_p 
    coeficiente += 0.0001
    orbitas +=1
    if altituda <= altitud_m:
        print (f"El satlite ingreso a la atmósfera luego de {orbitas} orbitas")
        break
    elif altitud_p <2: 
        print(f"El satélite se ha estabilizado en órbita debido a que presenta una perdida de altitud menor a 2 kilometros a una altitud de {altituda:.2f} km después de {orbitas} órbitas.")
        break 