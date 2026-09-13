def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    import numpy as np

    K = len(a[0]) #No. of columns for A and rows for B
    M = len(a)
    rows_b = len(b)
    N = len(b[0])
    
    if K != rows_b:
        return -1

    c = []
    for i in range(M):
        for j in range(N):
            result = 0
            for k in range(K):
                result += a[i][k] * b[k][j]

            c.append(result)
    matrix_c = np.array(c).reshape(M, N)

    return matrix_c.tolist()