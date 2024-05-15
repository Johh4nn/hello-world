#librerias 

import webbrowser 

print("Bienvenido, Byron")
dia = input("Ingrese un dia de la semana: ")

match(dia):
    case "lunes":
        print("Hoy debes, hacer ejercicios")
    case "martes":
        print("Hoy debes, hacer las compras")
    case "miercoles":
        print("Hoy debes, ver peliculas")
        print("¿Deseas que te recomiende un canal?")
        tipWeb = input("Dime si o no ")
        if tipWeb == "si":
            webbrowser.open_new_tab("https://www.disneyplus.com")
    case "jueves":
        print("Hoy debes, hacer deberes")
    case "viernes":
        print("Hoy debes, jugar futbol")
    case _:
        print("No existe actividad para ese dia")