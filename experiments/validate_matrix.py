
import sys
from pathlib import Path

# Import Python implementation
project_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_dir / "python"))

from matrix_multiplication import matrix_multiplication


def test_identity_matrix():
    A = [
        [1, 2],
        [3, 4]
    ]

    I = [
        [1, 0],
        [0, 1]
    ]

    result = matrix_multiplication(A, I)

    assert result == A, "Identity matrix test failed"
    print("Identity matrix test: PASSED")


def test_zero_matrix():
    A = [
        [1, 2],
        [3, 4]
    ]

    Z = [
        [0, 0],
        [0, 0]
    ]

    result = matrix_multiplication(A, Z)

    assert result == Z, "Zero matrix test failed"
    print("Zero matrix test: PASSED")


def test_known_result():
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]

    expected = [
        [19, 22],
        [43, 50]
    ]

    result = matrix_multiplication(A, B)

    assert result == expected, "Known result test failed"
    print("Known result test: PASSED")


def main():
    test_identity_matrix()
    test_zero_matrix()
    test_known_result()

    print("All validation tests passed!")


if __name__ == "__main__":
    main()