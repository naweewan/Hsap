import numpy as np

def spMT(Ai,Aj,Ad):

    ATi = np.zeros(max(Aj)+2, dtype = np.intp)
    ATj = np.zeros(Ai[-1], dtype = np.intp)
    ATd = np.zeros(Ai[-1])
    counter = np.zeros(max(Aj)+1, dtype = np.intp)

    for i in Aj:
        ATi[i+1]+=1
    
    ATi = np.add.accumulate(ATi)

    for i in range(len(Ai)-1): #i ranges through each row of A
        for j in range(Ai[i],Ai[i+1]): #j ranges through nnz's in ith row of A.  
            ATj[ATi[Aj[j]]+counter[Aj[j]]]=i
            ATd[ATi[Aj[j]]+counter[Aj[j]]]=Ad[j]
            counter[Aj[j]]+=1
    return([ATi,ATj,ATd])
