package aula_05_05_25;

public class Pessoa {
	private String nome;
	private int idade;
	private String cpf;
	
	void imprimir_dados() {
		System.out.println("\nNome: "+nome+""
				+ "\nIdade: "+idade+""
				+ "\nCPF: "+cpf);
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

	public String getCpf() {
		return cpf;
	}
}	