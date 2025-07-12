package Classes_e_MétodosAbstratos;

public class Programador extends Funcionario{
	private int horasTrabalhadas;
	
	public Programador(String nome, double salarioBase, int horasTrabalhadas) {
		super(nome, salarioBase);
		this.horasTrabalhadas = horasTrabalhadas;
	}
	
	@Override
	public double calcularSalario() {
		setSalarioBase(getSalarioBase() * horasTrabalhadas);
		return getSalarioBase();
	}

	public int getHorasTrabalhadas() {
		return horasTrabalhadas;
	}

	public void setHorasTrabalhadas(int horasTrabalhadas) {
		this.horasTrabalhadas = horasTrabalhadas;
	}
}
