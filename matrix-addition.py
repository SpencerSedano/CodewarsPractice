def matrix_addition(x, y):

    result = [[x[i][j] + y[i][j]  for j in range(len(x[0]))] for i in range(len(x))]
    
    return result
    
    '''
    for r in result:
        print(r)
    '''