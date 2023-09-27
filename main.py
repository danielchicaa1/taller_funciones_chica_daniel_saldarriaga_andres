import random

equipos = ['Medellin', 'Nacional', 'Millonarios', 'Envigado', 'America', 'Huila']


def crear_tabla(equipos):
    tabla = []
    for equipo in equipos:
        resultados = {
            'nombre': equipo,
            'puntos': 0,
            'goles a favor': 0,
            'goles en contra': 0
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

    equipo_uno['goles a favor'] = equipo_uno['goles a favor'] + partido[1]
    equipo_uno['goles en contra'] = equipo_uno['goles en contra'] + partido[3]

    equipo_dos['goles a favor'] = equipo_dos['goles a favor'] + partido[3]
    equipo_dos['goles en contra'] = equipo_dos['goles en contra'] + partido[1]

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
    print(f'Tabla de resultados')
    for posicion in tabla:
        print(posicion)

def iniciar_torneo():
    tabla = crear_tabla(equipos)
    for i in range(len(equipos)):
        for j in range(i+1,len(equipos)):
            resultado_partido = jugar_partido(equipos[i], equipos[j])
            print(resultado_partido)
            actualizar_tabla(resultado_partido, tabla)
    tabla = ordenar_tabla(tabla)
    imprimir_tabla(tabla)


iniciar_torneo()


