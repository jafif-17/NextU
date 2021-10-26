from Persona import *

#from Validator import *
#solamente creare dos personas
p1 = Persona("Ehecatzin",25,"Mexicana",123452)
p1.agregarMoneda("BTC", 1)
p2 = Persona("Brian",26,"Mexicana",23453)
p2.agregarMoneda("BTC", 2)

print("Bienvenido a tu sistema, por favor selecciona la operación a realizar. ")
print(""" 

Digita'1' = Recibir cantidad
Digita'2' = Transferir monto
Digita'3' = Mostrar balance una moneda
Digita'4' = Mostrar balance general
Digita'5' = Mostrar histórico de transacciones
Digita'6' = Salir del programa

""")
opcion = int(input())
if(opcion == 1):
    print("¿Que moneda vas a recibir?")
    moneda = str(input())
    print("Cantidad a recibir")
    cantidad = int(input())
    print("Ingresa id del remitente")
    idrem = int(input())
    Validator.doTrans(p1, p2, moneda, cantidad, idrem, 1)
    print("beneficiario")
    p1.listaMonedas[0].mostrarInfo()
    print("Remitente")
    p2.listaMonedas[0].mostrarInfo()


    