package aula14_05_25;

import java.util.Scanner;

public class Execucao {

	public static void main(String[] args) {
		Data d1 = new Data();
		Scanner sc = new Scanner(System.in);
		do {
			System.out.println("Digite o dia: ");
			d1.setDia(sc.nextInt());
			System.out.println("Digite o mês: ");
			d1.setMes(sc.nextInt());
			System.out.println("Digite o ano: ");
			d1.setAno(sc.nextInt());
		}while(d1.getDia() < 1 || d1.getDia() > 31 || d1.getMes() < 1 || d1.getMes() > 12 || d1.getAno() < 1);
		
		System.out.println("Data "+d1.getDia()+"/"
				+d1.getMes()
				+ "/"+d1.getAno());
		
				d1.dia_seguinte();
				
				System.out.println("\nData: "+d1.getDia()+"/"
						+d1.getMes()
						+ "/"+ d1.getAno());
	}
}
