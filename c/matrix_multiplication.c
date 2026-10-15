
#include <stdio.h>
#include <stdlib.h>

int **create_matrix(int n) {
    int **matrix = malloc(n * sizeof(int *));

    if (matrix == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < n; i++) {
        matrix[i] = malloc(n * sizeof(int));

        if (matrix[i] == NULL) {
            perror("Memory allocation failed");
            exit(EXIT_FAILURE);
        }
    }

    return matrix;
}

void free_matrix(int **matrix, int n) {
    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }

    free(matrix);
}

void load_matrix(const char *filename, int **matrix, int n) {
    FILE *file = fopen(filename, "r");

    if (file == NULL) {
        perror("Error opening matrix file");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (fscanf(file, "%d", &matrix[i][j]) != 1) {
                fprintf(stderr, "Error reading matrix values\n");
                fclose(file);
                exit(EXIT_FAILURE);
            }

            if (j < n - 1) {
                if (fgetc(file) != ',') {
                    fprintf(stderr, "Invalid CSV format\n");
                    fclose(file);
                    exit(EXIT_FAILURE);
                }
            }
        }
    }

    fclose(file);
}

void matrix_multiplication(int **A, int **B, int **C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = 0;

            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: matrix_multiplication.exe <size>\n");
        return 1;
    }

    int n = atoi(argv[1]);

    if (n <= 0) {
        fprintf(stderr, "Invalid matrix size\n");
        return 1;
    }

    char filenameA[256];
    char filenameB[256];

    snprintf(filenameA, sizeof(filenameA),
             "experiments/matrix/A_%d.csv", n);

    snprintf(filenameB, sizeof(filenameB),
             "experiments/matrix/B_%d.csv", n);

    int **A = create_matrix(n);
    int **B = create_matrix(n);
    int **C = create_matrix(n);

    load_matrix(filenameA, A, n);
    load_matrix(filenameB, B, n);

    matrix_multiplication(A, B, C, n);

    printf("Matrix multiplication completed: %dx%d\n", n, n);
    printf("Result verification value: %d\n", C[0][0]);

    free_matrix(A, n);
    free_matrix(B, n);
    free_matrix(C, n);

    return 0;
}
