import random

equipos = ['Medellin', 'Nacional', 'Millonarios', 'Envigado', 'America', 'Huila']


def crear_tabla(equipos):
    tabla = []
    for equipo in equipos:
        resultados = {
            'nombre': equipo,
            'puntos': 0,
            'GF': 0,
            'GC': 0
        }
        tabla.append(resultados)
    return tabla


jugar_partido = lambda equipo1, equipo2: (equipo1, random.randint(0, 5), 'vs', random.randint(0,5), equipo2)


def actualizar_tabla(partido, tabla):
    equipo1 = partido[0]
    equipo2 = partido[4]

    for equipo in tabla:
        if equipo['nombre'] == equipo1:
            equipo_uno = equipo

    for equipo in tabla:
        if equipo['nombre'] == equipo2:
            equipo_dos = equipo

    equipo_uno['GF'] = equipo_uno['GF'] + partido[1]
    equipo_uno['GC'] = equipo_uno['GC'] + partido[3]

    equipo_dos['GF'] = equipo_dos['GF'] + partido[3]
    equipo_dos['GC'] = equipo_dos['GC'] + partido[1]

    if partido[1] > partido[3]:
        equipo_uno['puntos'] = equipo_uno['puntos'] + 3

    elif partido[1] < partido[3]:
        equipo_dos['puntos'] = equipo_dos['puntos'] + 3

    else:
        equipo_uno['puntos'] = equipo_uno['puntos'] + 1
        equipo_dos['puntos'] = equipo_dos['puntos'] + 1


ordenar_tabla = lambda tabla: sorted(tabla, key=lambda k: k['puntos'], reverse=True)

def imprimir_tabla(tabla):
    print()
    print(f'{"Tabla de resultados".center(40, " ")}')
    print(f'{"Equipo".center(20, " ")} {"Puntos".ljust(10, " ")} {"GF".ljust(4, " ")} {"GC".ljust(4, " ")}')
    for posicion in tabla:
        print(f'{posicion["nombre"].ljust(20, " ")} {str(posicion["puntos"]).ljust(10, " ")} {str(posicion["GF"]).ljust(4, " ")} {str(posicion["GC"]).ljust(4, " ")}')

def iniciar_torneo():
    tabla = crear_tabla(equipos)
    print()
    print(f'{"Partidos Jugados".center(35, " ")}')
    print()
    for i in range(len(equipos)):
        for j in range(i+1,len(equipos)):
            resultado_partido = jugar_partido(equipos[i], equipos[j])
            print(resultado_partido)
            actualizar_tabla(resultado_partido, tabla)
    tabla = ordenar_tabla(tabla)
    imprimir_tabla(tabla)


iniciar_torneo()


