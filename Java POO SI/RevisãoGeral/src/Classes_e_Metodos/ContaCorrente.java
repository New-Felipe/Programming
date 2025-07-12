package Classes_e_Metodos;

public class ContaCorrente {
	String nome;
	int numeroConta;
	double saldo;
	
	public double depositar(double valor) {
		saldo = saldo + valor;
		return saldo;
	}
	
	public double sacar(double valor) {
		double taxaOperacao = 0.0;
		taxaOperacao = valor*(0.5/100);
		saldo = saldo - (valor+taxaOperacao);
		return saldo;
	}
	
	public void imprimirInformacoes() {
		System.out.println("Nome: "+nome+""
				+ "\nNúmero: " + numeroConta);
	}
	
	public void obterSaldo() {
		System.out.println("\nSaldo atual: "+saldo);
	}
}
