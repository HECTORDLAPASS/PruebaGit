print("holas")

nombre = input("Tu nombre: ")
telefono = input("Tu telefono: ")

i  =1
while i < 2:
    opcion = input("1. para ver nombre \n2. para ver telefono \n3. para ver todo \n...")

    if opcion == "1":
        print("tu nombre es",nombre)
        break
    elif opcion == "2":
        print("tu telefono es",telefono)
        break
    elif opcion == "3":
        print("tu nombre es",nombre, "tu telefono es",telefono)
        break
    else:
        print("opcion invalida")


print("estamos en una rama")