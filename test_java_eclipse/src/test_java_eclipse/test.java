package test_java_eclipse;

import java.util.HashSet;
import java.util.Scanner;

public class test {

	public static void main(String[] args) throws Exception {
		Solution.main(null);
	}

	public class Solution {

		public static int validQuadruples(int N, int A[]) {
	        
	        //this is default OUTPUT. You can change it.
	        int result= 0;
	        
	        //write your Logic here:
	        int[] nums = new int[4];
	        
	        for(int i=0;i<N;i++) {
	        	nums[i%4] = A[i];
	        	
	        	if( i>=4 && (nums[i%4]+nums[(i+1)%4]) ==  (nums[(i+2)%4]+nums[(i+3)%4]) ) {
	        		result ++;
	        	}
	        }
	        
	        return result ==0 ? -404 : result;
	    }
		
		public static void main(String[] args) throws Exception {
			Scanner sc = new Scanner(System.in);
	        int N = sc.nextInt();
	        
	        int A [] = new int[N];
	        for(int i=0; i<N; i++) {
	            A[i] = sc.nextInt();
	        }
	        
	        // OUTPUT [uncomment & modify if required]
	        System.out.print(validQuadruples(N,A));
	        sc.close();
		}
	}
}
