class LambdaTest:
    @staticmethod
    def main(args):
        op = lambda num1, num2 : print("El resultado es: "+(num1+num2))

        objeto = LambdaTest()
        objeto.miMetodo(op, 10, 10)

    def miMetodo(self, op, num1, num2):
        op.imprimeSuma(num1, num2)

