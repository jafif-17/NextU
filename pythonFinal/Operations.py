import requests
import json
from datetime import datetime

class Operations:
    
    def __init__(self):

        self.COINMARKET_API_KEY = "2448e9c9-b938-4f0e-85f1-9878a7b41c87"

    def getInfo(self):
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': self.COINMARKET_API_KEY
        }
        coins_json = {}
        data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

        for cripto in data["data"]:
            coinInfo = dict(name=cripto["slug"],valueDSD = cripto["quote"]["USD"]["price"])
            coins_json[cripto['symbol']] = coinInfo
        

        with open('coinsData.json','w') as output:
            data_json = coins_json
            json.dump(data_json,output)


    def toDolar(self,coin,cant):
        f = open("./coinsData.json","r")
        data = json.loads(f.read())
        f.close()
        usd = 0
        if(self.verifyCoin(coin) == True):
            for cripto in data:
                if(cripto == coin):
                    usd = float(data[cripto]["valueDSD"]) * float(cant)
        
            return usd

        else:
            return -1

    
    def verifyCoin(self,coin):
        #read info from created arch
        f = open("./coinsData.json","r")
        data = json.loads(f.read())
        f.close()
        band = False
        #the name of cripto is a key 
        #I'm iterating that keys if that key is equal coin
        #I can say that the coin exist ,and change the value of band = true
        for cripto in data:
            if(cripto == coin):
                band = True
                break
        
        
        return band

    
    def doTrans(self,personA,personB,typeTrans,arrPersons):
        #case(1) "envio" : person A is a Remitente, person B is a beneficiario
        #case(2) "Recibir" : personA is a Beneficiario , person B is a Remitente
       
        #check type of trans
        bandRem = False
        bandBen = False
        if((typeTrans == 1 ) or (typeTrans == 2)):
            #while id is wrong 
            while(bandRem == False):
                idRem = input("ingresa tu ID : ")
            
                for p in arrPersons:
                    if(idRem == p.getID()):
                        bandRem = True
                    
                if(bandRem == False):
                    print("ID incorrecto")
                else:
                    break

            while(bandBen == False):
                idBen = input("ingresa ID del beneficiario : ")

                for person in arrPersons:
                    if(idBen == person.getID()):
                        bandBen = True
                
                if(bandBen == False):
                    print("ID incorrecto")
                else:
                    break
            
            
            coin = input("Ingresa Moneda a enviar : ")
            while(self.verifyCoin(coin) == False):
                coin = input("Ingresa Moneda válida : ")

            cant = int(input("Ingresa la cantidad : "))
            while(cant < 0):
                cant = int(input("Ingresa cantidad valida : "))
            
            if(cant > personA.getCantOfCoin(coin)):
                print("Error : Verifica la cantidad que intentas enviar")
            else:
                fecha = datetime.today().strftime('%Y-%m-%d %H:%M')
                personA.SubCoin(coin,cant)

                #si es (1)
                if(typeTrans == 1):
                    personA.SubCoin(coin, cant)
                    #construir transaccion para personA
                    transA = dict(enviadoA = personB.getName(), coin = coin , cantidad = cant, USD = self.toDolar(coin, cant), fechaTransferencia =  fecha)
                    personA.addHistory(transA)
                    transB = dict(recibidoDe = personA.getName(), coin = coin , cantidad = cant, USD = self.toDolar(coin, cant), fechaTransferencia = fecha )
                    #construir transaccion para personB
                    personB.SumCoin(coin, cant)
                    personB.addHistory(transB)
                    print("Transferencia exitosa")
                    #person A subs de cant , person B add that cant
                else:

                    personB.SubCoin(coin, cant)
                    #construir transaccion para personA
                    transB = dict(enviadoA = personA.getName(), coin = coin , cantidad = cant, USD = self.toDolar(coin, cant), fechaTransferencia =  fecha)
                    personB.addHistory(transB)
                    personA.SumCoin(coin, cant)
                    transA = dict(recibidoDe = personB.getName(), coin = coin , cantidad = cant, USD = self.toDolar(coin, cant), fechaTransferencia = fecha )
                    #construir transaccion para personB
                    personA.addHistory(transA)
                    print("Transferencia exitosa")
                    #person A subs de cant , person B add that cant

            



            
        
           


            
            





        




