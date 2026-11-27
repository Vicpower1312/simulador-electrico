
# ==========================================
# PROYECTO: SIMULADOR DE CARGAS ELECTRICAS
# Mecanica y Electromagnetismo
# ==========================================

# Constante de Coulomb
K = 8.99e9

# Cargas electricas (Coulombs)
q1 = 2e-6
q2 = 3e-6

# Posiciones sobre el eje X (metros)
x1 = 0
x2 = 3


# ------------------------------------------
# 1. CALCULAR DISTANCIA
# ------------------------------------------

def calcular_distancia(x1, x2):
    distancia = abs(x2 - x1)
    return distancia


# ------------------------------------------
# 2. CALCULAR FUERZA ELECTRICA EN 1D
# ------------------------------------------

def calcular_fuerza_1d(q1, q2, x1, x2):

    distancia = calcular_distancia(x1, x2)

    # Componente de la fuerza sobre q1
    fuerza_x = K * q1 * q2 * (x1 - x2) / distancia**3

    return fuerza_x


# ------------------------------------------
# 3. PROGRAMA PRINCIPAL
# ------------------------------------------

def main():

    distancia = calcular_distancia(x1, x2)

    fuerza_x = calcular_fuerza_1d(q1, q2, x1, x2)

    magnitud = abs(fuerza_x)

    print("SIMULADOR DE CARGAS ELECTRICAS")
    print("--------------------------------")

    print(f"Carga 1: {q1} C")
    print(f"Carga 2: {q2} C")

    print(f"Posicion q1: {x1} m")
    print(f"Posicion q2: {x2} m")

    print("--------------------------------")

    print(f"Distancia: {distancia} m")
    print(f"Fuerza sobre q1: {magnitud:.7f} N")
    print(f"Componente Fx: {fuerza_x:.7f} N")

    if fuerza_x > 0:
        print("Direccion: Hacia la derecha (+X)")
    elif fuerza_x < 0:
        print("Direccion: Hacia la izquierda (-X)")
    else:
        print("Fuerza nula")


# Ejecutar programa
if __name__ == "__main__":
    main()
