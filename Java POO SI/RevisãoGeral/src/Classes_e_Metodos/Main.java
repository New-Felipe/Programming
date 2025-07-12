package Classes_e_Metodos;

public class Main {

	public static void main(String[] args) {
		ContaCorrente c1 = new ContaCorrente();
		c1.nome = "Ana";
		c1.numeroConta = 1;
		c1.saldo = 350;
		
		c1.depositar(200);
		c1.sacar(100);
		c1.imprimirInformacoes();
		c1.obterSaldo();
	}
}
