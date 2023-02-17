import java.util.*;
import java.io.*;

public class p1 {
   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());

      int n = Integer.parseInt(st.nextToken());

      String[] breeds = new String[n];
      st = new StringTokenizer(br.readLine());
      String b = st.nextToken();
      for (int i = 0; i < n; i++) {
         breeds[i] = b.substring(i, i + 1);
      }

      st = new StringTokenizer(br.readLine());
      int[] eList = new int[n];
      for (int i = 0; i < n; i++) {
         eList[i] = Integer.parseInt(st.nextToken());
      }

      int numG = 0;
      int numH = 0;
      for (int i = 0; i < n; i++) {
         if (breeds[i].equals("G")) {
            numG++;
         } else {
            numH++;
         }
      }

      int[] cows = new int[n];
      int countG = 0;
      int countH = 0;
      for (int i = 0; i < n; i++) {
         String breedType = breeds[i];
         for (int j = i; j < eList[i]; j++) {
            if (breedType.equals("G")) {
               if (breeds[j].equals(breedType)) {
                  countG++;
               } else {
                  countH++;
               }
            }

            else {
               if (breedType.equals("H")) {
                  if (breeds[j].equals(breedType)) {
                     countH++;
                  } else {
                     countG++;
                  }
               }
            }
         }

         if (breedType.equals("G") && countG == numG) {
            cows[i] = 1;
         }
         if (breedType.equals("H") && countH == numH) {
            cows[i] = 1;
         }
         countH = 0;
         countG=0;
      }


      for (int i = 0; i < n; i++) {
         for(int j = i; j < eList[i]; j++){
               if(!breeds[i].equals(breeds[j]) && cows[i] == 1 && i>=j && i <=eList[i]){
                  cows[j] = 1;
               }
            }
            
         }
      

      int leaders = 0;
      for (int i = 0; i < n; i++) {
         if (cows[i] == 1) {
            leaders++;
         }
      }

      System.out.println(leaders);

   }

   public static void printArray(int[] arr){
      for(int i = 0; i < arr.length; i++){
         System.out.print(arr[i] + " ");
      }
      System.out.println();
   }

}
