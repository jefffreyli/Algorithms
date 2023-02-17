import java.util.Random;

public class sudoku3 {
   // Size of the Sudoku grid
   private static final int GRID_SIZE = 9;
   // Number of blocks in each row/column
   private static final int BLOCK_SIZE = 3;

   public static void main(String[] args) {
      // Create a 3D array to represent the Sudoku grid
      int[][][] grid = new int[GRID_SIZE][GRID_SIZE][GRID_SIZE];

      // Generate the Sudoku grid
      generateSudoku(grid);

      // Print the Sudoku grid
      printSudoku(grid);
   }

   private static void generateSudoku(int[][][] grid) {
      Random random = new Random();

      // Generate a random solution for the Sudoku grid
      for (int i = 0; i < GRID_SIZE; i++) {
         for (int j = 0; j < GRID_SIZE; j++) {
            for (int k = 0; k < GRID_SIZE; k++) {
               int value = random.nextInt(GRID_SIZE) + 1;
               if (isValid(grid, i, j, k, value)) {
                  grid[i][j][k] = value;
               } else {
                  k--;
               }
            }
         }
      }
   }

   private static boolean isValid(int[][][] grid, int x, int y, int z, int value) {
      // Check if the value is already present in the row
      for (int i = 0; i < GRID_SIZE; i++) {
         if (grid[x][y][i] == value) {
            return false;
         }
      }

      // Check if the value is already present in the column
      for (int i = 0; i < GRID_SIZE; i++) {
         if (grid[x][i][z] == value) {
            return false;
         }
      }

      // Check if the value is already present in the block
      int blockStartX = x - x % BLOCK_SIZE;
      int blockStartY = y - y % BLOCK_SIZE;
      int blockStartZ = z - z % BLOCK_SIZE;
      for (int i = blockStartX; i < blockStartX + BLOCK_SIZE; i++) {
         for (int j = blockStartY; j < blockStartY + BLOCK_SIZE; j++) {
            for (int k = blockStartZ; k < blockStartZ + BLOCK_SIZE; k++) {
               if (grid[i][j][k] == value) {
                  return false;
               }
            }
         }
      }

      // The value is not present in the row, column, or block, so it is valid
      return true;
   }

   private static void printSudoku(int[][][] grid) {
      for (int i = 0; i < GRID_SIZE; i++) {
         for (int j = 0; j < GRID_SIZE; j++) {
            for (int k = 0; k < GRID_SIZE; k++) {
               System.out.print(grid[i][j][k] + " ");
            }
            System.out.println();
         }
         System.out.println();
      }
   }
}
