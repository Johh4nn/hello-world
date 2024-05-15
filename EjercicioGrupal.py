#Ingreso de datos

nombre = input("Ingrese su nombre: ")
promedio = float(input("Ingrese el promedio de compras realizadas"))
edad = int(input("Ingrese su edad"))

if edad>=18 :
    if promedio >= 500:
        print("Gano un viaje a Estados Unidos")
    elif promedio > 300 and promedio <= 499:
        print("Gana un viaje a España")
    elif promedio >=200 and promedio <=299:
        print("Gano un viaje a Colombia")
    elif promedio >=100 and promedio <=199:
        print("Gano un viaje a Galapagos")


elif promedio >= 50 and promedio <= 99:
    print("Gano un viaje a guayaquil")

else:
    
    print("NO GANO NADA")
