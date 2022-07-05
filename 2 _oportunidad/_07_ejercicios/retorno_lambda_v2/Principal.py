#mi solucion --> correcto
class Principal:
    @staticmethod
    def main(args):
        Principal.engine(lambda x, y :lambda x1, y2 : x1+y2)
    @staticmethod
    def _engine(cal):
        x =2
        y =4
        resultado = cal.calcular(x,y)
        print(resultado.calcular(int(x), int(y)))
    @staticmethod
    def _engine(cal):
        x =2
        y =4
        resultado = cal.calcular(x,y)
        print(resultado)
