package try_java;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;

public class try_java {

	public static void main(String[] args) {
		
		HashMap<String, Integer> hmap = new HashMap<>();
        for(String word: words){
            hmap.put(word, hmap.getOrDefault(word,0)+1);
        }
        
        HashMap<Integer, ArrayList> hmap2 = new HashMap<>();
        for (String key : hmap.keySet()) {
            int value = hmap.get(key);            
            if(!hmap2.containsKey(value)) {
            	hmap2.put(value, new ArrayList());
            }
            hmap2.get(value).add(key);
        }
        
        Object[] sortedArr; 
        
        hmap2.keySet().toArray(sortedArr);
        
        ArrayList output = new ArrayList();
        for(Object i: sortedArr) {
        	Collections.sort(hmap2.get(i));
        	output.addAll(hmap2.get(i));
        }
		
		return output;
	}

}
