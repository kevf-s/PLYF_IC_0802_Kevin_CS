import math

class Principal:
    @staticmethod
    def main(args):
        #Casting a nivel de Interfaz
        objInt =lambda x, y : x+y
        Principal._engine(objInt)
        objInt=lambda x, y : x*y
        Principal._engine(objInt)
        objInt=lambda x, y : x/y
        Principal._engine(objInt)
        #-----
        objLong =lambda x, y : x-y
        Principal._engine(objLong)
        objLong=lambda x, y : math.fmod(x, y)
        Principal._engine(objLong)
    @staticmethod
    def _engine(cal):
        x =2
        y =4
        resultado = cal.calcular(x,y)
        print(resultado)
    @staticmethod
    def _engine(cal):
        x =2
        y =4
        resultado = cal.calcular(x,y)
        print(resultado)
