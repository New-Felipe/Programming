package Classes_e_MétodosAbstratos;

public class Main {

	public static void main(String[] args) {
		Gerente g1 = new Gerente("Carlos", 3500, 400);
		Programador p1 = new Programador("Maria", 400, 200);
		
		System.out.println("---GERENTE---");
		System.out.println("Nome: "+g1.getNome()+""
				+ "\nSalário Base: "+g1.getSalarioBase()+""
				+ "\nBônus: "+g1.getBonus());
		System.out.println("\nSalário atual: "+g1.calcularSalario());
		System.out.println("\n---PROGRAMADOR---");
		System.out.println("\nNome: "+p1.getNome()+""
				+ "\nSalário Base: "+p1.getSalarioBase()+""
				+ "\nHoras trabalhadas: "+p1.getHorasTrabalhadas());
		System.out.println("\nSalário atual: "+p1.calcularSalario());
	}
}
