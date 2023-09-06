package USACO;
import java.util.*;
import java.io.*;

public class template {
   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());

   }

   public static void printArray(String[][] arr) {
      for (int i = 0; i < arr.length; i++) {
         System.out.println(Arrays.toString(arr[i]));
      }
   }
}