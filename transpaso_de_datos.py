import json
listaventas = {}#Creacion diccionario
listaventas['Vendedores']=[]#cree una lista dentro de un dicc
with open ("ventas.txt", 'r') as file:#Definir un archivo
    lineas = file.readlines()#Almacenar las lineas en la variable lineas 

    for linea in lineas [1:]:
        datos = linea.strip().split(',')#quitar espacios y separar por comas 
        print(datos[0])
        listaventas['Vendedores'].append(
            {
                'Nombre':datos[0],
                'Id':datos[1],
                'Ventas':datos[2:9]
            }
        )
        with open ('ventas.json','w') as file2:
            json.dump(listaventas,file2, indent=4)