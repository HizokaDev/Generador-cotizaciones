# main.py
import gestor
import os

def menu():
    while True:
        os.system("clear")
        print("\n🧾 GESTOR DE COTIZACIONES 🧾")
        print("1. Crear nueva cotización")
        print("2. Buscar cotización por cliente")
        print("3. Editar cotización")
        print("4. Eliminar cotización")
        print("5. Ver cotización (vista previa)")
        print("6. Exportar cotización de un cliente")
        print("7. Salir")
       
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestor.crear_cotizacion()
        elif opcion == "2":
            gestor.buscar_cotizacion()
        elif opcion == "3":
            gestor.editar_cotizacion()
        elif opcion == "4":
            gestor.eliminar_cotizacion()
        elif opcion == "5":
            gestor.vista_previa()
        elif opcion == "6":
            gestor.exportar_cotizacion()
        elif opcion == "7":
            print("¡Hasta luego, Hizoka-sensei! 😼")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
        input("\nPresione Enter para continuar....")

# Iniciar programa

gestor.crear_archivo_si_no_existe()
gestor.limpiar()
menu()