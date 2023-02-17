import java.util.*;

public class sudoku {
   public static void main(String[] args) {
      int counter = 1;
      int[][][] solution = new int[9][3][3];
      int[][][] player = new int[9][3][3];
      boolean playagain = true;

      for (int i = 0; i < solution.length; i++) {
         for (int j = 0; j < solution[i].length; j++) {
            for (int k = 0; k < solution[i][j].length; k++) {
               solution[i][j][k] = counter;
               counter += 1;
            }
         }
         counter = 1;
      }

      int rand = (int) (Math.random()*9+1);
      for (int i = 0; i < 9; i++) {
         for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 1; k++) {
               while(hasRepeats(solution, rand)){
                  rand = (int) (Math.random()*9+1);
               }
               solution[i][j][k] = rand;
            }
         }
      }

      // to check if the player correctly put it in the right position, match the
      // position from the solution board to the player's board
      int strike = 0;
      int whitespaces = 0; // obviously arbitrary until i figure it out I think we can just parse through
                           // the 3D array and if a number is 0 its whitespaces or whatever value we assign
                           // to it.
      for (int i = 0; i < solution.length; i++) {
         for (int j = 0; j < solution[i].length; j++) {
            for (int k = 0; k < solution[i][j].length; k++) {
               if (solution[i][j][k] == 0)
                  whitespaces++;
               // all just calculates number of whitespaces
            }
         }
      }
      Scanner sc = new Scanner(System.in);
      while (whitespaces >= 0) {
         System.out.println("Please enter the number of the cube you are guessing");
         int numcube = sc.nextInt();
         // all of this input code is meant to detect where on the board the player is
         // guessing
         System.out.println("Please enter row that you are guessing in the cube");
         int rowguess = sc.nextInt();
         System.out.println("Please enter row that you are guessing in the cube");
         int colguess = sc.nextInt();
         System.out.println("Please enter you guess for the number");
         int numguess = sc.nextInt();
         if (numguess != solution[numcube - 1][rowguess - 1][colguess - 1]) {
            strike++;

            // sees if the input from the user is the same as the solution array’s element
            // in the same place
            whitespaces++; // i do this in order to give the player the white spot back bc he isnt revealed
                          // yet
            System.out.println("Incorrect!");
         } else
            System.out.println("Correct!");
         if (strike == 3) {
            System.out.println("You lose!"); // just to check if the user maxed out his lives yet
            break; // bc the user lost we go out of the whole while loop
         }
         whitespaces -= 1; // to make the while loop work yk this you gave me the idea
      }

      // to check if the player won, count the number of whitespaces at the beginning
      // and decrement it for each correct answer. when it reaches 0, the player has
      // won.
      displayBoard(solution);

      strike = 0;
   whitespaces = 9;
   while(whitespaces>=0)
   {
      System.out.println("Please enter the number of the cube you are guessing");
      int numcube = sc.nextInt();
      System.out.println("Please enter row that you are guessing in the cube");
      int rowguess = sc.nextInt();
      System.out.println("Please enter row that you are guessing in the cube");
      int colguess = sc.nextInt();
      System.out.println("Please enter you guess for the number");
      int numguess = sc.nextInt();
      if (numguess != solution[numcube - 1][rowguess - 1][colguess - 1]) {
         strike++;
         System.out.println("Incorrect!");
      } else
         System.out.println("Correct!");
      if (strike == 3) {
         System.out.println("You lose!");
         break;
      }
      whitespaces -= 1;
   }if(whitespaces==0)System.out.println("You win!!");

   // System.out.println(“
   // Any character-
   // Play Again or 1-Exit”);
   // int againornot = sc.nextInt();if(againornot==1)playagain=false;
   // // i will place the while loop at the end to avoid confusion
   // while(playagain==true)
   // {
   //    // all code here
   // }

   }

   //Helper functions Helper functions Helper functions

   public static boolean hasRepeats(int[][][] arr, int n) {
      for (int i = 0; i < arr.length; i++) {
         for (int j = 0; j < arr[i].length; j++) {
            for (int k = 0; k < arr[i][j].length; k++) {
               if (n == k) {
                  return true;
               }
            }

            if (n == j) {
               return true;
            }
         }
      }
      // loop through each row in the 3D array
      // if (n is in the row){
      // return true;
      // }
      // loop through each column in the 3D array
      // if (n is in the column){
      // return true;
      // }
      // loop through each 2D array in the 3D array
      // if (n is in the box){
      // return true;
      // }

      // return false at the very end if there are no repeats.
      // return false;
      return false;
   }

   public static void displayBoard(int[][][] arr) {
      int row = 0;
      System.out.println("A B C   D E F   G H I");
      System.out.println("  ---------------------------");
      for (int i = 0; i < 3; i++) {
         for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 1; k++) {
               String letters = "ABCDEFGHI";

               System.out.print(letters.substring(row, row + 1) + " | ");

               System.out.print(arr[i][j][k] + " ");
               System.out.print(arr[i][j][k + 1] + " ");
               System.out.print(arr[i][j][k + 2] + " ");
               System.out.print(" | ");

               System.out.print(arr[i + 1][j][k] + " ");
               System.out.print(arr[i + 1][j][k + 1] + " ");
               System.out.print(arr[i + 1][j][k + 2] + " ");
               System.out.print(" | ");

               System.out.print(arr[i + 2][j][k] + " ");
               System.out.print(arr[i + 2][j][k + 1] + " ");
               System.out.print(arr[i + 2][j][k + 2] + " ");

               row += 1;
            }
            System.out.println("|");
         }
         System.out.println("  ---------------------------");
      }
   }

}
