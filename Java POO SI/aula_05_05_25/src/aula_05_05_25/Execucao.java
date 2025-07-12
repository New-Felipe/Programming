package aula_05_05_25;

import java.util.Scanner;

public class Execucao {

	public static void main(String[] args) {
		Diretor d1 = new Diretor();
		Gerente g1 = new Gerente();
		int opcao = 0;
		Scanner sc = new Scanner(System.in);
		do {
			System.out.println("Digite sua opção: "+""
					+ "\n1 - Diretor"+""
					+ "\n2 - Gerente"+""
					+ "\n3 - Sair");
			opcao = sc.nextInt();
			if(opcao == 1) {
				System.out.println("### DIRETOR ###");
				System.out.println("Nome: ");
				d1.setNome(sc.next());
				System.out.println("Idade: ");
				d1.setIdade(sc.nextInt());
				System.out.println("CPF: ");
				d1.setCpf(sc.next());
				System.out.println("Matrícula: ");
				d1.setMatricula(sc.nextInt());
				System.out.println("Cargo: ");
				d1.setCargo(sc.next());
				System.out.println("Salário: ");
				d1.setSalario(sc.nextDouble());
				d1.imprimir_dados();
				d1.imprimir_salario();
				System.out.println("\n");
			}else if(opcao == 2) {
				System.out.println("### GERENTE ###");
				System.out.println("Nome: ");
				g1.setNome(sc.next());
				System.out.println("Idade: ");
				g1.setIdade(sc.nextInt());
				System.out.println("CPF: ");
				g1.setCpf(sc.next());
				System.out.println("Matrícula: ");
				g1.setMatricula(sc.nextInt());
				System.out.println("Cargo: ");
				g1.setCargo(sc.next());
				System.out.println("Salário: ");
				g1.setSalario(sc.nextDouble());
				g1.imprimir_dados();
				g1.imprimir_salario();
				System.out.println("\n");
			}else {
				System.out.println("Saindo do sistema...");
			}
		}while(opcao < 3);
	}
}
