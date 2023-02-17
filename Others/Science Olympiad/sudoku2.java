import java.util.*;

public class sudoku2 {
   public static void main(String[] args){
      int [][] board = new int[9][9];
      int boxNumber = 1;

      for(int i = 0; i < board.length; i++){
         for(int j = 0; j < board[i].length; j++){
            int n = (int) Math.random()*10+1;
            
            
         }
      }
   }

   public static boolean hasRepeats(int[][] arr, int box, int row, int col, int n){
      for(int i = 0; i < 9; i++){
         if(arr[row][i] == n){
            return true;
         }
      }

      for(int i = 0; i < 9; i++){
         if(arr[i][col] == n){
            return true;
         }
      }


      return true;

   }
}
