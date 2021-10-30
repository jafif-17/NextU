import os
from Operations import *
from Person import *

#object operations
#do the essential transaction operations 
operaciones = Operations()
#if this arch don't exist, call to the endpoint for get the information
#and create "data.txt"
if(not(os.path.exists('./coinsData.json'))):
    operaciones.getInfo()

#create person1
p1 = Person("Ehecatzin","12342")
p1.addCoin("BTC", 2)
p1.addCoin("ELON", 2)
p1.addCoin("REN", 2)

#create person2
p2 = Person("Brian", "45674")
p2.addCoin("BTC", 2)




#add all persons
persons = [p1,p2]

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

    #read de option
    option = int(input())

    if(option == 1):
        operaciones.doTrans(p1, p2, 1, persons)

    if(option == 2):
        operaciones.doTrans(p1, p2, 2, persons)

    if(option == 3):
        coin = input("Ingresa el nombre de la moneda, que deseas verificar ")
        band =  operaciones.verifyCoin(coin)
        if(band == False):
            print("Verifica el nombre de la moneda")

        while(band == False):
            coin = input("Ingresa el nombre de la moneda, que deseas verificar ")
            band =  operaciones.verifyCoin(coin)
            print("Verifica el nombre de la moneda")
        
        print("El valor actual en DLS es : {}".format(operaciones.toDolar(coin, 1)))

    if(option == 4):
        print("De acuerdo a tus monedas existentes :\n")
        print("para {}".format(p1.getName()))
        p1.showBalanceOfCoins()
        print("para {}".format(p2.getName()))
        p2.showBalanceOfCoins()


    if(option == 5):
        if(p1.getLenOfHistory() >= 1):

            print("Historico para {}".format(p1.getName()))
            p1.showMyHistory()
        else:
            print("Historico para {}".format(p1.getName()))
            print("Aun no existe registro")
        if(p2.getLenOfHistory() >= 1):
            print("Historico para {}".format(p2.getName()))
            p2.showMyHistory()
        else:
            print("Historico para {}".format(p2.getName()))
            print("Aun no existe registro")

    if(option == 6):
        print("Nos vemos pronto :)")
        break