import random

def distancia(ciudad1, ciudad2):
    return abs(ciudad1[0] - ciudad2[0]) + abs(ciudad1[1] - ciudad2[1])

def longitud_ruta(ruta, ciudades):
    longitud = 0
    for i in range(len(ruta) - 1):
        longitud += distancia(ciudades[ruta[i]], ciudades[ruta[i + 1]])
    return longitud

def solucion_inicial(ciudades):
    return random.sample(range(len(ciudades)), len(ciudades))

def actualizar_feromona(feromonas, rutas, evaporation_rate, Q):
    for i in range(len(feromonas)):
        for j in range(len(feromonas[i])):
            feromonas[i][j] *= (1 - evaporation_rate)
            for ruta in rutas:
                if (i, j) in ruta:
                    feromonas[i][j] += Q / longitud_ruta(ruta, ciudades)

ciudades = [(0, 0), (1, 2), (3, 4), (5, 6)]
n_ciudades = len(ciudades)
n_hormigas = 10
n_generaciones = 100
evaporation_rate = 0.1
Q = 1.0

feromonas = [[1.0] * n_ciudades for _ in range(n_ciudades)]

for generacion in range(n_generaciones):
    rutas = []
    for _ in range(n_hormigas):
        ruta = solucion_inicial(ciudades)
        rutas.append(ruta)

    actualizar_feromona(feromonas, rutas, evaporation_rate, Q)

mejor_ruta = min(rutas, key=lambda ruta: longitud_ruta(ruta, ciudades))
mejor_longitud = longitud_ruta(mejor_ruta, ciudades)

print(mejor_ruta)
print(mejor_longitud)
