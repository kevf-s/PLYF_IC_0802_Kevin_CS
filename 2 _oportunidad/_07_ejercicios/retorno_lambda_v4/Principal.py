#correcto
class Principal:
    @staticmethod
    def main(args):
        #/Principal.engine((int x, int y)->(long x1,long y2)->x1+y2)
        print("CalcularInt --> resultado = "+ str(Principal._engine(3,7).calculate(5,2)))
        print("CalcularLong --> resultado = "+ str(Principal._engine(int(5),int(5)).calculate(6,2)))
    @staticmethod
    def _engine(a, b):
        return lambda x, y : a * b
    @staticmethod
    def _engine(a, b):
        return lambda x, y : a + b