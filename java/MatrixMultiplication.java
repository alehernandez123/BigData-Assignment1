public class MatrixMultiplication {

    public static int[][] matrixMultiplication(int[][] A, int[][] B) {

        int n = A.length;

        int[][] C = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        return C;
    }

    public static void main(String[] args) {

        int[][] A = {
            {1, 2},
            {3, 4}
        };

        int[][] B = {
            {5, 6},
            {7, 8}
        };

        int[][] C = matrixMultiplication(A, B);

        for (int[] row : C) {
            for (int value : row) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
    }
}