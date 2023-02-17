package CSES;

import java.util.*;
import java.io.*;

public class sumtwovalues {
   static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
   static int n = 0;
   static int x = 0;
   public static void main(String[] args) throws IOException {
      //reading in data
      StringTokenizer st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      x = Integer.parseInt(st.nextToken());

      st = new StringTokenizer(br.readLine());
      int[] arr = new int[n];
      for(int i = 0; i <n; i++){
         arr[i] = Integer.parseInt(st.nextToken());
      }

      //---

      // mapSolution(arr);
      twoPointersSolve(arr);
   }

   public static void twoPointersSolve(int [] arr){
      Arrays.sort(arr);
      HashMap<Integer, Integer> nums = new HashMap<Integer,Integer>();

      for(int i = 0; i < n; i++){
         nums.put(arr[i], i+1);
      }

      int left = 0;
      int right = arr.length-1;

      while(left < right){
         int currSum = arr[left] + arr[right];
         if(currSum == x){
            System.out.println((nums.get(arr[left])) + " " + (nums.get(arr[right])));
            return;
         }
         else if(currSum < x){
            left++;
         }
         else if(currSum > x){
            right--;
         }
      }
      System.out.println("IMPOSSIBLE");
   }

   public static void mapSolution(int [] arr){
      boolean found = false;
      HashMap<Integer, Integer> nums = new HashMap<Integer,Integer>();

      for(int i = 0; i < n; i++){
         nums.put(arr[i], i+1);
      }

      for(int i = 0; i < n; i++){
         if(nums.containsKey(x-arr[i]) && !(i+1==nums.get(x-arr[i])) ){
            System.out.print((i+1) + " " + (nums.get(x-arr[i])));
            found=true;
            break;
         }
      }

      if(!found) System.out.println("IMPOSSIBLE");
   }

}