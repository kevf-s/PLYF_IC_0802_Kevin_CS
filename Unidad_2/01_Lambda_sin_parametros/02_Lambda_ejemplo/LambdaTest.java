public class LambdaTest{
    public static void main(String[] args) {
        //Expreción lambda => representa un objeto de una interfaz funcional
        FunctionTest ft = () -> System.out.println("Hola Mundo"); //implementacion del metodo "saludar()"
                                                                // de la Interfaz Funcional<
        //ft.saludar();

        LambdaTest objeto = new LambdaTest();
        objeto.miMetodo(ft);
    }

    public void miMetodo(FunctionTest parametro){
        parametro.saludar();
    }
}