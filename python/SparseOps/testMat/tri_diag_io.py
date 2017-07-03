

import random as rand
import numpy as np

n = 10**6 #matrix dimensions
#m = 100

#A triDiagonal matrix with random data in "matlab" sparse format.  Every matrix entry is zero except for (Ai[k],Aj[k]) which has value Data[k].
nnz = 3*n - 2 #number of nonZero entries

Data = np.zeros(nnz)
Ai =   np.zeros(nnz, dtype = np.intp)
Aj =   np.zeros(nnz, dtype = np.intp)





for k in range(0,nnz):
    Ai[k]   = (k+1)//3
    Aj[k]   = (k+1)//3 + (k+1) % 3 -1
    Data[k] = rand.random()
    
'''    
#A dense matrix with all random entries

nnz = n**2
for k in range(0,n):
    Ai[k:k+(n-1)] = k
    
'''

#A random m x n matrix with ps of all entries nonzero.



#Write the file



file = open("tridiag_3m.txt","w")

for k in range(0,nnz):
    s = str(Ai[k]) + " " + str(Aj[k]) +  " " + str(Data[k]) + "\r" 
    file.write(s)
    
file.close()