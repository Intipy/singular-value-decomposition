def dotProduct(vector1, vector2):
    if len(vector1) != len(vector2):
        return 'invalid arguments'
    else:
        total = 0
        for x in range(len(vector1)):
            total += vector1[x] * vector2[x]
        return total;


def add(vector1, vector2):
    newVector = []
    if len(vector1) != len(vector2):
        return 'invalid arguments'
    else:
        for x in range(len(vector1)):
            newVector.append(vector1[x] + vector2[x])
        return newVector


def getVectorMagnitude(vector):
    totalSquared = 0
    for x in vector:
        totalSquared += pow(x, 2)
    return pow(totalSquared, .5)


def getProjectionLength(vector1, vector2):
    product = dotProduct(vector1, vector2)
    magnitude = getVectorMagnitude(vector2)
    if magnitude != 0:
        return product / magnitude
    else:
        return product


def normalize(vector1):
    newVector = []
    magnitude = getVectorMagnitude(vector1)
    for x in vector1:
        if magnitude != 0:
            newVector.append(x / magnitude)
        else:
            newVector.append(x)
    return newVector


def subtract(vector1, vector2):
    newVector = []
    if len(vector1) != len(vector2):
        return 'invalid arguments'
    else:
        for x in range(len(vector1)):
            newVector.append(vector1[x] - vector2[x])
        return newVector


def scaleElements(matrix, scalar):
    if isinstance(matrix[0], list):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = matrix[row][col] * scalar
    else:
        newVector = [0 for j in range(len(matrix))]
        for x in range(len(matrix)):
            if matrix[x] != 0:
                newVector[x] = matrix[x] * scalar

        return newVector


def transpose(matrix):
    if isinstance(matrix[0], list):
        newMatrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                newMatrix[y][x] = matrix[x][y]
        return newMatrix
    else:
        newMatrix = [[0] for j in range(len(matrix))]
        for x in range(len(matrix)):
            newMatrix[x][0] = matrix[x]
        return newMatrix


def printMatrix(matrix):
    if isinstance(matrix[0], list):
        for row in matrix:
            for col in row:
                print(str(format(col, '.2f')) + "   ", end="")
            print()
    else:
        for i in matrix:
            print(str(format(i, '.2f')) + "   ", end="")

    print()


def identity(rows, cols):
    eye = [[] for j in range(rows)]
    index = 0
    for row in eye:
        for i in range(cols):
            if i == index:
                row.append(1)
            else:
                row.append(0)
        index += 1
    return eye


def cloneMatrix(matrix):
    cloneMatrix = [[0.00 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            cloneMatrix[row][col] = matrix[row][col]
    return cloneMatrix


def invertedAugmentMatrix(matrix):
    invertedAugmentMatrix = [[0.00 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            invertedAugmentMatrix[row][col] = matrix[row][col]

    index = 0
    matrixWidth = len(invertedAugmentMatrix[0])
    for row in invertedAugmentMatrix:
        for i in range(matrixWidth):
            if i == index:
                row.append(1)
            else:
                row.append(0)
        index += 1
    return invertedAugmentMatrix


def appendVector(matrix, vector):
    for row in range(len(matrix)):
        matrix[row].append(vector[row])


def getVector(matrix, index):
    vector = []
    for row in range(len(matrix)):
        vector.append(matrix[row][index])
    return vector


def inverse(matrix):
    if len(matrix) != len(matrix[0]):
        return 'Matrix is non invertible'
    else:
        invertedMatrix = invertedAugmentMatrix(matrix)
        matrixWidth = len(matrix[0])
        row = 0
        curRow = 0
        col = 0
        lastPivRow = 0
        lastPivCol = 0

        while col < matrixWidth and curRow < len(invertedMatrix):
            if invertedMatrix[curRow][col] != 0:
                lastPivRow = curRow
                lastPivCol = col
                invertedMatrix[curRow] = scaleElements(invertedMatrix[curRow], 1 / (invertedMatrix[curRow][col]))
                row = curRow + 1
                while row < len(invertedMatrix):
                    scalar = invertedMatrix[row][col] / invertedMatrix[curRow][col]
                    invertedMatrix[row] = add(scaleElements(invertedMatrix[curRow], -scalar), invertedMatrix[row])
                    row += 1
                curRow += 1
            else:
                row = curRow + 1
                while row < len(invertedMatrix):
                    if invertedMatrix[row][col] != 0:
                        temp = invertedMatrix[curRow]
                        invertedMatrix[curRow] = invertedMatrix[row]
                        invertedMatrix[row] = temp
                        col -= 1
                        break
                    row += 1
            col += 1

        col = lastPivCol;
        curRow = lastPivRow;

        while col != 0:
            if invertedMatrix[curRow][col] != 0:
                row = curRow - 1
                while row != -1:
                    scalar = invertedMatrix[row][col] / invertedMatrix[curRow][col]
                    invertedMatrix[row] = add(scaleElements(invertedMatrix[curRow], -scalar), invertedMatrix[row])
                    row -= 1
                curRow -= 1
            col -= 1

    for row in range(len(invertedMatrix)):
        invertedMatrix[row] = invertedMatrix[row][matrixWidth:]
    return invertedMatrix


def multiplyMatrices(matrix1, matrix2):
    newMatrix = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]

    for col in range(len(newMatrix[0])):
        vec = [0 for j in range(len(matrix2))]
        for row in range(len(matrix2)):
            vec[row] = matrix2[row][col]
        for row in range(len(newMatrix)):
            d = dotProduct(matrix1[row], vec)
            newMatrix[row][col] = d
    return newMatrix


def GramSchmidt(matrix):
    orthonormalMatrix = [[] for j in range(len(matrix))]
    index = 0

    for col in range(len(matrix[0])):
        originalVector = getVector(matrix, col)
        newVector = getVector(matrix, col)

        for loc in range(index):
            vecLoc = getVector(orthonormalMatrix, loc)
            projectionLength = getProjectionLength(originalVector, vecLoc)
            normalizedVec = normalize(vecLoc)
            projectionVector = scaleElements(normalizedVec, projectionLength)
            newVector = subtract(newVector, projectionVector)

        v = normalize(newVector)
        appendVector(orthonormalMatrix, v)
        index += 1

    return orthonormalMatrix


def eig(matrix):
    Qbuilder = identity(len(matrix), len(matrix[0]))
    A = cloneMatrix(matrix)

    for i in range(len(matrix[0])):
        Q = GramSchmidt(A)
        Qbuilder = multiplyMatrices(Qbuilder, Q)
        R = multiplyMatrices(inverse(Q), A)
        A = multiplyMatrices(R, Q)

    return [A, Qbuilder]


def SVD(matrix):
    AAT = multiplyMatrices(matrix, transpose(matrix))
    eigAAT = eig(AAT)
    U = eigAAT[1]
    ATA = multiplyMatrices(transpose(matrix), matrix)
    eigATA = eig(ATA)
    V = eigATA[1]
    holder = eigATA[0]
    Sigma = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for row in range(min(len(Sigma), len(Sigma[0]))):
        Sigma[row][row] = pow(holder[row][row], .5)
    return U, Sigma, transpose(V)


