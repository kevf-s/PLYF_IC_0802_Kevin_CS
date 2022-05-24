public interface Prueba_Examen{  /*Paso 1*/

    public default void MensajeHola(){ /*Paso 2*/
    System.out.println("Hola mi nombre es: Kevin Celote Segundo"); /*Paso3*/
    }
    public default void MensajeHola(String cadena){  /*Paso 4*/
    System.out.println("La cadena es: " + cadena);
    }

    public static int OperacionPrueba(int a, int b){ /*Paso 5*/
        return a + b; /*Paso 6*/
    }
    public void OperacionPrueba(int a, int b, int c); /*Paso 7*/
}