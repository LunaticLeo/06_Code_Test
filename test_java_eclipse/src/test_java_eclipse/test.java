package test_java_eclipse;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class test {

	public static void main(String[] args) throws Exception {
		double [] arr ={ 1, 2, 3, 5	 };
		
		System.out.println(Arrays.stream(arr).max());
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
