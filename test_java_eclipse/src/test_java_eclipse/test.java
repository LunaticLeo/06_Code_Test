package test_java_eclipse;

<<<<<<< HEAD
import java.util.*;
=======
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
>>>>>>> 05407c7a90a441f70591a7dbe3df7ea7aff8c307

public class test {

	public static void main(String[] args) throws Exception {
		System.out.println();
		
		
		System.out.println("aaa".compareTo("b"));
		
		int[] arr = new int[10];
		
		
	}

	public static String solution(String s) {
		HashMap<Character, Boolean >hm = new HashMap<Character, Boolean>();
		
		StringBuffer output = new StringBuffer();
		
		for(int i = 0; i<s.length();i++) {
			if(hm.getOrDefault(s.charAt(i), false) == false) {
				hm.put(s.charAt(i),true);
				output.append(s.charAt(i));
			}
		}
		
		return output.toString();
	}
}
