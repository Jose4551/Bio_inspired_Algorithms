import random 

def evaluar_apt(solve, obj):
    suma1 = sum(solve)
    return -abs(obj - suma1) 
 
 
#evaluacion de la poblacion
def selecciondepoblacion(poblacion, aptitudes, tamano_seleccion):
    seleccionados = []
    for _ in range(tamano_seleccion):
        indice = aptitudes.index(max(aptitudes))
        seleccionados.append(poblacion[indice])
        del poblacion[indice]
        del aptitudes[indice]
    return seleccionados
 
#clonacion de la poblacion 
def clonar_p(seleccionados, tasa_mutacion):
    poblacion_clonada = []
    for solve in seleccionados:
        num_clones = int(1 + tasa_mutacion * random.random())
        for _ in range(num_clones):
            copia = solve[:] 

            indice_mutacion = random.randint(0, len(copia) - 1)
            copia[indice_mutacion] = random.choice([-1, 1]) * random.randint(1, 10)
            poblacion_clonada.append(copia)
    return poblacion_clonada
#se reemplaza la poblacion
def reemplazar_p(poblacion, poblacion_clonada):
    poblacion.extend(poblacion_clonada)
    poblacion.sort(key=lambda solve: evaluar_apt(solve, obj), reverse=True)
    return poblacion[:len(poblacion_clonada)]
 
tamano_poblacion = 100
max_generaciones = 100
tasa_mutacion = 0.1
tamano_seleccion = 20
obj = 50  

# Inicialización de la población
poblacion = [[random.randint(1, 10) * random.choice([-1, 1]) for _ in range(10)] for _ in range(tamano_poblacion)]
for generacion in range(max_generaciones):
    # Evaluar la aptitud de la población
    aptitudes = [evaluar_apt(solve, obj) for solve in poblacion]
    # Selección de soluciones para clonación
    seleccionados = selecciondepoblacion(poblacion, aptitudes, tamano_seleccion)
    # Clonación y mutación
    poblacion_clonada = clonar_p(seleccionados, tasa_mutacion)
    # Reemplazo de la población original
    poblacion = reemplazar_p(poblacion, poblacion_clonada)

mejor_solucion = poblacion[0]
mejor_aptitud = evaluar_apt(mejor_solucion, obj)

print("La mejor solucion es : ", mejor_solucion)
print("Suma :", sum(mejor_solucion))
print("Aptitud :", mejor_aptitud)