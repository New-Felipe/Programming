package aula_19_05_25;

public class Programador extends Funcionario{
	private int horasTrabalhadas;
	
	public Programador(String nome, double salarioBase, int horasTrabalhadas) {
		super(nome, salarioBase);
		this.horasTrabalhadas = horasTrabalhadas;
	}

	@Override
	public double calcularSalario() {
		// TODO Auto-generated method stub
		return 0;
	}

	public int getHorasTrabalhadas() {
		return horasTrabalhadas;
	}

	public void setHorasTrabalhadas(int horasTrabalhadas) {
		this.horasTrabalhadas = horasTrabalhadas;
	}
}
