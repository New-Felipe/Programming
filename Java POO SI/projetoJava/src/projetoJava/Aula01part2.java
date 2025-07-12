package projetoJava;

public class Aula01part2 {

	public static void main(String[] args) {
		double v1 = 0.0, v2 = 0.0, resultado = 0.0;
		v1 = 100;
		v2 = 20;
		resultado = v1 - v2;
		System.out.println("Soma: "+resultado);
		resultado = v1 - v2;
		System.out.println("Subtração: "+resultado);
		resultado = v1 * v2;
		System.out.println("Multiplicação: "+resultado);
		resultado = v1/v2;
		System.out.println("Divisão: "+resultado);
		
		if(v1 >= v2) {
			System.out.println("V1 Maior ou igual a V2");
		} else {
			System.out.println("V2 Maior que V1");
		}
	}

}
