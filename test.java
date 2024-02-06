// java test.java

import java.util.*;
import java.util.stream.*;

public class test 
{
    
    public static void main( String[] args )
    {   
    
        int[] arr = new int[7](4,5,62,1,3,56,7);

        sort(arr);

        for(int i : arr){
            System.out.println(i);
        }

    }

    void sort(int[] arr, int a, int b){
        if(a==b){
            return ;
        }

        int point = a+1;
        for(int i=a+1;i<b;i++){
            if(arr[i]<arr[a] && point != i){
                int temp = arr[i];
                arr[i] = arr[point];
                arr[point] = temp;
                point++;
            }   
        }
        if(arr[point] > arr[a]){
            int temp = arr[point-1];
            arr[point-1] = arr[a];
            arr[a] = temp;
            point = point -1;
        }
        if(arr[point] < arr[a]){
            int temp = arr[point];
            arr[point] = arr[a];
            arr[a] = temp;
        }
        sort(arr, a, point);
        sort(arr, point+1, b);
    }


 