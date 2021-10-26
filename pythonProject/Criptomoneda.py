import requests
from Validator import *

class Criptomoneda:
    # va a tomar los datos de "esta" clase
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.cambioUSD = Validator.toDolar(nombre)
    

    def mostrarInfo(self):
        print("- - - - - - - - - - - - - - - -")
        print("Moneda {}".format(self.nombre))
        print("- - - - - - - - - - - - - - - -")
        print("Cantidad {}".format(self.cantidad))
        print("- - - - - - - - - - - - - - - -")
        print("Valor en DLS p/u  {}".format(self.cambioUSD))
        print("- - - - - - - - - - - - - - - -")


   


 





    
        

