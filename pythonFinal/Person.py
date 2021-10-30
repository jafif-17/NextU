from Operations import *
class Person:

    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.coins = []
        self.history = []
        self.op = Operations()

    def getLenOfHistory(self):
        return len(self.history)

    def getID(self):
        return self.id
    
    def getName(self):
        return self.name

    def addHistory(self,trans):
        self.history.append(trans)
    
    def showMyHistory(self):
        for i in self.history:
            print(i)
       
    #this method add a coin in coins
    def addCoin(self,coin,cant):
        final = {}
        #if coin exist !
        if(self.op.verifyCoin(coin) == True):
            dolars = self.op.toDolar(coin,cant)
            cripto = dict(coin = coin, cant = cant , USD = dolars)
            final[coin] = cripto  
            self.coins.append(final)
        else:
            print("Error, verifica el nombre de la criptomoneda")
    

    def getCantOfCoin(self,coin):
        cant = 0
        band,position = self.searchCoin(coin)
        if(band == True):
            cant = self.coins[position-1][coin]["cant"]
            return cant
        else:
            print("Ocurrio un error")

   


    def showMyCoins(self):
        for data in self.coins:
            print(data)

    
    def searchCoin(self,coin):
        band = False
        posicion = 0
        for c  in self.coins:
            for k in c.keys():
                if(coin == k):
                    band = True
                    break
            posicion = posicion +1

        return band,posicion

    
    def SumCoin(self,coin,cant):
        #I have the coin in my list of coins
        dolar = self.op.toDolar(coin, cant)
        band,posicion = self.searchCoin(coin)  
        if(band == True):
            self.coins[posicion-1][coin]["cant"] = self.coins[posicion-1][coin]["cant"]  + cant
            self.coins[posicion-1][coin]["USD"] = self.coins[posicion-1][coin]["USD"]  + dolar
        #if I haven't the coin , add to the list of my coins
        else:
            self.addCoin(coin, cant)
    

    def SubCoin(self,coin,cant):
        #I have the coin in my list of coins
        dolar = self.op.toDolar(coin, cant)
        band,posicion = self.searchCoin(coin)  
        if(band == True):
            self.coins[posicion-1][coin]["cant"] = self.coins[posicion-1][coin]["cant"]  - cant
            self.coins[posicion-1][coin]["USD"] = self.coins[posicion-1][coin]["USD"]  - dolar
        #if I haven't the coin , add to the list of my coins
        else:
            print("Verifica la existencia de la moneda")


    def showBalanceOfCoin(self,coin):
        if(self.op.verifyCoin(coin) == True):
            band,position = self.searchCoin(coin)
            if(band == True):
                return self.op.toDolar(coin, 1)
            else:
                print("Error : No cuentas con {}".format(coin))
        
        else:
            print("Ocurrio un Error , verifica el nombre de la moneda")
    

    def showBalanceOfCoins(self):
        for c in self.coins:
            for k in c:
                
                print("Coin {} : {}".format(k,self.showBalanceOfCoin(k)))


      
           
        





