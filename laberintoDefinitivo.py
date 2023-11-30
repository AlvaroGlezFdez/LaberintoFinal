

# Coordenadas de los muros del laberinto
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

# Establecemos las dimensiones del laberinto
filas = 5
columnas = 5

laberinto = [[" " for _ in range(columnas)] for _ in range(filas)]

for coordenadas in muro:
    fila,columna = coordenadas
    laberinto[fila][columna] = "X"


# Como imprimir el laberinto

for fila in laberinto:
    print(" ".join(fila))


def encontrar_salida(laberinto, fila, columna, camino):

    if fila < 0 or fila  >= len(laberinto) or columna < 0 or columna >= len(laberinto[0]) or laberinto[fila][columna] == 'X':
        return False

    if laberinto[fila][columna] == 'S':
        camino.append('Salida')
        return True

    if laberinto[fila][columna] == ' ':
        laberinto[fila][columna] = 'Visitado'
        if encontrar_salida(laberinto, fila + 1, columna, camino):
            camino.append('Abajo')
            return True
        if encontrar_salida(laberinto, fila - 1, columna, camino):
            camino.append('Arriba')
            return True
        if encontrar_salida(laberinto, fila, columna + 1, camino):
            camino.append('Derecha')
            return True
        if encontrar_salida(laberinto, fila, columna - 1, camino):
            camino.append('Izquierda')
            return True
        laberinto[fila][columna] = " "
        return False

camino = []
print(camino)
