public class principal{
    public static void main(String[] args) {
        persona personas = new persona("Kevin", "celote Segundo", 20,'M');
        personas.mostrarPersona();
        personas.comer();
        personas.caminar();
        personas.hablar();
        personas.dormir();
    }
}
