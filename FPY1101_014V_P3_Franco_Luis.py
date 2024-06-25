import os
import random
os.system("cls")
def validar_patente(patente):
    if len(patente) != 6:
        return False
    consonantes = 'ABCDFGHJKLPQRSTVWXYZ'
    if (patente[:4].upper() != patente[:4]) or (not patente[4:].isdigit()):
        return False
    for letra in patente[:4].upper():
        if letra not in consonantes:
            return False
    return True

#

def validar_precio(precio):
    if precio > 5000000:
        return True
    else:
        return False

vehiculos = []

def grabar_vehiculo():
    tipo = input("Ingrese el tipo de vehículo: ")

    patente = input("Ingrese la patente del vehículo (4 consonantes y 2 números): ")
    while not validar_patente(patente):
        patente = input("Patente incorrecta. Ingrese nuevamente la patente del vehículo: ")

    marca = input("Ingrese la marca del vehículo (entre 2 y 15 caracteres): ")
    while len(marca) < 2 or len(marca) > 15:
        marca = input("Marca incorrecta. Ingrese nuevamente la marca del vehículo: ")

    precio = int(input("Ingrese el precio del vehículo (mayor a $5,000,000): "))
    while not validar_precio(precio):
        precio = int(input("Precio incorrecto. Ingrese nuevamente el precio del vehículo: "))

    multas = int(input("Ingrese el número de multas: "))
    fecha_multas = []
    for i in range(multas):
        fecha_multas.append((random.randint(1500, 3500), random.randint(1, 31)))

    fecha_registro = input("Ingrese la fecha de registro del vehículo: ")
    run_dueno = input("Ingrese el RUN del dueño del vehículo: ")
    nombre_dueno = input("Ingrese el nombre del dueño del vehículo: ")

    vehiculo = {
        "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "precio": precio,
        "multas": multas,
        "fecha_registro": fecha_registro,
        "run_dueno": run_dueno,
        "nombre_dueno": nombre_dueno
    }

    vehiculos.append(vehiculo)
    print("Vehículo registrado exitosamente.")

def buscar_vehiculo():
    patente_buscar = input("Ingrese la patente del vehículo a buscar: ")
    encontrado = False
    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente_buscar:
            print(f"Vehículo encontrado:")
            print(f"Tipo: {vehiculo['tipo']}")
            print(f"Patente: {vehiculo['patente']}")
            print(f"Marca: {vehiculo['marca']}")
            print(f"Precio: ${vehiculo['precio']}")
            print(f"Multas: {vehiculo['multas']}")
            print(f"Fecha de registro: {vehiculo['fecha_registro']}")
            print(f"RUN del dueño: {vehiculo['run_dueno']}")
            print(f"Nombre del dueño: {vehiculo['nombre_dueno']}")
            encontrado = True
            break
    if not encontrado:
        print("Vehículo no encontrado.")

def imprimir_certificados():
    patente = input("Ingrese la patente del vehículo para imprimir certificados: ")
    encontrado = False
    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente:
            print(f"Certificado para el vehículo con patente {vehiculo['patente']}:")
            print(f"Nombre del dueño: {vehiculo['nombre_dueno']}")
            print(f"Fecha de registro: {vehiculo['fecha_registro']}")
            print("Certificado impreso correctamente.")
            encontrado = True
            break
    if not encontrado:
        print("Vehículo no encontrado.")


#menu inciall

def menu():
    while True:
        print("----- Menu Principal -----")
        print("1. Grabar vehículo")
        print("2. Buscar vehículo por patente")
        print("3. Imprimir certificados")
        print("4. Salir del programa")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            grabar_vehiculo()
        elif opcion == '2':
            buscar_vehiculo()
        elif opcion == '3':
            imprimir_certificados()
        elif opcion == '4':
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción inválida. Por favor ingrese una opción válida.")

menu()
