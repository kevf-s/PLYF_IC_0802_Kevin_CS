import math

class Principal:
    @staticmethod
    def main(args):
        #casting a nivel de dato
        Principal.engine(lambda x, y : x+y)
        Principal.engine(lambda x, y : x*y)
        Principal.engine(lambda x, y : x/y)
        Principal.engine(lambda x, y : x-y)
        Principal.engine(lambda x, y : math.fmod(x, y))
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
