package construtor;

import java.util.Scanner;

public class Execucao {

	public static void main(String[] args) {
		Pessoa p = new Pessoa("Ana", 20, "5000-05");
		Scanner sc = new Scanner(System.in);
		System.out.println("Nome: ");
		p.setNome(sc.nextLine());
		System.out.println("Idade: ");
		p.setIdade(sc.nextInt());
		System.out.println("CPF: ");
		p.setCpf(sc.next());
		
		System.out.println("\nNome: "+p.getNome()+""
				+ "\nIdade: "+p.getIdade()
				+ "\nCPF: "+p.getCpf());
	}
}
