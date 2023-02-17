import java.util.*;
import java.io.*;

public class p3 {
   static int[] cows;
   static int n = 0;
   static int q = 0;

   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new FileReader("bcount.in"));
      PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("bcount.out")));
      StringTokenizer st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      q = Integer.parseInt(st.nextToken());
      cows = new int[n];
      int[] start = new int[q];
      int[] end = new int[q];

      for (int i = 0; i < n; i++) {
         st = new StringTokenizer(br.readLine());
         cows[i] = Integer.parseInt(st.nextToken());
      }

      for (int i = 0; i < q; i++) {
         st = new StringTokenizer(br.readLine());
         start[i] = Integer.parseInt(st.nextToken())-1;
         end[i] = Integer.parseInt(st.nextToken())-1;
      }

      // ---

      int[] pSumHolstein = pSum(1);
      int[] pSumGuernseys = pSum(2);
      int[] pSumJerseys = pSum(3);
      System.out.println(Arrays.toString(pSumHolstein));
      System.out.println(Arrays.toString(pSumGuernseys));
      System.out.println(Arrays.toString(pSumJerseys));

      // int h,g,j = 0;
      for(int i = 0; i < q; i++){
         int h = pSumHolstein[end[i]] - pSumHolstein[start[i]];
         if(pSumHolstein[start[i]] !=0) h++;

         int g = pSumGuernseys[end[i]] - pSumGuernseys[start[i]];
         if(pSumGuernseys[start[i]] !=0) g++;

         int j = pSumJerseys[end[i]] - pSumJerseys[start[i]];
         if(pSumJerseys[start[i]] !=0) j++;

         pw.println(h + " " + g + " " + j);
      }
      pw.close();

   }

   public static int[] pSum(int type) {
      int[] cow = new int[n];
      cow[0] = cows[0] == type ? 1 : 0;

      for (int i = 1; i < n; i++) {
         if (cows[i] == type) {
            cow[i] = cow[i - 1] + 1;
         } else {
            cow[i] = cow[i - 1];
         }
      }
      return cow;
   }

}
