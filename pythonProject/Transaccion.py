from datetime import datetime
class Transaccion:

    def __init__(self,moneda,cantidadTrans,tipo,remitente,beneficiario):
        self.moneda = moneda
        self.cantidad = cantidadTrans
        self.tipoTrans = self.asignaTipo(tipo)
        self.idRem = remitente.id
        self.idBen = beneficiario.id
        self.fecha = datetime.today().strftime('%Y-%m-%d %H:%M')

    def asignaTipo(self,tipo):
        if(tipo == 1):
            return "Recibido"
        else:
            return "Enviado"


    def mostrarInfo(self):
        print("Moneda: {}".format(self.moneda))
        print("Cantidad: {}".format(self.cantidad))
        print("Tipo de transaccion: {}".format(self.tipo))
        print("Fecha de la transaccion: {}".format(self.fecha))