from turtle import st


dolar = input("Cuantos dolares tienes ?: ")
dolar = float(dolar)

valor_peso = 0.00024
peso = dolar / valor_peso
peso = round(peso, 2)
peso = str(peso)

print("Usted tiene :" + peso + " Pesos Colombianos")
