package aula_05_05_25;

public class Diretor extends Funcionario{
	
	public void imprimir_salario() {
		double bonificacao = getSalario() * 0.15;
		setSalario(getSalario()+bonificacao);
		System.out.println("\nSalário: "+getSalario());
	}

	public void setNome(String next) {
		// TODO Auto-generated method stub
		
	}

	public void setIdade(int nextInt) {
		// TODO Auto-generated method stub
		
	}

	public void setCpf(String next) {
		// TODO Auto-generated method stub
		
	}
	
}
