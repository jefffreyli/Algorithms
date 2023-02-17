import java.util.*;
import java.io.*;

public class main {
   public static void main(String[] args) throws IOException {
      //reading in data
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      int x = Integer.parseInt(st.nextToken());

      st = new StringTokenizer(br.readLine());
      int[] arr = new int[n];
      for(int i = 0; i <n; i++){
         arr[i] = Integer.parseInt(st.nextToken());
      }

      //---

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