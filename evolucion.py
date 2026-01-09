import math

def simulador_evolucion_wesker():
    print("\n" + "="*45)
    print("   ARCHIVOS SECRETOS: PROYECTO EVOLUCIÓN")
    print("="*45)
    
    # --- BLOQUE DEL PASADO ---
    trabajo_pasado = 100 
    recursos_pasados = 0.5
    enfoque_pasado = 0  
    tiempo_pasado = 1
    
    e_pasado = ((trabajo_pasado + recursos_pasados) * (enfoque_pasado**2)) / tiempo_pasado

    print(f"\nANÁLISIS PASADO (Edad 20):")
    print(f"Resultado Éxito (E): {e_pasado}")
    print("Nota: El enfoque 0 anuló todo el esfuerzo previo.")

    print("\n" + "-"*30)
    print("CONFIGURACIÓN PRESENTE (Edad 21 - UNLP)")
    
    try:
        # --- BLOQUE DE ENTRADA DE DATOS ---
        en_presente = float(input("Ingresá tu nivel de ENFOQUE hoy (1-10): "))
        re_presente = float(input("Ingresá tus RECURSOS hoy (PC, UNLP, Libros): "))
        tr_presente = float(input("Horas de TRABAJO/ESTUDIO invertidas: "))

        # --- NUEVO BLOQUE DE SELECCIÓN DE TIEMPO ---
        print("\nSeleccione el periodo de tiempo de la meta:")
        print("1) 1 Mes (Intensivo)")
        print("2) 4 Meses (Cuatrimestre UNLP)")
        print("3) 6 Meses (Semestre)")
        print("4) 12 Meses (1 Año)")
        
        opcion_t = input("Elija una opción (1-4): ")

        if opcion_t == "1":
            ti_presente = 1
        elif opcion_t == "2":
            ti_presente = 4
        elif opcion_t == "3":
            ti_presente = 6
        elif opcion_t == "4":
            ti_presente = 12
        else:
            print("Opción no válida, usando 1 mes por defecto.")
            ti_presente = 1

        # --- CÁLCULO FINAL ---
        e_presente = ((tr_presente + re_presente) * (en_presente**2)) / ti_presente

        print(f"\nANÁLISIS ACTUAL:")
        print(f"Resultado Éxito (E): {e_presente:.2f}")
        
        crecimiento = e_presente - e_pasado
        print(f"\nEVOLUCIÓN NETA: +{crecimiento:.2f} puntos de eficiencia.")
        
        if en_presente > 0:
            print("\nWESKER: 'Finalmente has entendido. El enfoque es el catalizador.'")

    except ValueError:
        print("Error: Ingresá números válidos, espécimen.")

if __name__ == "__main__":
    simulador_evolucion_wesker()