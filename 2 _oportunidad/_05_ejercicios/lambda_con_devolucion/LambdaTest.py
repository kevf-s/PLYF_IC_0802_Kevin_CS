import math

class LambdaTest:
    @staticmethod
    def main(args):
        LambdaTest._engine(lambda x, y : x+y)
        LambdaTest._engine(lambda x, y : x*y)
        LambdaTest._engine(lambda x, y : x/y)
        LambdaTest._engine(lambda x, y : x-y)
        LambdaTest._engine(lambda x, y : math.fmod(x, y))
    @staticmethod
    def _engine(cal):
        x =2
        y = 4
        resultado = cal.calcular(x, y)
        print(resultado)
