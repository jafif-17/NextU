from Persona import *
from Validator import * 

#solamente creare dos personas como ejemplo
p1 = Persona("Ehecatzin",25,"Mexicana",123452)
p1.agregarMoneda("BTC", 1)
p2 = Persona("Brian",26,"Mexicana",23453)
p2.agregarMoneda("BTC", 2)

while(True):

    print("Bienvenido a tu sistema, por favor selecciona la operación a realizar. ")
    print(""" 
    - - - - - - - - - - - - - - - - - - - - - - - - - 
    Digita'1' = Recibir cantidad
    Digita'2' = Transferir monto
    Digita'3' = Mostrar balance una moneda
    Digita'4' = Mostrar balance general
    Digita'5' = Mostrar histórico de transacciones
    Digita'6' = Salir del programa
    - - - - - - - - - - - - - - - - - - - - - - - - - 
    """)
    #leer opcion
    opcion = int(input())
    if(opcion == 1):
        print("¿Que moneda vas a recibir?")
        moneda = str(input())
        print("Cantidad a recibir")
        cantidad = int(input())
        print("Ingresa id del remitente")
        idrem = int(input())
        Validator.doTrans(p1, p2, moneda, cantidad, idrem, 1)

    elif(opcion == 2):
        print("¿Que moneda vas a mandar?")
        moneda = str(input())
        print("Cantidad a enviar")
        cantidad = int(input())
        print("Ingresa id del beneficiario")
        idben = int(input())
        Validator.doTrans(p1, p2, moneda, cantidad, idben, 2)

    elif(opcion == 3):
        moneda = str(input("Ingresa el nombre de la criptomoneda \n"))
        if(Validator.verificaMoneda(moneda)):
            print("El valor actual de {} es {} ".format(moneda,Validator.toDolar(moneda)))
        else:
            print("Moneda no válida")

    elif(opcion == 4):
        print("Balcance general")
        Validator.showmeCriptos()
      

    elif(opcion == 5):
        if(len(p1.historial) >= 1):

            print("- - - - - - - - - - - - - - - - - ")
            print("Historial persona 1 : {}".format(p1.nombre))
            for t in p1.historial:
                t.mostrarInfo()
            print("- - - - - - - - - - - - - - - - - ")
        else:
            print("Aún no existen trasacciones para {}".format(p1.nombre))
        
        if(len(p2.historial) >= 1):
            print("Historial persona 2 : {}".format(p2.nombre))
            for t2 in p2.historial:
                t2.mostrarInfo()
            print("- - - - - - - - - - - - - - - - - ")
        else:
            print("Aún no existen trasacciones para {}".format(p2.nombre))
        
    
    else:
        print("Nos vemos pronto :)")
        break

    #print("\n\n\n\n\n\n\n")

    


    