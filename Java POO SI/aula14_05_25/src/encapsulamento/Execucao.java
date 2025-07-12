package encapsulamento;

public class Execucao {

	public static void main(String[] args) {
		Encapsulamento e = new Encapsulamento();
		e.setNome("Teste");
		e.setAno(2025);
		e.setModelo("A");
		
		System.out.println("Nome: "+e.getNome()+""
				+ "\nAno: "+e.getAno()+""
						+ "\nModelo: "+e.getModelo());
	}
}
