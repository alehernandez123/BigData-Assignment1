
#include <stdio.h>

#define N 2

void matrix_multiplication(int A[N][N], int B[N][N], int C[N][N]) {

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {

    int A[N][N] = {
        {1, 2},
        {3, 4}
    };

    int B[N][N] = {
        {5, 6},
        {7, 8}
    };

    int C[N][N] = {0};

    matrix_multiplication(A, B, C);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    return 0;
}
