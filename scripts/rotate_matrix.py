"""Rotate a rectangular matrix 90 degrees clockwise."""


def rotate_clockwise(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix or not matrix[0]:
        raise ValueError("Matrix must contain at least one value")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Matrix rows must all have the same length")
    return [list(row) for row in zip(*matrix[::-1])]


if __name__ == "__main__":
    source = [[1, 2], [3, 4]]
    for row in rotate_clockwise(source):
        print(row)
