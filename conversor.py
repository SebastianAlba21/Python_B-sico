pesos = input("Cuantos pesos Colombianos tienes ? : ")
pesos = float(pesos)

valor_rublo = 74.73
rublos = pesos / valor_rublo
rublos = round(rublos, 2)
rublos = str(rublos)

print("Tines la cantidad de " + rublos + " Rublos")
