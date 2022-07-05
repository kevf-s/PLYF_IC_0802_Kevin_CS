import math

class LambdaTest:
    @staticmethod
    def main(args):
        LambdaTest._engine(lambda x, y : x+y)
        LambdaTest._engine(lambda x, y : x*y)
#JAVA TO PYTHON CONVERTER TODO TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        LambdaTest._engine(lambda x, y : x/y)
        LambdaTest._engine(lambda x, y : x-y)
        LambdaTest._engine(lambda x, y : math.fmod(x, y))
    @staticmethod
    def _engine(cal):
        x =2
        y = 4
        resultado = cal.calcular(x, y)
        print(resultado)
