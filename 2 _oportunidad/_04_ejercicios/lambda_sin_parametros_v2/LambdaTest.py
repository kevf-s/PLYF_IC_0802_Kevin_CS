class LambdaTest:
    @staticmethod
    def main(args):
        # Esprexion Lambda => represnetando un objeto de una Interfaz funcional (FunctionTest)
        ft = lambda : print("Hola Mundo")
        objeto = LambdaTest()
        objeto.miMetodo(ft)

    def miMetodo(self, parametro):
        parametro.saludar()
