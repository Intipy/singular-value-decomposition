import math
import matrix
import eigen


A = matrix.sample_1    # matrix A


U, sigma, V_T = eigen.SVD(A)


print("============1============")
eigen.printMatrix(A)
print("============2============")
eigen.printMatrix(U)
eigen.printMatrix(sigma)
eigen.printMatrix(V_T)
print("============3============")
eigen.printMatrix(eigen.multiplyMatrices(eigen.multiplyMatrices(U, sigma), V_T))







