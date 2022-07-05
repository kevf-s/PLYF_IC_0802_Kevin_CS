#/ esta mal
class Principal:
    @staticmethod
    def main(args):
        #/Principal.engine((int x, int y)->(long x1,long y2)->x1+y2)
        print("CalcularInt --> resultado = "+ str(Principal._engine().calculate(5,2)))
        print("CalcularLong --> resultado = "+ str(int(Principal._engine(5).calculate(6,2))))
    @staticmethod
    def _engine():
        return lambda x, y : x * y
    @staticmethod
    def _engine(x1):
        return lambda x, y : x - y
