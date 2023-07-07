package Others;

import java.util.*;

public class algorithms {
   public static void main(String[] args) {
      int[] nums = new int[10];
      Random rand = new Random();
      for (int i = 0; i < nums.length; i++) {
         nums[i] = rand.nextInt(10);
      }

      Arrays.sort(nums);

      printArray(nums);

      int index = binarySearch(nums, 3);

      System.out.println(index);
   }

   //============================================================\\

   public static int binarySearch(int[] arr, int x) {
      int left = 0, right = arr.length - 1;

      while (left <= right) {
         int middle = (left + right) / 2;
         if (arr[middle] == x) {
            return middle;
         } else if (arr[middle] < x) {
            left = middle - 1;
         } else {
            right = middle - 1;
         }
      }
      return -1;
   }

   public static void printArray(int[] arr) {
      for (int i = 0; i < arr.length; i++) {
         System.out.print(arr[i] + " ");
      }
      System.out.println();
   }

   public static void insertionSort(int[] arr) {
      for (int i = 1; i < arr.length; i++) {
         int j = i - 1;
         int curr = arr[i];
         while (j >= 0 && curr < arr[j]) {
            arr[j + 1] = arr[j];
            arr[j] = curr;
            j--;
         }
      }
   }
}
