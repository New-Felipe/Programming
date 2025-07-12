package aula_19_05_25;

public abstract class Funcionario {
	private String nome;
	private double salarioBase;
	
	public Funcionario(String nome, double salarioBase) {
		this.nome = nome;
		this.salarioBase = salarioBase;
	}
	
	
	public abstract double calcularSalario();

	public String getNome() {
		return nome;
	}


	public void setNome(String nome) {
		this.nome = nome;
	}


	public double getSalarioBase() {
		return salarioBase;
	}


	public void setSalarioBase(double salarioBase) {
		this.salarioBase = salarioBase;
	}	
}
