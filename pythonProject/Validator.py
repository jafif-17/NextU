import requests
from Persona import *
from Transaccion import *
class Validator:
    
    @staticmethod
    #aqui recibe la cadena
    def verificaMoneda(moneda):
        nombre = moneda
        monedas_list=[]
        COINMARKET_API_KEY = "0e30af23-a662-4376-8dfd-1c6e9af22d9a"
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
        }
        data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
        for cripto in data["data"]:
            monedas_list.append(cripto["symbol"])
        
        return (nombre in monedas_list)
  
    @staticmethod
    #solo recibe nombre
    def toDolar(nomMoneda):
        
        #ruta
        _ENDPOINT = "https://api.binance.com/api/v3/ticker/price?symbol="+nomMoneda+"USDT"
        data = requests.get(_ENDPOINT).json()
        return data["price"]
    

    @staticmethod
    def showmeCriptos():
        #array de monedas
        monedas_list = [ ]
        COINMARKET_API_KEY = "0e30af23-a662-4376-8dfd-1c6e9af22d9a"
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
        }
        data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
        #cripto es un obejto del tipo de la respuesta
        #manzanas = [       ]
        #for manzana in manzanas foreach en java
        for cripto in data["data"]:
            print("- - - - - - - - - - - - - - - - - - - - - - - -")
            #imprimo los datos que yo quiero de esa informacion
            print(cripto["symbol"], cripto["quote"]["USD"]["price"])
            print("- - - - - - - - - - - - - - - - - - - - - - - -")

    @staticmethod
    def doTrans(personA,personB,moneda,cantidad,id,FlagTrans):
        #recibir
        #checar si es la bandera de recibir (osea 1)
        if(FlagTrans == 1):
            #remitente es personB
            #Beneficiario es personA
            #verificar que el id deel remitente sea igual al que meten por consola
            if(personB.id == id):
                #verificar si tiene la moneda que quiere enviar 
                if(personB.verifyCripto(moneda) == True):
                    
                    if(cantidad <= personB.criptoStatus(moneda)):
                        personA.addCantidad(moneda,cantidad)
                        #transaccion para remitente           
                        trem = Transaccion(moneda, cantidad, 1,personB,personA)
                        #se añade al historial del remiente
                        personB.addToHistorial(trem)
                        #transaccion para beneficiario
                        tben = Transaccion(moneda, cantidad, 2,personB,personA)
                        personA.addToHistorial(tben)
                        #Si todo sale perron
                        print("Transaccion exitosa")
                        personB.subCantidad(moneda,cantidad)
                    else:
                        print("No tienes el saldo suficiente")
                else:
                    #si no tiene esa cripto
                    print("No tienes esa criptoMoneda")

            else:
                print("ID no valido")

        #si no es 1 (recibir ) es envio
        else:
            #checar id del beneficiario (personB)
            if(personB.id == id):
                #verificar si tiene la modena que quiere enviar
                if(personA.verifyCripto(moneda) == True):
                    #checar la cantidad
                    #si la cantidad es menor a la que tiene se hace el envio sin problemas
                    if(cantidad <= personA.criptoStatus(moneda)):
                        #como A es el que envia le resto a su monenda
                        personA.subCantidad(moneda, cantidad)
                        #transaccion para A es un envio           
                        trem = Transaccion(moneda, cantidad,2,personA,personB)
                        #se añade al historial del remiente
                        personA.addToHistorial(trem)
                        #transaccion para beneficiario
                        tben = Transaccion(moneda, cantidad,1,personA,personB)
                        personB.addToHistorial(tben)
                        print("Transaccion exitosa")
                        personB.addCantidad(moneda, cantidad)
                        
                    #sino
                    else:
                        print("No tienes el saldo suficiente")

                else:
                    print("No tienes esa cripto moneda")

            else:
                print("ID incorrecto")

        



    


           





      
      

       

     
       
     






