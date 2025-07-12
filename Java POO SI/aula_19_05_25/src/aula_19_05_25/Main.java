package aula_19_05_25;

public class Main {

	public static void main(String[] args) {
		Funcionario f1 = new Gerente("Maria", 2000, 200);
		Funcionario f2 = new Programador("Carlos", 100, 10);
		double resultado = 0.0;
		System.out.println("Salário Gerente: R$ "+f1.calcularSalario());
		resultado = f2.calcularSalario();
		System.out.println("Salário Programador: R$ "+resultado);
	}
}
