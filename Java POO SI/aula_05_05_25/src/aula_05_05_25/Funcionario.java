package aula_05_05_25;

public class Funcionario {
	private int matricula;
	private String cargo;
	private double salario;
	
	void imprimir_dados() {
		System.out.println("\nNome: "+getNome()+""
				+ "\nIdade: "+getIdade()+""
				+ "\nCPF: "+getCpf()+""
				+ "\nMatricula: "+matricula+""
				+ "\nCargo: "+cargo+""
				+ "\nSalário: "+salario);
	}
	
	private String getCpf() {
		// TODO Auto-generated method stub
		return null;
	}

	private String getIdade() {
		// TODO Auto-generated method stub
		return null;
	}

	private String getNome() {
		// TODO Auto-generated method stub
		return null;
	}

	void imprimir_salario() {
		System.out.println("Salário: "+salario);
	}

	public int getMatricula() {
		return matricula;
	}

	public void setMatricula(int matricula) {
		this.matricula = matricula;
	}

	public String getCargo() {
		return cargo;
	}

	public void setCargo(String cargo) {
		this.cargo = cargo;
	}

	public double getSalario() {
		return salario;
	}

	public void setSalario(double salario) {
		this.salario = salario;
	}
}
