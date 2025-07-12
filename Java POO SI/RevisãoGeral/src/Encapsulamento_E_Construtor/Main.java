package Encapsulamento_E_Construtor;

public class Main {

	public static void main(String[] args) {
		ContaBancaria c1 = new ContaBancaria("Ana", 1, 0, "teste123");
		System.out.println("Titular: "+c1.getTitular()+""
				+ "\nNúmero da conta: "+c1.getNumeroConta()+""
				+ "\nSenha: "+c1.getSenha());
		c1.depositar(400);
		c1.sacar(150, "teste123");
		c1.exibirSaldo("teste123");
		c1.alterarSenha("teste123", "teste");
		
		System.out.println("Titular: "+c1.getTitular()+""
				+ "\nNúmero da conta: "+c1.getNumeroConta()+""
				+ "\nSenha: "+c1.getSenha());
	}
}
