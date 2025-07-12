package Classes_e_MétodosAbstratos;

public class Gerente extends Funcionario{
	private double bonus;
	
	public Gerente(String nome, double salarioBase, double bonus) {
		super(nome, salarioBase);
		this.bonus = bonus;
	}


	//serve para chamar um método sendo abstrato:
	@Override
	public double calcularSalario() {
		setSalarioBase(getSalarioBase() + bonus);
		return getSalarioBase();
	}
	
	public double getBonus() {
		return bonus;
	}


	public void setBonus(double bonus) {
		this.bonus = bonus;
	}
}
