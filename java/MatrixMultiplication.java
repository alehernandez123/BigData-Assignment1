
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class MatrixMultiplication {

    public static int[][] loadMatrix(String filename, int n) throws IOException {
        int[][] matrix = new int[n][n];

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            for (int i = 0; i < n; i++) {
                String line = reader.readLine();

                if (line == null) {
                    throw new IOException("Missing matrix rows");
                }

                String[] values = line.split(",");

                if (values.length != n) {
                    throw new IOException("Invalid matrix dimensions");
                }

                for (int j = 0; j < n; j++) {
                    matrix[i][j] = Integer.parseInt(values[j].trim());
                }
            }

            if (reader.readLine() != null) {
                throw new IOException("Too many matrix rows");
            }
        }

        return matrix;
    }

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

    public static void main(String[] args) throws IOException {
        if (args.length != 1) {
            System.out.println("Usage: java MatrixMultiplication <size>");
            return;
        }

        int n = Integer.parseInt(args[0]);

        String matrixDir = "experiments/matrix/";

        int[][] A = loadMatrix(matrixDir + "A_" + n + ".csv", n);
        int[][] B = loadMatrix(matrixDir + "B_" + n + ".csv", n);

        int[][] C = matrixMultiplication(A, B);

        System.out.println("Matrix multiplication completed: " + n + "x" + n);
        System.out.println("Result verification value: " + C[0][0]);
    }
}
