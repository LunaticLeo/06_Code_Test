package test_java_eclipse;

import java.lang.Boolean;
import java.util.*;

public class test {

	public static void main(String[] args) throws Exception {
		byte a = 90;  
		a = (byte)(a*2); //所以这一行会报错，提示 Type mismatch: cannot convert from int to byte
		System.out.print(a);
	}

}
