

totalCompra = float(input("Ingrese el precio final de la compra: "))

if totalCompra >= 500:
    descuentoAplicado = totalCompra*0.50
    print(f"Felicitaciones su compra es {descuentoAplicado}")
else:
    print(f"El pago es de:{totalCompra} ")

print("----------Muchas Gracias-----------")