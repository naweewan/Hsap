import spMM
import spMV
import spMT
import time
import numpy as np

#read in file

print("Enter filename:")
filename = input()

with open(filename,"r") as rawdata:
    nums  = rawdata.read().split()

with open(filename,"r") as rawdata:
    first = len(rawdata.readlines()[0].split())

if first == 3:
    Is = np.asarray([int(v) for i,v in enumerate(nums) if i%3 == 0  ])
    Js = np.asarray([int(v) for i,v in enumerate(nums) if i%3 == 1  ])
    Ds = np.asarray([float(v) for i,v in enumerate(nums) if i%3 == 2  ])
elif first == 2:
    Is = np.asarray([int(v) for i,v in enumerate(nums) if i%2 == 0  ])
    Js = np.asarray([int(v) for i,v in enumerate(nums) if i%2 == 1  ])
    Ds = np.ones(len(Js))
else:
    print("Input Error: txt file not formatted correctly")    

# construct Aj.  

temp = [Js,Is]
index = np.lexsort(temp)
Aj = np.asarray([ Js[index[i]] for i in range(len(Js))])
Ad = np.asarray([ Ds[index[i]] for i in range(len(Js))])

#Note: Aj is sorted wrt to each row-block. 
 
# construct Ai

Ai = np.zeros(max(Is)+2,dtype = np.intp)   
for k in Is:
        Ai[k+1] += 1    
Ai = np.add.accumulate(Ai)

#print matrix info

print("Testing a "+ str(Ai.shape[0]-1) +" by "+ str(Aj.max()+1) +" matrix A with " + str(Ai[-1]) + " non-zero entries.")



w = np.random.rand((max(Aj)+1))


#sparse matrix vector product

start_time=time.time()

spMV.spMV(Ai,Aj,Ad,w)

dt = time.time() - start_time

print("time for sparse matrix vector product:")
print(str(dt) + " seconds")

#sparse matrix transpose

start_time=time.time()

spMT.spMT(Ai,Aj,Ad)

dt = time.time() - start_time

print("time for sparse transpose:")
print(str(dt) + " seconds")

#sparse Matrix squared

start_time = time.time()
    
C = spMM.spMM(Ai,Aj,Ad,Ai,Aj,Ad)    

dt = time.time() - start_time

print("squared matrix has " + str(C[0][-1]) + " non-zero entries")
print("time for sparse square:")
print(str(dt) + " seconds")

