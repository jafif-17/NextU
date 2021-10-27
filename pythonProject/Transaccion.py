from datetime import datetime
from Persona import * 
class Transaccion:

    def __init__(self,moneda,cantidadTrans,tipo,remitente,beneficiario):
        self.moneda = moneda
        self.cantidad = cantidadTrans
        self.remitente = remitente #objetos persona
        self.beneficiario = beneficiario #objetos persona
        self.fecha = datetime.today().strftime('%Y-%m-%d %H:%M')
        self.tipoTrans = self.asignaTipo(tipo)

    def asignaTipo(self,tipo):
        if(tipo == 1):
            return "Recibido"
        else:
            return "Enviado"     

    def mostrarInfo(self):
        #si es 1 es recibido
        if(self.tipoTrans == "Recibido"):
            print("Fecha de transaccion : {}".format(self.fecha))
            print("Tipo de transaccion: {}".format(self.tipoTrans))
            print("Moneda recibida : {}".format(self.moneda))
            print("Cantidad recibida : {}".format(self.cantidad))
            print("Recibido de :")
            self.remitente.infoTrans()
           
        else:
            print("Fecha de transaccion : {}".format(self.fecha))
            print("Tipo de transaccion: {}".format(self.tipoTrans))
            print("Moneda enviada : {}".format(self.moneda))
            print("Cantidad enviada : {}".format(self.cantidad))
            print("Enviado a:\n")
            self.beneficiario.infoTrans()
         

            
        