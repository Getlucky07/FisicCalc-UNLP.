def convertir_tiempo(valor, unidad):
    """
    Convierte el tiempo ingresado a días.
    """
    if unidad == "dias":
        return valor
    elif unidad == "semanas":
        return valor * 7
    elif unidad == "meses":
        return valor * 30
    elif unidad == "trimestres":
        return valor * 90   # 3 meses ≈ 90 días
    elif unidad == "semestres":
        return valor * 180  # 6 meses ≈ 180 días
    elif unidad == "años":
        return valor * 365
    elif unidad == "cuatrimestres":
        return valor * 120  # 4 meses ≈ 120 días
    else:
        raise ValueError("Unidad de tiempo no válida. Use: dias, semanas, meses, trimestres, semestres, cuatrimestres, años.")

def calcular_exito(trabajo, recursos, enfoque, tiempo_valor, tiempo_unidad):
    """
    Calcula el éxito según la fórmula:
    E = ((T + R) * e^2) / t
    """
    t = convertir_tiempo(tiempo_valor, tiempo_unidad)
    E = ((trabajo + recursos) * (enfoque ** 2)) / t
    return E

def simulador_exito():
    print("\n" + "="*45)
    print("   SIMULADOR DE ÉXITO PERSONAL (v3.0)")
    print("="*45)

    try:
        enfoque = float(input("Ingresá tu nivel de ENFOQUE hoy (1-10): "))
        recursos = float(input("Ingresá tus RECURSOS hoy (PC, UNLP, Libros): "))
        trabajo = float(input("Horas de TRABAJO/ESTUDIO invertidas por día: "))
        tiempo_valor = float(input("Ingrese cantidad de tiempo: "))
        tiempo_unidad = input("Unidad de tiempo (dias/semanas/meses/trimestres/semestres/cuatrimestres/años): ").lower()

        resultado = calcular_exito(trabajo, recursos, enfoque, tiempo_valor, tiempo_unidad)
        print(f"\n--> Nivel de Éxito calculado: {resultado:.2f}")

    except ValueError:
        print("Error: Ingresá números válidos.")

if __name__ == "__main__":
    simulador_exito()
