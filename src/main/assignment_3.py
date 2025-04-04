#Andrew Chambers
#Assignment as3b

import numpy as np

def GaussianElim() :

    #Hardcode the system of equations
    System = [
        [2, -1, 1, 6],
        [1, 3, 1, 0],
        [-1, 5, 4, -3]
    ]

    # Forward Elim
    for i in range(3):
        # Find the pivot element
        max_row = i
        for k in range(i + 1, 3):
            if abs(System[k][i]) > abs(System[max_row][i]):
                max_row = k
        
        # Make the highest in the row the head of the row
        if max_row != i:
            System[i], System[max_row] = System[max_row], System[i]

        # Make pivot point 1
        pivot = System[i][i]
        for j in range(i, 3+1): 
            System[i][j] /= pivot

        # Eliminate below the pivot
        for j in range(i+1, 3):
            factor = System[j][i]
            for k in range(i, 3+1):
                System[j][k] -= factor * System[i][k]

    # Back substitution to find the values
    x = [0,0,0]
    for i in range(2, -1, -1):
        x[i] = System[i][3]  
        for j in range(i+1, 3):
            x[i] -= System[i][j] * x[j]

  
    print(x)
    print()
    return x

#Function that solves the determinate of a System
def finddeter(System):
    det = np.prod(np.diagonal(System))
    print(det)
    print()

#Function that uses LU factorization
def LUfac():
    System =[
            [1,1,0,3],
            [2,1,-1,1],
            [3,-1,-1,2],
            [-1,2,3,-1]
            ]
    #Make a 4x4 matrix to use as the L
    L = np.zeros((4,4))
    Length = 4
    #Diagnalize the L
    for i in range(Length):
        L[i][i] = 1  

        for j in range(i + 1, Length):
            #Fill the points in L using pivot points
            L[j][i] = System[j][i] / System[i][i]

            #Use pivot to solve the row to 0
            for k in range(Length):
                System[j][k] -= L[j][i] * System[i][k]

    #Find the matrix determinant
    finddeter(System)
    #Print the L matrix
    print(np.array(L))
    print()
    #Print the U matrix
    print(np.array(System))

#Function that tells if a System is Diagnally Dominant
def DiagDom():
    System = [
        [9,0,5,2,1],
        [3,9,1,2,1],
        [0,1,7,2,3],
        [4,2,3,12,2],
        [3,2,4,0,8]
        ]
    Length = 5
    
    for i in range(Length):
        pivot = abs(System[i][i])
        for j in range(Length):
            if j != 1:
                total = abs(System[i][j])
        #See if we are not Dominant, if so state False
        if total > pivot:
            print(False)
            return False
    #We passed the test, return True
    print(True)
    return True

#Function that checks if a System is Positively Definite
def PositiveDefinite():
    System = [
        [2,2,1],
        [2,3,0],
        [1,0,2]
        ]
    #Check for eigenvalues and make sure they are positive
    return np.all(np.linalg.eigvals(System) > 0)

#Main function, runs all asked for questions in order of expected output
def main() :
     Positive = PositiveDefinite()
     print(Positive)
     print()
     Dominant = DiagDom()
     print()
     Gaussian = GaussianElim()
     factor = LUfac()
    
  

if __name__ == "__main__":
    main()    
