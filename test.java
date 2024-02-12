// java test.java

import java.util.*;
import java.util.stream.*;

public class test 
{
    
    public static void main( String[] args )
    {   
    
        int[] arr = new int[]{4,5,62,1,3,56,7};

        sort(arr, 0, 7);

        for(int i : arr){
            System.out.println(i);
        }

    }

    static void sort(int[] arr, int a, int b){
        if(a==b){
            return ;
        }

        int point = a+1;
        for(int i=a+1;i<b;i++){
            if(arr[i]<arr[a]){
                int temp = arr[i];
                arr[i] = arr[point];
                arr[point] = temp;
                point++;
            }   
        }
        if(arr[point] > arr[a]){
            point = point - 1;
        }else{
            int temp = arr[point];
            arr[point] = arr[a];
            arr[a] = temp;
        }
        sort(arr, a, point);
        sort(arr, point+1, b);
    }
}

 