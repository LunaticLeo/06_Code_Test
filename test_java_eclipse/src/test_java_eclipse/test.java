package test_java_eclipse;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;

public class test {
	public static void main(String[] args) {
		return;
	}

	public class BookSale {
		public static int nthLowestSelling(int[] sales, int n) {

			HashMap<Integer, Integer> hmap = new HashMap<>();

			for (int id : sales) {
				hmap.put(id, hmap.getOrDefault(id, 0));
			}
			
			HashMap<Integer, Integer> swap = new HashMap<>();
			for(int id : hmap.keySet()) {
				swap.put(hmap.get(id), id);
			}
			
			
			int[] nums = Arrays.toArray(swap.keySet());
			
//			int ans = findKthSmallest( , n, 0)
			
			return 0;
		}

		
		public static int findKthSmallest(int[] nums, int k,int start, int end){
	        
	        
	        
	        if(start==end) return nums[start];
	        
	        int i=start, point=end-1, temp;
	        
	        // random => half
	        temp= nums[end];
	        nums[end]=nums[end/2+start/2];
	        nums[end/2+start/2]=temp;
	        
	        while(i<=point){
	            if(nums[i]<=nums[end]){ //<= or < doesn't matter, the key is i<=point
	                i++;
	            }else{
	                temp = nums[point];
	                nums[point]=nums[i];
	                nums[i]=temp;
	                point--;
	            }
	        }

	        temp=nums[end];
	        nums[end]=nums[i];
	        nums[i]=temp; 
	        
	        // System.out.println(Arrays.toString(nums)+i);
	        
	        if(i==k) return nums[i];
	        if(i<k){
	            return findKthSmallest(nums, k, i+1, end);
	        } 
	        else return findKthSmallest(nums, k, start, i-1);
	        
	    }
		
		public static void main(String[] args) {
			int x = nthLowestSelling(new int[] { 5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5 }, 2);
			System.out.println(x);
		}
	}

}
