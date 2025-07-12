package Herança;

public class Carro extends Veiculo{
	private int numeroPortas;
	
	public Carro(String modelo, int ano, int numeroPortas) {
		super(modelo, ano);
		this.numeroPortas = numeroPortas;
	}
	public void exibirDetalhes() {
		System.out.println("Modelo: "+getModelo()+""
				+ "\nAno: "+getAno()+""
				+ "\nNúmero de portas: "+numeroPortas);
	}
	public int getNumeroPortas() {
		return numeroPortas;
	}
	public void setNumeroPortas(int numeroPortas) {
		this.numeroPortas = numeroPortas;
	}
}
