# aplicacion que administra un puesto de fruta

print == "hola bienvenido que desea comprar"

compra = ()


while True:
    print ("1. Añadir producto. ")
    print ("2. Eliminar producto ")
    print ("3. Ver lista del producto. ")
    print ("4. Cerrar programa. ")
    print ()
    opcion = input = ("--->")
    print ()
    




    if opcion == "1":
         producto = input ("Añadir producto").capitalize()
         if producto in compra:
             print ("ese producta ya esta en la lista")
         else:
             compra.append(producto)
             
    elif opcion == "2":
        producto = input ("Eliminar producto" ).capitalize()
        if producto not in compra:
            print ("Ese producto ha sido removido")
        else:
            compra.remove(producto)
     
    elif opcion == "3":
        producto = input
        print ("Lista de compra:")
        for e in (compra):
            print(" 3-"),e
            
    elif opcion == ("4"):
        break
    
    
    