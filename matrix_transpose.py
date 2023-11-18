# This program takes input for a matrix, displays the original matrix,
# and then prints its transpose.)


# Prompt the user to input the number of rows and columns for the matrix
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

# Initialize a_matrix and b_matrix
a_matrix = [[0 for _ in range(c)] for _ in range(r)]
b_matrix = [[0 for _ in range(r)] for _ in range(c)]

# Fill a_matrix
print(f"Enter integer values for a {r}x{c} matrix:")
for i in range(r):
    for j in range(c):
        a_matrix[i][j] = int(input(f"Enter value at position [{i}][{j}]: "))

# Display original matrix
print(f"\nOriginal Matrix ({r}x{c}):")
for row in a_matrix:
    print(row)

# Transpose the matrix
for i in range(r):
    for j in range(c):
        b_matrix[j][i] = a_matrix[i][j]

# Display transposed matrix
print(f"\nTranspose of the Matrix ({c}x{r}):")
for row in b_matrix:
    print(row)
