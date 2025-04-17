import numpy as np
from fractions import Fraction

# Read and parse matrix input
def read_matrix(prompt):
    raw = input(prompt)
    return np.array([list(map(float, row.split())) for row in raw.strip().split(';')])

# Subscript function
def subscript(n):
    return ''.join("₀₁₂₃₄₅₆₇₈₉"[int(d)] for d in str(n))

# Format matrix for pretty printing
def format_matrix(mat):
    return '\n'.join(['[' + ' '.join(f'{int(x):>3}' for x in row) + ' ]' for row in mat])

# --- Input ---
A = read_matrix("Enter the symmetric matrix A: ")
P = read_matrix("Enter the transformation matrix P: ")

# Check dimensions
if A.shape[0] != A.shape[1] or A.shape[0] != P.shape[0]:
    raise ValueError("Matrix dimensions mismatch!")

# --- Computations ---
PT = P.T
B = PT @ A @ P

# --- Output ---
print("\nMatrix of the transform is:\n")
print("B = P' A P =")
print(format_matrix(PT), "×\n", format_matrix(A), "×\n", format_matrix(P), "=\n", format_matrix(B))

# Linear transformation
print("\nThe resulting linear transform is:")
P_display = np.round(P @ np.identity(P.shape[1]), 0).astype(int)
print(f"[y₁ y₂ y₃] × \n{format_matrix(P_display.T)}")

# Show x = Py transformation
print("\nThis means the given quadratic form")
original_form = []
for i in range(A.shape[0]):
    for j in range(i, A.shape[1]):
        coeff = A[i][j] if i == j else 2 * A[i][j]
        if coeff != 0:
            xi, xj = f"x{i+1}", f"x{j+1}"
            term = f"{int(coeff)}{xi}²" if i == j else f"{int(coeff)}{xi}{xj}"
            original_form.append(term)
print(" + ".join(original_form), "under the linear transformation")

# Print x = Py
for i in range(P.shape[0]):
    expr = []
    for j in range(P.shape[1]):
        if P[i][j] != 0:
            coeff = int(P[i][j])
            part = f"{'' if coeff == 1 else '-' if coeff == -1 else coeff}y{j+1}"
            expr.append(part)
    print(f"x{i+1} = {' + '.join(expr).replace('+-', '- ')}")

# Print transformed quadratic form
print("transforms to the quadratic form:")
terms = []
for i in range(B.shape[0]):
    coeff = Fraction(B[i][i]).limit_denominator()
    if coeff != 0:
        terms.append(f"{coeff}y{subscript(i+1)}²")
print(" + ".join(terms).replace('+ -', '- '))