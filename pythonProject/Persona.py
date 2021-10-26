from Criptomoneda import *
from Validator import Validator

class Persona:

    def __init__(self,nombre,edad,nacionalidad,id):
        self.nombre = nombre
        #self.id = u.uuid1()
        self.id = id
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.listaMonedas = []
        self.historial = []
    

    def verifyCripto(self,moneda):
        band = False
        str(moneda)
        for cripto in self.listaMonedas:
            if(str(cripto.nombre) == moneda):
                band = True
          
        return band


    def criptoStatus(self,nombreMoneda):
        cantidadBuscada= 0
        for moneda in self.listaMonedas:
            if(moneda.nombre == nombreMoneda):
                cantidadBuscada = moneda.cantidad
        
        return cantidadBuscada



    def mostrarInfo(self):

        print("{}".format(self.nombre))
        print("{}".format(self.id))
        print("{}".format(self.edad))
        print("{}".format(self.nacionalidad))

    def agregarMoneda(self,moneda,cantidad):
        #debemos verificar la moneda
        #para ver si existe o nel
        #creas un objeto moneda
        if(Validator.verificaMoneda(moneda) == True):
            nueva = Criptomoneda(moneda, cantidad)
            self.listaMonedas.append(nueva)
        else:
            print("Ingresa una criptomoneda válida")

    
    def subCantidad(self,moneda,cantidad):

        band = False
        #iterando sobre el tipo de dato 
        aux = 0
        for i in self.listaMonedas:
            if(moneda == i.nombre):
                band = True
            
            aux = aux+1
        
        if(band == True):
            self.listaMonedas[aux-1].cantidad = self.listaMonedas[aux-1].cantidad - cantidad
        else:
            moneda = Criptomoneda(moneda, cantidad)
            self.listaMonedas.append(moneda)

    
    def addCantidad(self,moneda,cantidad):
        band = False
        #iterando sobre el tipo de dato 
        aux = 0
        for i in self.listaMonedas:
            if(moneda == i.nombre):
                band = True
            
            aux = aux+1
        
        if(band == True):
            self.listaMonedas[aux-1].cantidad = self.listaMonedas[aux-1].cantidad + cantidad
        else:
            moneda = Criptomoneda(moneda, cantidad)
            self.listaMonedas.append(moneda)

        

           


      
      
       




