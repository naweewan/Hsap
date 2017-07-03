import numpy as np

def spMV(Ai,Aj,Ad,w):
    v = np.zeros(len(Ai)-1)
    for k in range(len(Ai)-1):
        for j in range(Ai[k],Ai[k+1]):
            v[k] = v[k] + Ad[j]* w[Aj[j]]
    return(v)