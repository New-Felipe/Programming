package heranca;

public class Execucao {

	public static void main(String[] args) {
		Cachorro c1 = new Cachorro("Cachorro",10,"Pitbull");
		Gato g1 = new Gato("Gato",2, "Sianês");
		c1.mostrar_info();
		g1.mostrar_info();
	}
}
