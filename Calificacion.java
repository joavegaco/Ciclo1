import java.util.Scanner;

public class Calificacion{

	public static void main(String[] args){
		
		Scanner s = new Scanner(System.in);

		System.out.println("Introduce la nota del primer examen: ");
		double notaPrimer = Double.parseDouble(s.nextLine());

		System.out.println("¿Que nota final quieres tener? ");
		double notaDef = Double.parseDouble(s.nextLine());

		double notaSegundo = (notaDef - 0.4 * notaPrimer)/0.6;
		
		System.out.println("Debes sacar un " + notaSegundo + "para pasar la materia con " + notaDef);


	}
	
}