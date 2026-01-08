import sys

def iniciar():
    print("\n========================================")
    print("   SISTEMA FISIC-CALC UNLP ACTIVADO")
    print("========================================\n")
    
    while True:
        print("¿Qué desea calcular?")
        print("1. Velocidad (d/t)")
        print("2. Distancia (v*t)")
        print("3. Tiempo (d/v)")
        print("4. SALIR")
        
        opcion = input("\nElija una opción (1-4): ")

        if opcion == "4":
            print("Cerrando sistema... ¡Éxitos, futuro Ingeniero!")
            break

        try:
            if opcion == "1":
                d = float(input("Distancia (m): "))
                t = float(input("Tiempo (s): "))
                print(f"--> Resultado: {d/t:.2f} m/s")
            elif opcion == "2":
                v = float(input("Velocidad (m/s): "))
                t = float(input("Tiempo (s): "))
                print(f"--> Resultado: {v*t:.2f} m")
            elif opcion == "3":
                d = float(input("Distancia (m): "))
                v = float(input("Velocidad (m/s): "))
                print(f"--> Resultado: {d/v:.2f} s")
            else:
                print("Opción inválida, intente de nuevo.")
        except Exception as e:
            print(f"Error en los datos: {e}")

if __name__ == "__main__":
    iniciar()