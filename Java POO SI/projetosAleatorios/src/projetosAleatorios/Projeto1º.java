package projetosAleatorios; // login..

import java.util.Scanner;

public class Projeto1º {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String username = "Admin";
		String password = "Password";
		
		System.out.print("Digite o nome de usuário: ");
		String inputUsername = scanner.nextLine();
		
		System.out.print("Digite a senha do usuário: ");
		String inputPassword = scanner.nextLine();
		
		if(inputUsername.equals(username) && inputPassword.equals(password)) {
			System.out.println("Login bem sucedido!");
		}else {
			System.out.println("Nome de usuário ou senha incorretos. =/");
		}
		scanner.close();
	}
}
