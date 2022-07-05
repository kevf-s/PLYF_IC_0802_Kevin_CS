# corecto
class Principal:
    @staticmethod
    def main(args):
        #/Principal.engine((int x, int y)->(long x1,long y2)->x1+y2)
        print("CalcularInt --> resultado = "+ str(Principal._engine1().calculate(5,2)))
        print("CalcularLong --> resultado = "+ str(Principal._engine2().calculate(6,2)))
    @staticmethod
    def _engine1():
        return lambda x, y : x * y
    @staticmethod
    def _engine2():
        return lambda x, y : x - y
