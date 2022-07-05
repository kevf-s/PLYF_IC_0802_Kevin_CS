import math

class Principal:
    @staticmethod
    def main(args):
        #Casting a nivel de Interfaz
        Principal._engine(lambda x, y : x+y)
        Principal._engine(lambda x, y : x*y)

        Principal._engine(lambda x, y : x/y)
        Principal.engine(lambda x, y : x-y)
        Principal._engine(lambda x, y : math.fmod(x, y))
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
