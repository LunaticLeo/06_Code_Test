package convert_words;

public class EngCNConnect {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "";

		String str2 = "";

		String[] eng = str.split("\r\n");
		String[] cn = str2.split("\r\n");
		for (int i = 0; i < eng.length; i++) {
			System.out.println(eng[i] + " " + cn[i]);
		}

	}

}
