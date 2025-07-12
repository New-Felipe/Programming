package heranca;

public class Animal {
	private String nome;
	private int idade;
	
	Animal(String nome, int idade) {
		this.nome = nome;
		this.idade = idade;
	}
	void mostrar_info() {
		System.out.println("\nNome: "+nome+""
				+ "\nIdade: "+idade);
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public int getIdade() {
		return idade;
	}
	public void setIdade(int idade) {
		this.idade = idade;
	}
}
