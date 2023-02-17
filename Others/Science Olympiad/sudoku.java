import java.util.*;

public class sudoku {
   public static void main(String[] args){
      int counter = 1;
      int[][][] solution = new int[9][3][3];
      int[][][] player = new int[9][3][3];

      //right now this generates 123 456 789 in each box (run the code to see what I mean).

      for(int i = 0; i < solution.length; i++){
         for(int j = 0; j < solution[i].length; j++){
            for(int k = 0; k < solution[i][j].length; k++){
               solution[i][j][k] = counter;
               counter+=1;
            }
         }
         counter=1;
      }

      for(int i = 0; i < 9; i++){
         for(int j = 0; j < 3; j++){
            for(int k = 0; k < 1; k++){
               //see how i printed the board - use that to populate the array
               //make sure to check if there are any repeats (use a while loop)
            }
         }
      }

      //to check if the player correctly put it in the right position, match the position from the solution board to the player's board
      //to check if the player won, count the number of whitespaces at the beginning and decrement it for each correct answer. when it reaches 0, the player has won.
      //the rest should be pretty straightforward
      //let me know if you need any help :)
      


      displayBoard(solution);
   }

   public static boolean hasRepeats(int [][][] arr, int n){
      // loop through each row in the 3D array
      //    if (n is in the row){
      //       return true;
      //    }
      // loop through each column in the 3D array
      // if (n is in the column){
      //    return true;
      // }
      // loop through each 2D array in the 3D array
      // if (n is in the box){
      //    return true;
      // }
      
      // return false at the very end if there are no repeats.
      // return false;
      return false;
   }


   public static void displayBoard(int[][][] arr){
      int row = 0;
      System.out.println("A B C   D E F   G H I");
      System.out.println("  ---------------------------");
      for(int i = 0; i < 3; i++){
         for(int j = 0; j < 3; j++){
            for(int k = 0; k < 1; k++){
               String letters = "ABCDEFGHI";

               System.out.print(letters.substring(row,row+1) + " | ");

               System.out.print(arr[i][j][k] + " ");
               System.out.print(arr[i][j][k+1] + " ");
               System.out.print(arr[i][j][k+2] + " ");
               System.out.print(" | ");

               System.out.print(arr[i+1][j][k] + " ");
               System.out.print(arr[i+1][j][k+1] + " ");
               System.out.print(arr[i+1][j][k+2] + " ");
               System.out.print(" | ");

               System.out.print(arr[i+2][j][k] + " ");
               System.out.print(arr[i+2][j][k+1] + " ");
               System.out.print(arr[i+2][j][k+2] + " ");

               row+=1;
            }
            System.out.println("|");
         }
         System.out.println("  ---------------------------");
      }
   }

   
}

