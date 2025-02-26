package test_java_eclipse;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class test {

	public static void main(String[] args) throws InterruptedException {

		ArrayList<String> al = new ArrayList<>(); // Raw type, no generics
        
        al.add("1");
        
        System.out.print(al.add("2"));

	}

}
