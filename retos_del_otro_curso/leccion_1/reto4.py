def calcular_horario_de_llegada (hora_salida: int, minuto_salida: int, 
                                 segundo_salida: int, duracion_horas: 
                                 int, duracion_minutos: int, 
                                 duracion_segundos: int)->str:
    hora_llegada = hora_salida + duracion_horas
    minuto_llegada = minuto_salida + duracion_minutos
    segundo_llegada = segundo_salida + duracion_segundos 
    
    a =str(hora_llegada) + ":" + str(minuto_llegada) + ":" + str(segundo_llegada)
    print ("su vuelo llegara a las: " + str(a))
    return 

hora_partida = int(input("ingrese la hora de partida de su vuelo: "))
minuto_partida = int(input("ingrese el minuto de partida de su vuelo: "))
segundos_partida = int(input("ingrese el segundo de partida de su vuelo: "))

hora_duración = int(input("ingrese las horas que dura su vuelo: "))
minuto_duración = int(input("ingrese los minutos que dura su vuelo: "))
segundos_duración = int(input("ingrese los segundos que dura su vuelo su vuelo: "))

z = calcular_horario_de_llegada(hora_partida, minuto_partida, segundos_partida, hora_duración, minuto_duración, segundos_duración)















