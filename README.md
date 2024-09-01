[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/fz23fUQP)
# Documentación del proyecto
## Unidad 2

Estudiante: David Mejía Betancur
ID: 000248668
Como parte principal del algoritmo se hará preguntas introductorias al usuario que permitirán su identificación dentro de la plataforma creada, en el cual se dará a conocer información esencial como su nombre, apellido y género, allí se leerá los datos suministrados.
 leer título (Sr. o Sra.)
 leer nombre 
 leer apellido")
Con esta información suministrada se dará un mensaje de bienvenida al usuario, que incluye su título, nombre y apellido de la siguiente forma:
#"escribir "título nombre apellido, ¡Bienvenido a FastFast Airlines!"#
Luego de la identificación del usuario se comenzará con la información importante para la asignación del vuelo, que contendrá su asiento y precio, para esto se consultará el lugar de origen y de llegada (entre las opciones suministradas que son: Medellín, Cartagena, Bogotá)
#"escribir "Opciones: \nMedellín\nCartagena\nBogotá"
leer origen 
leer destino"#
Luego de tener el lugar de partida y llegada se le preguntará al usuario cual será la fecha en la cual se hará efectivo el tiquete (fecha y día ej: lunes, 5) mediante la función leer.
#"leer día (lunes, martes, miércoles, jueves, viernes, sábado o domingo)
leer ndía del mes (1-30) #número de dia "#
Como siguiente paso se suministrará la información de la distancia que hay entre cada uno de los destinos para que automáticamente mediante la función condicional "si", se haga una estimación del costo en el tiquete en donde se pondrá como condición que para que este tenga un costo de 79.000 debe ser un recorrido menor a 400 kilómetros entre los días lunes y jueves lo cual se agregará en un condicional interno, si esto no se cumple, o sea que sea entre los días viernes y domingo se haga efectivo el tiquete este tendrá un costo de 119.900 acabando este condicional interno, para luego aplicar un "Si no" al condicional principal en el cual se determinará que si no sé qué cumple que el viaje tenga menos de 400 kilómetros entonces este tendrá un precio de 156.900 entre los días lunes y jueves, lo cual será impuesto en un condicional interno que en caso de no cumplirse, lo que significa que el tiquete correspondiente a un viaje mayor 400 kilómetros se hará efectivo entre los días viernes y domingo, tomando un valor de 213.000, para luego dar fin al condicional interno y al principal.
#"distancias= 
Medellín-Bogotá: 240
Medellín-Cartagena: 461
Bogotá-Medellín: 240
Bogotá-Cartagena: 657
Cartagena-Medellín:461
Cartagena-Bogotá: 657
SI distancia entre origen y destino < 400 km
  SI día de la semana es lunes, martes, miércoles o jueves
    PRECIO = $79,900
  SINO
    PRECIO = $119,900
    fin si
SINO
  SI día de la semana es lunes, martes, miércoles o jueves
    PRECIO = $156,900
  SINO
    PRECIO = $213,000
    Fin si 
fin si"#
Con el precio del tiquete ya estimado ahora se le preguntará al usuario cuál es su zona preferente dentro de la aeronave de manera que se le pueda asignar el asiento más cómodo para él, por lo cual se le preguntará que zona le gusta más entre el pasillo y las ventana o si de lo contrario no tiene preferencias.
#"escribir "preferencia de asiento (pasillo, ventana o sin preferencia)"
leer preferencia"#
Con la respuesta del usuario se hará un condicional en el cual en el cual se asignará la letra "A" para los preferentes de la zona de las ventanas, la letra "B" para las personas sin preferencia alguna y la letra "C" para quienes prefieran la zona de los pasillos, lo que se hará es lo siguiente: Si la zona preferente son los pasillos el asiento irá acompañado con la letra "C" si esto no se cumple y la zona de preferencia son las ventanas se asignará un asiento de tipo "B", de lo contrario se le asignará la "A" lo que quiere decir que no tiene preferencia alguna:
#"SI preferencia es pasillo
  ASIENTO = C
fin si
SINO SI preferencia es ventana
  ASIENTO = A
  fin si
SINO
  ASIENTO = B
fin si "#
Para el número del asiento se utilizará una generación automática 
#"N_asiento = aleatorio entre 1 y 29"#
Por último, se le informará cual es la silla asignada al usuario y su precio correspondiente
#"escribir "Precio del tiquete: PRECIO"
escribir "Asiento asignado: N_asiento asiento""# 


