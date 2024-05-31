import numpy as np


def calculate(list):
    MATRIX_ROWS = 3
    MATRIX_COLS = 3

    if len(list) != MATRIX_ROWS * MATRIX_COLS:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(MATRIX_ROWS, MATRIX_COLS)

    calculations = {
        "mean": [
            np.mean(a=matrix, axis=0).tolist(),
            np.mean(a=matrix, axis=1).tolist(),
            np.mean(a=matrix),
        ],
        "variance": [
            np.var(a=matrix, axis=0).tolist(),
            np.var(a=matrix, axis=1).tolist(),
            np.var(a=matrix),
        ],
        "standard deviation": [
            np.std(a=matrix, axis=0).tolist(),
            np.std(a=matrix, axis=1).tolist(),
            np.std(a=matrix),
        ],
        "max": [
            np.max(a=matrix, axis=0).tolist(),
            np.max(a=matrix, axis=1).tolist(),
            np.max(a=matrix),
        ],
        "min": [
            np.min(a=matrix, axis=0).tolist(),
            np.min(a=matrix, axis=1).tolist(),
            np.min(a=matrix),
        ],
        "sum": [
            np.sum(a=matrix, axis=0).tolist(),
            np.sum(a=matrix, axis=1).tolist(),
            np.sum(a=matrix),
        ],
    }

    return calculations
