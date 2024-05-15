#Declaracion de constantes

import time


#Entrada de datos 
precioCompra = float(input("Ingrese el precio final de compra: "))
cantidadPrendas = int(input("Ingrese la cantidad de prendas: "))

print("Procesando los datos ... ")

print("Por favor espere....")
time.sleep(3) #Eskeleton o loading 

if cantidadPrendas >= 21:
    descuento = 0.1* precioCompra
    precioFinal = precioCompra - descuento
    print(f"La cantidad de prendas fueron {cantidadPrendas}")
    print(f"El precio final a pagar es de {precioFinal}")
elif cantidadPrendas >=10 and cantidadPrendas <=20:
    descuento = 0.05* precioCompra
    precioFinal = precioCompra - descuento
    print(f"La cantidad de prendas fueron {cantidadPrendas}")
    print(f"El precio final a pagar es de {precioFinal}")

elif cantidadPrendas<= 9:
    print(f"La cantidad de prendas fueron {cantidadPrendas}")
    print(f"El precio final a pagar es de {precioCompra}")