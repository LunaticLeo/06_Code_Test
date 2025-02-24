package test_java_eclipse;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class test {

	public static void main(String[] args) throws InterruptedException {

		int[] arr = { 1, 11, 3, 2 };
		
		Integer[] list = Arrays.stream(new int[]{1,2,3}).boxed().toArray(Integer[]::new);

		Arrays.sort(arr);
		
		System.out.print(arr.clone() == arr);

	}

}
