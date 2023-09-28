import random

equipos = ['Medellin', 'Nacional', 'Millonarios', 'Envigado', 'America', 'Huila']

todos_los_partidos = []
for i in range(len(equipos)):
    for j in range(i+1, len(equipos)):
        todos_los_partidos.append((equipos[i], equipos[j]))

fechas = []
for i in range(5):
    fecha = []
    while len(fecha) < 10:
        indice = random.randint(0, len(todos_los_partidos) - 1)
        partido = todos_los_partidos[indice]
        ya_jugo = False
        for un_partido in fecha:
            if partido[0] in un_partido or partido[1] in un_partido:
                ya_jugo = True
                break
        if ya_jugo:
            continue
        fecha.append(partido)
        todos_los_partidos.pop(indice)
    fechas.append(fecha)
print(fecha)
print(fechas)


