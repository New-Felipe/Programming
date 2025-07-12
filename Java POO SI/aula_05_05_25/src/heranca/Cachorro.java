package heranca;

public class Cachorro extends Animal{
	private String raca;
	
	Cachorro(String nome, int idade, String raca) {
		super(nome, idade);
		this.raca = raca;
	}
	
	void mostrar_info() {
		super.mostrar_info();
		System.out.println("\nRaça: "+ raca);
	}
	public String getRaca() {
		return raca;
	}

	public void setRaca(String raca) {
		this.raca = raca;
	}
}
