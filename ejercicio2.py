import json

def clientemayor(data):
#Se tiene un archivo en formato Json con la información de ahorradores de un banco: Id, Nombre, nimCuenta y Saldo.Elabore un programa Python que lea este archivo y genere otro archivo en el mismo formato con la siguiente información: Consecutivo, NumCuenta y Saldo, solamente para aquellos ahorradores que tengan en su saldo un valor superior a 35 millones de pesos.
    cont = 0
    datosnuevos ={}
    datosnuevos['clients'] = []
    for elem in data['cliente']:
        if elem ['Saldo']> 35000000:
            cont = cont +1

            datosnuevos['clients'].append({
                'consecutivo': cont,
                'numero_cuenta': elem['NumCuenta'],
                'saldo': elem['Saldo']
            })

with open('Ahorradores.json') as file:
    data = json.load(file)
