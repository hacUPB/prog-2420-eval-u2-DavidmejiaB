print ("Sistema de reservas aerolineas para el mes de agosto")
print ("TITULO \nSeñor (Sr.)\nSeñora (Sra.)")
titulo=input("ingrese su titulo ")
nombre= input("Ingrese su nombre ")
apellido= input("Ingrese su ingrese su apellido ")
print (f"{titulo} {nombre} {apellido}, ¡Bienvenida a FastFast Airlines!")
print ("\nMedellín \nBogotá \nCartagena")
origen= input("Ingrese la ciudad de origen dentro las opciones: ")
destino= input ("Ingrese la ciudad de destino: ")
distancia=0
valort= 0
dia= ["lunes", "martes", "miercoles", "jueves","viernes", "sabado", "domingo"]
dia= input("Ingrese el día de la semana que desea viajar: ")
ndia= int(input("Ingrese el día del mes correspondiente: ")) 
if dia== "lunes":
    ndia= [5,12,19,26]
elif ndia != [5,12,19,26]: 
    print("no es posible las fechas no corresponden")
elif dia== "martes"or "MARTES":
    ndia= [6,13,20,27]
elif ndia != [6,13,20,27]: 
    print("no es posible las fechas no corresponden")
elif dia== "miercoles"or "MIERCOLES":
    ndia= [7,14,21,28]
elif ndia != [7,14,21,28]: 
    print("no es posible las fechas no corresponden")
elif dia== "jueves"or "JUEVES":
    ndia= [1,8,15,22,29]
elif ndia != [1,8,15,22,29]: 
    print("no es posible las fechas no corresponden")
elif dia== "viernes"or "VIERNES":
    ndia= [2,9,16,23,30]
elif ndia != [2,9,16,23,30]: 
    print("no es posible las fechas no corresponden")
elif dia== "sabado"or "SABADO":
    ndia= [3,10,17,24,31]
elif ndia != [3,10,17,24,31]: 
    print("no es posible las fechas no corresponden")
elif dia== "domingo"or "DOMINGO":
    ndia= [4,11,18,25]
elif ndia != [4,11,18,25]: 
    print("no es posible las fechas no corresponden")

if origen=="medellin" or "Medellin" or "medellín" or "Medellín" and destino=="bogota"or "Bogota" or "Bogotá" or "bogotá":
    distancia=240
elif origen=="bogota"or "Bogota" or "Bogotá" or "bogotá" and destino=="medellin" or "Medellin" or "medellín" or"Medellín":
    distancia=240
if origen=="medellin" or "Medellin" or "medellín" or "Medellín" and destino== "cartagena" or "Cartagena":
    distancia=461
elif origen=="cartagena" or "Cartagena" and destino== "medellin" or "Medellin" or "medellín" or "Medellín":
    distancia=461
elif origen=="cartagena" or "Cartagena" and destino== "bogota"or "Bogota" or "Bogotá" or "bogotá":
    distancia=657
elif origen=="bogota"or "Bogota" or "Bogotá" or "bogotá"and destino== "cartagena" or "Cartagena":
    distancia=657
if distancia<400:
    if dia in ["lunes", "martes", "miercoles", "jueves"]:
        valort=79000
    else: valort=119900
elif distancia>400: 
    if dia in ["lunes", "martes", "miercoles", "jueves"]:
        valort=156900
    else: valort=213000
print(f"el precio a pagar es: {valort}")
import random
print("pasillo\nventana\nsin preferencia")
nc= random.randint(1,29)
puesto= input("Escoja la opción de preferencia: ")
if puesto=="pasillo":
    print(f"Su asiento es {nc}C con un precio de {valort}")
if puesto=="ventana":
    print(f"Su asiento es {nc}A con un precio de {valort}")
if puesto=="sin preferencia":
    print(f"Su asiento es {nc}B con un precio de {valort}")