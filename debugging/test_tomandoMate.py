import unittest

class Mate:
    def tomar_mate(self):
        return
    
    def cambiar_yerba(self, cantidad_cebadas):
        self.cantidad_cebadas -= cantidad_cebadas

    def cambiar_agua(self, temperatura_agua):
        pass

    def tomar(self):
        if self.temperatura_agua > 80:
            mensaje = "Esta que pela!"
        elif self.temperatura_agua < 65:
            mensaje = "No sabia que era terere"
        else:
            mensaje = "Tomando el mate"
        
        print(mensaje)
        
