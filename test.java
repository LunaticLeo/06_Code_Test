// java test.java

import java.util.*;
import java.util.stream.*;

public class test 
{
    
    public static void main( String[] args )
    {   
        // System.out.println("01" < "02");

        // try stream, collect
        // import java.util.*;
        // import java.util.stream.*;
        // List<String> list = List.of("Apple", "Banana", "Blackberry", "Coconut", "Avocado", "Cherry", "Apricots");
        // Map<String, List<String>> groups = list.stream()
        //         .collect(Collectors.groupingBy(s -> s.substring(0, 1), Collectors.toList()));
        // System.out.println(groups);

        // enum TreatmentType {
		//     SURGERY,DRUGTREATMENT,RADIOLOGY,PHYSIOTHERAPY;		
	    // }
        // TreatmentType tt = TreatmentType.SURGERY;
        // System.out.println(TreatmentType.SURGERY.equals(tt));



        // try streamReader
        // import java.io.BufferedReader;
        // import java.io.InputStreamReader;
        // BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        // try{
        //     String line = in.readLine();
        //     String[] inputs = line.split(" +");
        //     System.out.println(inputs.length);
        // }catch(Exception e){
        //     System.out.println(e);
        // }



        // try UUID
        // import java.util.UUID;
        // UUID uuid = UUID.randomUUID();
        // System.out.println(uuid.toString());

        // UUID uuid2 = UUID.fromString("10000000-0000-0000-0000-000000000000"); // invaid
        // System.out.println(uuid2.toString());
        
    }


    
class GFG {
    public static int ans = 10000000;
    public static void solve(int a[], int n, int k,
                             int index, int sum, int maxsum)
    {
        // K=1 is the base Case
        if (k == 1) {
            maxsum = Math.max(maxsum, sum);
            sum = 0;
            for (int i = index; i < n; i++) {
                sum += a[i];
            }
            // we update maxsum
            maxsum = Math.max(maxsum, sum);
            // the answer is stored in ans
            ans = Math.min(ans, maxsum);
            return;
        }
        sum = 0;
        // using for loop to divide the array into
        // K-subarray
        for (int i = index; i < n; i++) {
            sum += a[i];
            // for each subarray we calculate sum ans update
            // maxsum
            maxsum = Math.max(maxsum, sum);
            // calling function again
            solve(a, n, k - 1, i + 1, sum, maxsum);
        }
    }
    public static void main(String[] args)
    {
        int arr[] = { 1, 2, 3, 4 };
        int k = 3; // K divisions
        int n = 4; // Size of Array
        solve(arr, n, k, 0, 0, 0);
        System.out.println(ans + "\n");
    }
}
}
