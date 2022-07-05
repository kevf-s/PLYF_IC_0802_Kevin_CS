class LambdaTest:
    @staticmethod
    def main(args):
        op = lambda num1, num2 : print("La suma es: "+(num1+num2))

        op.imprimeSuma(5, 10)

