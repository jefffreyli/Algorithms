package Others;
import java.util.*;

public class sorting {
   public static void main(String[] args){
      int [] bobbyArr = new int[10];
      Random rand = new Random();
      for(int i = 0; i < bobbyArr.length; i++){
         bobbyArr[i] = rand.nextInt(100);
      }

      System.out.println("Before: ");
      printArray(bobbyArr);

      insertionSort(bobbyArr);

      System.out.println("After: ");
      printArray(bobbyArr);
   }

   public static void printArray(int[] arr){
      for(int i = 0; i < arr.length; i++){
         System.out.print(arr[i] + " ");
      }
   }

   public static void insertionSort(int [] arr){
      for(int i = 1; i < arr.length; i++){
         int j = i-1;
         int curr = arr[i];
         while(j >=0 && curr < arr[j]){
            arr[j+1] = arr[j];
            arr[j] = curr;
            j--;
         }
      }
   }
}
