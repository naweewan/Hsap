
import numpy as np

def spMM(Ai,Aj,Ad,Bi,Bj,Bd):
    Arow = Ai.shape[0]-1#of rows
    Acol = np.max(Aj)+1 #of cols
    Annz = Ai[-1] #of non-zero entries
    Bcol = np.max(Bj)+1
    flag = np.zeros(Bcol,dtype = np.int) #flag[k] set to i+1 after first (i,k) pair enountered  
    Ci = np.zeros(Arow+1,dtype = np.intp)
    iPointer = 0 #Counts nnz's encountered so far
    for i in range(Arow):
        Ci[i]=iPointer
        for jPointer in range(Ai[i],Ai[i+1]):
            j = Aj[jPointer]
            for kPointer in range(Bi[j],Bi[j+1]):
                k = Bj[kPointer]
                if flag[k] != i+1:
                    iPointer += 1
                    flag[k] = i+1 
               
    Ci[Arow]=iPointer
    Cj = np.zeros(iPointer,dtype = np.intp)
    Cd = np.zeros(iPointer)
    Dtemp = np.zeros(Bcol)
    iPointer = 0
    flag.fill(0)
    for i in range(Arow):
        for j in range(Ci[i],Ci[i+1]):
            Dtemp[Cj[j]]=0
        for jPointer in range(Ai[i],Ai[i+1]):
            j = Aj[jPointer]
            Adat = Ad[jPointer]
            for kPointer in range(Bi[j],Bi[j+1]):
                k = Bj[kPointer]
                Dtemp[k]=Dtemp[k]+Adat*Bd[kPointer]
                if flag[k] != i+1:
                    Cj[iPointer] = k
                    iPointer += 1
                    flag[k]  = i+1
        for j in range(Ci[i],Ci[i+1]):
            Cd[j]=Dtemp[Cj[j]]
    return([Ci,Cj,Cd])

