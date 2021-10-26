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
    def doTrans(personA,personB,moneda,cantidad,id,FlagTrans):
        #recibir
        if(FlagTrans == 1):
            if(personB.id == id):

                if(personB.verifyCripto(moneda) == True):
                    
                    if(cantidad <= personB.criptoStatus(moneda)):
                        personA.addCantidad(moneda,cantidad)
                        t = Transaccion(moneda, cantidad, 1)
                
                        print("Transaccion exitosa")
                        personB.subCantidad(moneda,cantidad)
                    else:
                        print("No tienes el saldo suficiente")
                else:
                    print("No tienes esa criptoMoneda")

            else:
                print("ID no valido")
        


    


           





      
      

       

     
       
     






