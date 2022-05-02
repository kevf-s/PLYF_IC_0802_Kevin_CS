public class Principal{
	public static void main(String[] args){
		System.out.print("==> CalculadoraInt --> resultado " + Principal.engine_1().calculate(5, 5));
		System.out.print("==> CalculadoraLong --> resultado " + Principal.engine_2().calculate(6, 2));
	}

	//retorna un objeto de tipo "CalculadoraInt"
	private static CalculadoraInt engine_1(){
		return (x, y) -> x * y;
	}

	//retorna un objeto de tipo "CalculadoraLong"
	private static CalculadoraLong engine_2(){
		return (x, y) -> x - y;
	}
}