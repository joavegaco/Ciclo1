import java.util.Scanner;

public class Pregunta {
	public static void main(String[] args){

		Scanner s = new Scanner(System.in);

		System.out.println("Cual es la capital de Colombia?");
		String respuesta = s.nextLine();
	
		if (respuesta.equals("Bogota")){
			System.out.println("La respuesta es correcta");
	
	
		} else {
		System.out.println("Error. La respuesta es incorrecta");
		}

	}
}