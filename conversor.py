def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes ? : ")
    pesos = float(pesos)
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print("Tines la cantidad de " + dolar + " Dólares")


menu = """
Bienvenido al conversor de monedas 💰

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos
Elije una opción: """

opcion = input(menu)

if opcion == '1':
    conversor("Colombianos", 3875)
elif opcion == '2':
    conversor("Argentinos", 65)
elif opcion == '3':
    conversor("Mexicanos", 24)
else:
    print('Ingresa la opción correcta')
