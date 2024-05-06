package test_java_eclipse;

import java.util.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;


public class test {

	public static void main(String[] args) throws Exception {
		String str = "Welcome to Pax.";

        String[] a = str.split(" ");

        int i =0, j = a.length -1;        

        while(i<j){
            String temp = a[i];
            a[i] = a[j];
            a[j] = temp;  
            i++;
            j--;
        }

        String output = "";

        for(i= 0;i<a.length;i++){
            output = output.concat(a[i] + " ");
        }

        System.out.println(output);

	}

}
