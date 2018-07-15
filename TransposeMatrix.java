
import java.io.*;

public class TransposeMatrix {

   public int[][] matrix = new int[200][200];
   public int numRows = 0;
   public int numCols = 0;

    public void readInput(String filename) {
       try {
           BufferedReader br = new BufferedReader(new FileReader(filename));
           String s = "";
           int i=0;
           while((s=br.readLine())!=null) {
               String[] numbers = s.split(" ");
               int j = 0;
               for(int cnt=0;cnt<numbers.length;cnt++) {
                   matrix[i][j] = Integer.parseInt(numbers[cnt]);
                   j++;
               }
               numCols = j;
               i++;
           }
           numRows = i;
       } catch(FileNotFoundException fnfe) {
           fnfe.printStackTrace();
       } catch(IOException ie) {
           ie.printStackTrace();
       }
    }

    public void transpose_inplace() {
         for(int i=0;i<numRows;i++) {
             for(int j=0;j<=i;j++) {
                 int temp = matrix[i][j];
                 matrix[i][j] = matrix[j][i];
                 matrix[j][i] = temp;
             }
         }
    }

    public int[][] transpose_extra_memory() {
        int[][] matrix_t = new int[numCols][numRows];
        for(int i=0;i<numRows;i++) {
           for(int j=0;j<numCols;j++) {
              matrix_t[j][i] = matrix[i][j];
           }
        }
        return matrix_t;
    }

    public void print_matrix(int[][] matrix, int ncols, int nrows)  {
        for(int i=0;i<numRows;i++) {
            for(int j=0;j<numCols;j++) {
                System.out.print(matrix[i][j]);
            }
            System.out.print("\n");
        }   
    }
 
    public void flip() {
         for(int i=0;i<numRows;i++) {
            for(int j=0;j<numCols/2;j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][numCols-j-1];
                matrix[i][numCols-j-1] = temp;
            }
         }
    }

    public void rotate_right(int[][] matrix, int ncols, int nrows) {
//        transpose_inplace();
        flip();
    } 
    public static void main(String[] args) {
        TransposeMatrix tm = new TransposeMatrix();
        tm.readInput(args[0]);
        System.out.println("input matrix\n");
        tm.print_matrix(tm.matrix, tm.numCols, tm.numRows);
        System.out.println("transposed matrix\n");
        tm.transpose_inplace();
        tm.print_matrix(tm.matrix, tm.numCols, tm.numRows);

        System.out.println("rotated matrix\n");
        tm.rotate_right(tm.matrix, tm.numCols, tm.numRows);
        tm.print_matrix(tm.matrix, tm.numCols, tm.numRows);
      
        //int[][] matrix_t = tm.transpose_extra_memory();
        //tm.print_matrix(matrix_t, tm.numRows, tm.numCols);
    }
}
