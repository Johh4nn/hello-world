#Declaracion de librerias
COSTO_ROJAS = 0.75
COSTO_GIRASOLES = 0.5
COSTO_CLAVELES = 1.25
COSTO_DALIAS = 0.95

#Programa para determinar el precio de una venta realizada en una floristeria

#Declaracion de varibales

#Solicitacion de datos al usuario
nombre = input("Ingresa tu nombre: ")
correo_electronico = input("Ingresa tu correo: ")
cedula = input("Ingresa tu cédula: ")
print("Ingresa el número de flores para el arreglo")
floresRojas = int(input("Rojas: "))
girasoles = int(input("Girasoles:"))
claveles = int(input("Claveles: "))
dalias = int(input("Dalias: "))

#realizar el procedimiento

totRojas=floresRojas*COSTO_ROJAS
totGirasoles=girasoles*COSTO_GIRASOLES
totClaveles= claveles*COSTO_CLAVELES
totDalias = dalias*COSTO_DALIAS

tot=totClaveles+totDalias+totGirasoles+totRojas

pagoConIva=tot*(1.15)

#imprime resultados

print("-------------------Factura Electrónica--------------")
print(f"Usuario {nombre}")
print(f"El subtotal es de  {round(tot,2)} $")
print(f"El total es de {round(pagoConIva,2)} $")
print(f"La factura se enviara a su correo electrónico {correo_electronico}")
print("----------------------Muchas Gracias----------------")
