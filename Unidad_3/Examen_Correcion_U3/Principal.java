public class Principal{     /*Paso 1 */

 public static void main(String[] args) {  /*Paso 2 */

    Prueba_Examen pe; /*Paso 3*/
    
    pe = (a,b,c) -> System.out.println((a+b+c)); /*Paso 4 */
    System.out.println(Prueba_Examen.OperacionPrueba(3,5)); /*Paso 5*/

    pe.MensajeHola(); /*Paso 6*/
    pe.MensajeHola("Hola Mundo"); /*Paso 7*/

    pe = (a,b,c) -> System.out.println((a+(b*c))); /*Paso 8*/
    pe.OperacionPrueba(5,Prueba_Examen.OperacionPrueba(2,7), Prueba_Examen.OperacionPrueba(10,12)); /*Paso 9*/

    miMetodo(pe); /*Paso 12*/
    miMetodo((a,b,c) -> System.out.println((a+(b/c)))); /*Paso 13*/

    pe = (a,b,c)->System.out.println(((float)a+((float)b/(float)c))); /*Paso 16*/
    miMetodo(pe,4,6,7); /*Paso 17*/
    }

    private static void miMetodo(Prueba_Examen pe) { /*Paso 10*/
        pe.OperacionPrueba(6,Prueba_Examen.OperacionPrueba(4,4),Prueba_Examen.OperacionPrueba(2,2)); /*Paso 11*/
    }
    private static void miMetodo(Prueba_Examen pe, int a,int b,int c) { /*Paso 14*/
        pe.OperacionPrueba(a,Prueba_Examen.OperacionPrueba(b,b),Prueba_Examen.OperacionPrueba(c,c)); /*Paso 15*/
    }
}