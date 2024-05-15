#Operadores aritmeticos 
## + - * / % ** //


#Operadores Relacionales 
# == != > >= < <=

"""
x=2
y=3
print(x!=y)

"""

#Operadores Lógicos 
#and or not

"""
print(True and True)
print(not False)

"""
#Condicional Simple
"""
user  = "Joel23"

if user == "Joel23":
    print("User correct")

"""

#condicional doble 

"""
user = "Joel123"
if (user=="Joel123"):
    print("User correct")
else:
    print("User denied")

"""

#condicional anidada

user ="Joel1234"
rol = "admin"

if(user=="Joel1234"and rol=="admin"):
    print("Welcome user admin ")
    status = True
    if status == True:
        print("Profile")
    else: 
        print("Guest")
elif(user=="Joel1234"and rol=="employee"):
    print("Welcome user emmployee")
elif(user=="Byron "and rol=="secretary"):
    print("Welcome user Secretary")
else : 
    print("User and rol not found")
