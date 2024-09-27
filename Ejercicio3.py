import numpy as np

# Parámetro de la distribución exponencial
lambd = 1.0

# Número de muestras por estrato
n_samples = 10000

# Función para calcular el valor esperado en un estrato [a, b]
def valor_esperado_estratificado(lambd, a, b, n_samples):
    if b == np.inf:
        # Generar muestras de una distribución exponencial para el estrato [a, ∞)
        muestras = np.random.exponential(scale=1/lambd, size=n_samples)
        muestras_filtradas = muestras[muestras >= a]
    else:
        # Generar muestras uniformemente distribuidas para el estrato [a, b)
        muestras = np.random.uniform(a, b, size=n_samples)
        muestras_filtradas = muestras

    # Calcular el peso del estrato
    peso = np.exp(-lambd * a) - np.exp(-lambd * b) if b != np.inf else np.exp(-lambd * a)
    
    # Calcular el valor esperado de las muestras en el estrato
    valor_esperado = np.mean(muestras_filtradas)
    
    return valor_esperado * peso

# Función para calcular el valor esperado total utilizando tres estratos
def valor_esperado_total(lambd, n_samples):
    # Definir los estratos
    estratos = [(0, 1), (1, 3), (3, np.inf)]
    
    # Calcular el valor esperado en cada estrato y sumar
    valor_esperado_total = 0
    for a, b in estratos:
        valor_esperado_total += valor_esperado_estratificado(lambd, a, b, n_samples)
    
    return valor_esperado_total

# Calcular el valor esperado con el método estratificado
resultado = valor_esperado_total(lambd, n_samples)
print(f"Valor esperado aproximado usando el método estratificado: {resultado}")
