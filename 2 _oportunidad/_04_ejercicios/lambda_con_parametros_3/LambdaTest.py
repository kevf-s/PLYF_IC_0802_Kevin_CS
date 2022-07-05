class LambdaTest:
    @staticmethod
    def main(args):
        op = lambda num1, num2 : print("El resultado es: "+(num1+num2))
        op.imprimeOperacion(5, 10)

        objeto = LambdaTest()
        objeto.miMetodo(lambda num1, num2 : print("La resta es: "+(num1-num2)),20,10)
        objeto.miMetodo(lambda num1, num2 : print("La multiplicacion es : "+(num1*num2)),20,10)
    def miMetodo(self, op, num1, num2):
        op.imprimeOperacion(num1, num2)
