package aula_19_05_25;

public class Gerente extends Funcionario{
	private double bonus;
	
	public Gerente(String nome, double salarioBase, double bonus) {
		super(nome, salarioBase);
		this.bonus = bonus;
	}

	@Override
	public double calcularSalario() {
		// TODO Auto-generated method stub
		return 0;
	}

	public double getBonus() {
		return bonus;
	}

	public void setBonus(double bonus) {
		this.bonus = bonus;
	}
}
