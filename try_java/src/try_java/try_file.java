package try_java;

import java.io.*;
import java.util.ArrayList;


public class try_file {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {

			String pathname = "C:\\Users\\liaoy\\OneDrive\\Desktop\\Master\\leactures\\note words.txt"; 
			File filename = new File(pathname); 
			
			InputStreamReader reader = new InputStreamReader(new FileInputStream(filename)); 
			BufferedReader br = new BufferedReader(reader); 
			
			ArrayList<String> str =new ArrayList<String>();
			
			do {
				str.add(br.readLine());
			}while(str.get(str.size()-1)!=null);
			str.remove(str.size()-1);
			
			for(int i=0;i<str.size();i++) {
				System.out.println(str.get(i));
			}
			
			File writename = new File("C:\\Users\\liaoy\\OneDrive\\Desktop\\output.txt"); 
			writename.createNewFile(); 
			BufferedWriter out = new BufferedWriter(new FileWriter(writename));
			out.write("hello"); 
			out.flush(); 
			out.close(); 

		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
