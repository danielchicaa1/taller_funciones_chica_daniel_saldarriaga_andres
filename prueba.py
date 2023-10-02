import random

equipos = ['Nacional', 'Medellin', 'Pasto', 'Millonarios', 'America', 'Pereira']

todos_los_partidos = []
for i in range(len(equipos)):
    for j in range(i + 1, len(equipos)):
        todos_los_partidos.append((equipos[i], equipos[j]))


def verificar_fechas(lista_de_partidos):
    numero_fechas = len(equipos) - 1
    partidos_por_fecha = len(equipos) // 2
    for i in range(numero_fechas):
        equipos_en_fecha = set()
        for j in range(partidos_por_fecha):
            partido_actual = lista_de_partidos[i * partidos_por_fecha + j]
            equipos_en_fecha.add(partido_actual[0])
            equipos_en_fecha.add(partido_actual[1])
        if len(equipos_en_fecha) < len(equipos):
            return False
    return True

print(todos_los_partidos)

while not(verificar_fechas(todos_los_partidos)):
    random.shuffle(todos_los_partidos)

print()
for i in range(5):
    for j in range(3):
        print(todos_los_partidos[i * 3 + j])
    print()

