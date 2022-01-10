package convert_words;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Sort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try { 

			String pathname = "C:\\Users\\liaoy\\OneDrive\\Desktop\\Master\\leactures\\note words.txt"; 
			File filename = new File(pathname); 
			InputStreamReader reader = new InputStreamReader(new FileInputStream(filename));
			BufferedReader br = new BufferedReader(reader); 
			String line = "";
			ArrayList<String> strlist =new ArrayList<String>();
			line = br.readLine();
			strlist.add(line);
			while (line != null) {
				line = br.readLine();
				if(line !=null) {
					line.toLowerCase();
					strlist.add(line);
				}
			}
			
			
			Collections.sort(strlist);
			
			for(int i=0;i<strlist.size();i++) {
				System.out.println(strlist.get(i));
			}
			
			
			File writename = new File("C:\\Users\\liaoy\\OneDrive\\Desktop\\output.txt"); 
			writename.createNewFile(); 
			BufferedWriter out = new BufferedWriter(new FileWriter(writename));
			out.write("我会写入文件啦\r\n"); 
			out.flush(); 
			out.close(); 

		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
