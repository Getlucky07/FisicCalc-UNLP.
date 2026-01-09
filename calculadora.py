import math

def iniciar_sistema():
    while True:
        print("\n========================================")
        print("   SISTEMA FISIC-CALC UNLP (V2.0)")
        print("========================================")
        print("1. MRU (Velocidad Constante)")
        print("2. MRUV (Con Aceleración)")
        print("3. SALIR")
        
        opcion_principal = input("\nSeleccione el tipo de movimiento: ")

        if opcion_principal == "3":
            print("Cerrando sistema... ¡Éxitos en la cursada!")
            break

        try:
            if opcion_principal == "1":
                menu_mru()
            elif opcion_principal == "2":
                menu_mruv()
            else:
                print("Opción no válida.")
        except Exception as e:
            print(f"Error detectado: {e}")

def menu_mru():
    print("\n--- Cálculos de MRU ---")
    print("1. Velocidad | 2. Distancia | 3. Tiempo")
    op = input("Seleccione: ")
    if op == "1":
        d = float(input("Distancia (m): "))
        t = float(input("Tiempo (s): "))
        print(f"--> Velocidad: {d/t:.2f} m/s")
    # (Aquí sigue el resto de la lógica de MRU que ya tenías)

def menu_mruv():
    print("\n--- Cálculos de MRUV (Aceleración) ---")
    print("¿Qué desea calcular?")
    print("1. Velocidad Final (vf = vi + a*t)")
    print("2. Distancia (d = vi*t + 0.5*a*t^2)")
    
    op = input("Seleccione: ")
    
    vi = float(input("Velocidad Inicial (m/s): "))
    a = float(input("Aceleración (m/s²): "))
    t = float(input("Tiempo (s): "))
    
    if op == "1":
        vf = vi + (a * t)
        print(f"--> Velocidad Final: {vf:.2f} m/s")
    elif op == "2":
        dist = (vi * t) + (0.5 * a * (t**2))
        print(f"--> Distancia recorrida: {dist:.2f} m")

if __name__ == "__main__":
    iniciar_sistema()