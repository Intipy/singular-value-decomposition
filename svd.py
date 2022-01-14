import math
import matrix
import eigen


A = matrix.sample_1    # matrix A
A_T = [[0 for i in range(len(A))] for j in range(len(A[0])) ]   # transposed A

for i in range(len(A)):   # fill transposed A
    for j in range(len(A[0])):
        A_T[j][i] = A[i][j]



AA_T = [[0 for i in range(len(A))] for j in range(len(A))]   # A * A_T

sum = 0
for i in range(len(A)):   ## fill A * A_T
    for j in range(len(A)):
        for k in range(len(A_T)):
            sum += A[i][k] * A_T[k][j]
        AA_T[i][j] = sum
        sum = 0



A_TA = [[0 for i in range(len(A_T))] for j in range(len(A_T))]   # A_T * A

sum = 0
for i in range(len(A_T)):   ## fill A_T * A
    for j in range(len(A_T)):
        for k in range(len(A)):
            sum += A_T[i][k] * A[k][j]
        A_TA[i][j] = sum
        sum = 0



# AA_T (3, 3)
# A_TA (2, 2)
# now, we find eigenvalues and eigenvectors of AA_T and A_TA



eigenvalue_AA_T = eigen.find_eigenvalues(AA_T)   # eigenvalues of A_TA
eigenvalue_A_TA = eigen.find_eigenvalues(A_TA)   # eigenvalues of A_TA
singular_value = sorted([math.sqrt(i) for i in eigenvalue_A_TA], reverse=True)   # singular values of A

sigma = [[0 for i in range(len(A[0]))] for j in range(len(A))]   # A = U * sigma * V_T

for i in range(len(A)):
    for j in range(len(A[0])):
        if i == j:
            sigma[i][j] = singular_value[i]



for i in eigenvalue_AA_T:
    






