package Polimorfismo;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Pessoa p1;
		System.out.println("Digite sua opção: "+""
				+ "\n1 - Pessoa"+""
				+ "\n2 - Aluno(a)");
		int opcao = sc.nextInt();
		if(opcao == 1) {
			p1 = new Pessoa("Carlos", 25);
			p1.mostraDados();
		}else if (opcao == 2) {
			p1 = new Aluno("Maria", 22, "Sistemas de Informação");
			p1.mostraDados();
		}else {
			System.out.println("Opção Inválida...");
		}
	}
}
