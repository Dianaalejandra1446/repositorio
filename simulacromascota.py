"""Simulacro CICLO 1
 Elabore un programa Python para gestionar el CRUD del archivo de datos PetShopping.json con las siguientes funcionalidades:Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio 
 Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios Actualizar los datos de una mascota consultada por índice (Mostrar el listado total y elegir por índice) Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice)"""

import json

def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("-"*75)
            print("Ingrese un numero entero valido")


def leerString(msg):
    while True:
        try:
            n = input(msg)
            if n.strip() == "":
                print("Error! Ingrese el nombre valido.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError as e:
            print("Error! Hay que ingresar el nombre.")


def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("---> Presione ENTER para continuar")



def menu():
    print('----MENU PetShopping----\n')
    print('|1.Elegir mascota          |')
    print('|2.Crear nueva Mascota     |')
    print('|3.Mostrar o buscar mascota|')
    print('|4.Actualizar datos mascota|')
    print('|5.Eliminar mascota        |')
    print('|6.Salir                   |')
    print('>>Elige una opcion de 1 a 5')
    elegirop = leerInt('Ingrese un numero para acceder al menu: ')
    if elegirop < 1 or elegirop > 6:
        msgError('Ingrese una opcion valida')
    return elegirop

def elegir():
    print('     MASCOTAS DISPONIBLES:\n')
    for elem in datosmascotas["pets"]:
        print('_'*30,'\n')
        print('Tipo: ','-'*5,elem["tipo"],'\n')
        print('Raza: ','-'*5,elem["raza"],'\n')
        print('Precio:','-'*5,elem["precio"],'\n')
        servicios = ", ".join(elem["servicios"])
        print(f'Servicios: {servicios}')
    input("---> Presione ENTER para continuar")

def crear(datosmascotas):
    datosmascotas['pets']=[]
    print('     INGRESAR MASCOTA:\n')

    IngresaTipo = leerString("Ingresar tipo de mascota:")
    IngresaRaza = leerString("Ingresar tipo de raza: ")
    IngresaPrecio = leerInt("Ingresar precio mascota: ")
    IngresaServicio = leerString("Ingrese servicios mascota: ")

    datosmascotas["pets"].append({
        'tipo':IngresaTipo,
        'raza':IngresaRaza,
        'precio':IngresaPrecio,
        'servicios':IngresaServicio
    })
    #datosmascotas.append(["pets"])
    with open('PetShopping.json','w',encoding="utf-8")as archivo:
        json.dump(datosmascotas,archivo,indent=4)

    input("---> Presione ENTER para continuar")
    return datosmascotas

def buscar():
    pass
def actualizar():
    pass
def eliminar():
    pass



#CODIGO PRINCIPAL
datosmascotas = {}
with open('PetShopping.json','r',encoding="utf-8") as file:
    datosmascotas = json.load(file)

while True:
    elegirop = menu()
    if elegirop == 1:
        elegir()
    elif elegirop == 2:
        crear(datosmascotas)
    elif elegirop == 3:
        buscar()
    elif elegirop == 4:
        actualizar()
    elif elegirop == 5:
        eliminar()
    elif elegirop == 6:
        print('Saliendo del menu...')
        break
