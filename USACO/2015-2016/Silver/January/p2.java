
// package Old.USACO: 2015-2016.Silver.January;
import java.util.*;
import java.io.*;

public class p2 {
   public static void main(String[] args) throws IOException {
      // Scanner sc = new Scanner(new File("div7.in"));
      // PrintWriter pw = new PrintWriter(new File("div7.out"));
      // int n = sc.nextInt();
      // int [] cows = new int[n];
      // for(int i = 0; i < n; i++){
      // cows[i] = sc.nextInt();
      // // System.out.print(cows[i] + " ");
      // }

      BufferedReader br = new BufferedReader(new FileReader("div7.in"));
      PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("div7.out")));

      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());

      int[] cows = new int[n];
      for (int i = 0; i < n; i++) {
         st = new StringTokenizer(br.readLine());
         cows[i] = Integer.parseInt(st.nextToken());
      }

      int[] prefixSumArr = new int[n];
      prefixSumArr[0] = cows[0];
      for (int i = 1; i < n; i++) {
         prefixSumArr[i] = prefixSumArr[i - 1] + cows[i];
      }

      long maxLen = 0;
      for (int i = 0; i < n; i++) {
         for (int j = 0; j < n; j++) {
            long subSum = prefixSumArr[j] - prefixSumArr[i];
            int len = j - i;
            if ((subSum % 7 == 0) && len > maxLen) {
               maxLen = len;
            }
         }
      }
      System.out.println(maxLen);
      pw.println(maxLen);
      pw.close();

   }

   public static void printArray(int[] arr) {
      for (int i = 0; i < arr.length; i++) {
         System.out.print(arr[i] + " ");
      }
   }

}
