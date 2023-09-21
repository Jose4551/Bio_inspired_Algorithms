import math
import random

def funcion_objetivo(x):
    return x**2

def recocido_simulado(funcion_objetivo, temperatura_inicial, factor_enfriamiento, iteraciones):
    mejor_solucion = random.uniform(-2.0, 2.0)
    mejor_valor = funcion_objetivo(mejor_solucion)
    
    temperatura_actual = temperatura_inicial
    
    for _ in range(iteraciones):
        solucion_propuesta = mejor_solucion + random.uniform(-0.2, 0.2)
        valor_propuesto = funcion_objetivo(solucion_propuesta)
        
        if valor_propuesto < mejor_valor:
            mejor_solucion = solucion_propuesta
            mejor_valor = valor_propuesto
        elif random.random() < math.exp(-(valor_propuesto - mejor_valor) / temperatura_actual):
            mejor_solucion = solucion_propuesta
            mejor_valor = valor_propuesto
        
        temperatura_actual *= factor_enfriamiento
    
    return mejor_solucion, mejor_valor

temperatura_inicial = 10.0
factor_enfriamiento = 0.95
iteraciones = 100

solucion, valor = recocido_simulado(funcion_objetivo, temperatura_inicial, factor_enfriamiento, iteraciones)

print(f"Mejor solución encontrada: {solucion}")
print(f"Valor de la funcion objetivo: {valor}")
