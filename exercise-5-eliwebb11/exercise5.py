import numpy as np

print("CS 3513, Spring 2025")
print("Exercise 5")
print("StudentName = ", "Eli Webb")
print("GitHub Username = ", "eliwebb11")

# Matrixs
A = np.array([
    [16.0, -8.0, 12.0, -32.0, 1024.0],
    [32.0, -13.0, 15.0, -91.0, 2046.0],
    [-0.32, -95.84, 301.76, 864.89, 143.52],
    [0.064, -72.032, 272.048, 648.8721, 452.096],
    [400.0, 100.0, -1048.0, 96492.0, -77800.0]])

b = np.array([2.0, -4.0, 8.0, -27.0, 25.0])

A_original = A.copy()
b_original = b.copy()

n = len(b)

for i in range(4):
    print()
    print(f"Question {i}, processing column {i}")

    pivot_row = i + np.argmax(np.abs(A[i:, i]))
    P = np.identity(n)
    if pivot_row != i:
        P[[i, pivot_row]] = P[[pivot_row, i]]

    A = P @ A
    b = P @ b

    M = np.identity(n)
    for j in range(i + 1, n):
        if A[i, i] != 0:
            factor = A[j, i] / A[i, i]
            M[j, i] = -factor

    A = M @ A
    b = M @ b

    print("P)\n", P)
    print()
    print("M)\n", M)
    print()
    print("A)\n", A)
    print()
    print("b)\n", b)

# Question 4
print()
print("Question 4")
x = np.zeros(n)
for i in reversed(range(n)):
    sum_ax = np.dot(A[i, i+1:], x[i+1:])
    x[i] = (b[i] - sum_ax) / A[i, i]

print("x = ", x)

# Question 5
print()
print("Question 5")
residual = A_original @ x - b_original
residual_norm = np.linalg.norm(residual)
print("Residual Norm = ", residual_norm)

# Question 6
print()
print("Question 6")
x_solve = np.linalg.solve(A_original, b_original)
diff_norm = np.linalg.norm(x - x_solve)
print("x  =", x_solve)
print("Difference norm =", diff_norm)