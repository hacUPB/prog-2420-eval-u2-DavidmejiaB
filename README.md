[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/fz23fUQP)
# Documentación del proyecto
## Unidad 2
 
Estudiante: David Mejía Betancur
##
ID: 000248668
#autoevaluacion 
asistencia: 5.0
analisis:5.0
algoritmo:4.0
organización:4.0
promedio: 4.5
# Aerolinea
INICIO

// Solicitar información personal//
leer título (Sr. o Sra.)
leer nombre
leer apellido

// Mostrar saludo //
escribir "título nombre apellido, ¡Bienvenido a FastFast Airlines!"

// origen y destino//
escribir "Opciones: \nMedellín\nCartagena\nBogotá"
leer origen 
leer destino 

// Seleccionar día de la semana y día del mes//
leer día (lunes, martes, miércoles, jueves, viernes, sábado o domingo)
leer ndía del mes (1-30) #numero de dia 

// Calcular precio  
distancias= 
Medellín-Bogota: 240
Medellín-Cartagena: 461
Bogota-Medellín: 240
Bogota-Cartagena: 657
Cartagena-Medellín:461
Cartagena-Bogota: 657
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
fin si

// preferencia de asiento//
escribir "preferencia de asiento (pasillo, ventana o sin preferencia)"
leer preferencia

// asiento
SI preferencia es pasillo
  asiento = C
fin si
SINO SI preferencia es ventana
  asiento = A
  fin si
SINO
  asiento = B
fin si 
// Seleccionar número de asiento
N_asiento = aleatorio entre 1 y 29

// Mostrar información
escribir "Precio del tiquete: PRECIO"
escribir "Asiento asignado: N_asiento asiento"

FIN

Como parte principal del algoritmo se hará preguntas introductorias al usuario que permitirán su identificación dentro de la plataforma creada, en el cual se dará a conocer información esencial como su nombre, apellido y género, allí se leerá los datos suministrados.
"leer título (Sr. o Sra.)
leer nombre
leer apellido"
Con esta información suministrada se dará un mensaje de bienvenida al usuario, que incluye su título, nombre y apellido de la siguiente forma:
"escribir "título nombre apellido, ¡Bienvenido a FastFast Airlines!"
Luego de la identificación del usuario se comenzará con la información importante para la asignación del vuelo, que contendrá su asiento y precio, para esto se consultará el lugar de origen y de llegada (entre las opciones suministradas que son: Medellín, Cartagena, Bogotá)
"escribir "Opciones: \nMedellín\nCartagena\nBogotá"
leer origen 
leer destino"
Luego de tener el lugar de partida y llegada se le preguntará al usuario cual será la fecha en la cual se hará efectivo el tiquete (fecha y día ej: lunes, 5) mediante la función leer.
"leer día (lunes, martes, miércoles, jueves, viernes, sábado o domingo)
leer ndía del mes (1-30) #número de dia "
Como siguiente paso se suministrará la información de la distancia que hay entre cada uno de los destinos para que automáticamente mediante la función condicional "si", se haga una estimación del costo en el tiquete en donde se pondrá como condición que para que este tenga un costo de 79.000 debe ser un recorrido menor a 400 kilómetros entre los días lunes y jueves lo cual se agregará en un condicional interno, si esto no se cumple, o sea que sea entre los días viernes y domingo se haga efectivo el tiquete este tendrá un costo de 119.900 acabando este condicional interno, para luego aplicar un "Si no" al condicional principal en el cual se determinará que si no sé qué cumple que el viaje tenga menos de 400 kilómetros entonces este tendrá un precio de 156.900 entre los días lunes y jueves, lo cual será impuesto en un condicional interno que en caso de no cumplirse, lo que significa que el tiquete correspondiente a un viaje mayor 400 kilómetros se hará efectivo entre los días viernes y domingo, tomando un valor de 213.000, para luego dar fin al condicional interno y al principal.
"distancias= 
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
fin si"
Con el precio del tiquete ya estimado ahora se le preguntará al usuario cuál es su zona preferente dentro de la aeronave de manera que se le pueda asignar el asiento más cómodo para él, por lo cual se le preguntará que zona le gusta más entre el pasillo y las ventana o si de lo contrario no tiene preferencias.
"escribir "preferencia de asiento (pasillo, ventana o sin preferencia)"
leer preferencia"
Con la respuesta del usuario se hará un condicional en el cual en el cual se asignará la letra "A" para los preferentes de la zona de las ventanas, la letra "B" para las personas sin preferencia alguna y la letra "C" para quienes prefieran la zona de los pasillos, lo que se hará es lo siguiente: Si la zona preferente son los pasillos el asiento irá acompañado con la letra "C" si esto no se cumple y la zona de preferencia son las ventanas se asignará un asiento de tipo "B", de lo contrario se le asignará la "A" lo que quiere decir que no tiene preferencia alguna:
"SI preferencia es pasillo
  ASIENTO = C
fin si
SINO SI preferencia es ventana
  ASIENTO = A
  fin si
SINO
  ASIENTO = B
fin si "#
Para el número del asiento se utilizará una generación automática 
"N_asiento = aleatorio entre 1 y 29"
Por último, se le informará cual es la silla asignada al usuario y su precio correspondiente
"escribir "Precio del tiquete: PRECIO"
escribir "Asiento asignado: N_asiento asiento""
# Satelite 
INICIO

// Solicitar datos de entrada//
leer altitud_inicial (en kilómetros)
leer coeficiente_arrastre_inicial (un valor decimal pequeño, como 0.01) 
leer altitud_minima_seguridad (en kilómetros)

// Inicializar //
altitud_actual = altitud_inicial
coeficiente_arrastre = coeficiente_arrastre_inicial
orbitas_completadas = 0

// Simular desintegración orbital//
mientras 
  // Calcular pérdida de altitud debido al arrastre//
  altitud_perdida = coeficiente_arrastre * altitud_acual

  // Restar pérdida de altitud a la altitud actual//
  altitud_actual = altitud_actual - altitud_perdida

  // Aumentar ligeramente el coeficiente de arrastre//
  coeficiente_arrastre = coeficiente_arrastre + 0.0001

  // Incrementar número de órbitas completadas//
  orbitas_completadas = orbitas_completadas + 1

  // Verificar si el satélite se estabiliza en órbita o reingresa en la atmósfera terrestre// 
  si altitud_actual <= altitud_minima_seguridad
    escribir "El satélite ha reingresado en la atmósfera terrestre después de " orbitas_completadas " órbitas."
    fin mientras
  sino si altitud_perdida < 0.01
    escribir "El satélite se ha estabilizado en órbita a una altitud de " + ALTITUD_ACTUAL + " km después de " + ORBITAS_COMPLETADAS + " órbitas."
    fin mientras

FIN
Lo primero que se pedira son los parametros para estimar el proceso del satelite a lo largo del tiempo, empezando por la distanvia en kilometros del satelite con respecto a la tierra, luego su coeficiente de arrastre el cual indicará la razón de cambio mediante la cual el satelite tenderá a decender y por último la altura de seguridad la cual si el satelite sobrepasa ingresa a la atmosfera terrestre y se desintegrará.
"leer altitud_inicial (en kilómetros)
leer coeficiente_arrastre_inicial (un valor decimal pequeño, como 0.01) 
leer altitud_minima_seguridad (en kilómetros)"
Luego se inicializaran las variables que van a tender a cambiar mediante la estructura en bucle que mas adelante se mostrará. En este paso se determina la información suministrada por el usuario como la información actual del satelite, que será refrescada con el pasar del tiempo.
"altitud_actual = altitud_inicial
coeficiente_arrastre = coeficiente_arrastre_inicial
orbitas_completadas = 0"
En el siguiente paso se iniciará un proceso de bucle "mientras" el cual impondrá la condicioón que mientras el satelite no entre en la atmosfera terrestre este efectuará el siguiente proceso: primero se determinará la altitud perdida por el satelite en un primer mometno o primera orbita el cual se encuentra multiplicando el coeficiente de arratre ingresado por el usuario con la altitud actul del satelite, yendo al siguiente paso en el cual se determinara la nueva altitud del satelite, restando la altitud que anteriormente se consideraba como actual con la altitud perdida anteriormente hallada, para luega comenzar el mismo proceso pero con una situación adicional, la cual sera que el coeficiente de arrastre aumentará 0.0001 unidades y por ultimo se sumará una orbita completada al contador que sube progresivamente de uno en uno.
"mientras 
  // Calcular pérdida de altitud debido al arrastre//
  altitud_perdida = coeficiente_arrastre * altitud_acual

  // Restar pérdida de altitud a la altitud actual//
  altitud_actual = altitud_actual - altitud_perdida

  // Aumentar ligeramente el coeficiente de arrastre//
  coeficiente_arrastre = coeficiente_arrastre + 0.0001

  // Incrementar número de órbitas completadas//
  orbitas_completadas = orbitas_completadas + 1"
En última instancia se utilizará un condicional en el cual se determinará el final de bucle mediante las siguientes condiciones: Si la altitud actual es menor o igual a la altitud minima por seguridad, se dará el mensaje de que el satelite fue desintegrado luego de n órbitas, dando asi el fin del bucle
o en un segundo caso si la altitud perdida es menor a 0.01, se dirá que el satelite se estabilizó a x altura luego de n órbitas.
" si altitud_actual <= altitud_minima_seguridad
    escribir "El satélite ha reingresado en la atmósfera terrestre después de " orbitas_completadas " órbitas."
    fin mientras
  sino si altitud_perdida < 0.01
    escribir "El satélite se ha estabilizado en órbita a una altitud de " + ALTITUD_ACTUAL + " km después de " + ORBITAS_COMPLETADAS + " órbitas."
    fin mientras"
