package Polimorfismo;

public class Aluno extends Pessoa{
	private String nomeCurso;
	
	public Aluno(String nome, int idade, String nomeCurso) {
		super(nome, idade);
		this.nomeCurso = nomeCurso;
	}
	
	public void mostraDados() {
		System.out.println("\nNome do Aluno(a): "+getNome()+""
				+ "\nIdade do Aluno(a): "+getIdade()+""
				+ "\nCurso do Aluno(a)"+getNomeCurso());
	}

	public String getNomeCurso() {
		return nomeCurso;
	}

	public void setNomeCurso(String nomeCurso) {
		this.nomeCurso = nomeCurso;
	}
}
