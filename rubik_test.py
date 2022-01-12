A = list(range(0,24))
A[20:]
len(A)

# nice to haves
# not the same transformation again after two identical
# entropy reduction (with tresholds allowing little negative progress); number of colors per side is reducing or not

import random

Tk = ["LeftUp","LeftDown","RightUp","RightDown","TopLeft","TopRight","BottomLeft","BottomRight"]
Tk[random.choice(range(8))]

T = {}
T["LeftUp"]    =   [20,1,22,3,4,5,6,7,8,18,10,16,13,15,12,14,0,17,2,19,11,21,9,23]
T["LeftDown"]  =   [16,1,18,3,4,5,6,7,8,22,10,20,14,12,15,13,11,17,9,19,0,21,2,23]
T["RightUp"]   =   [0,21,2,23,6,4,7,5,19,9,17,11,12,13,14,15,16,1,18,3,20,10,22,8]
T["RightDown"] =   [0,17,2,19,5,7,4,6,23,9,21,11,12,13,14,15,16,10,18,8,20,1,22,3]
T["TopLeft"]   =   [4,5,2,3,8,9,6,7,12,13,10,11,0,1,14,15,18,16,19,17,20,21,22,23]
T["TopRight"]  =   [12,13,2,3,0,1,6,7,4,5,10,11,8,9,14,15,17,19,16,18,20,21,22,23]
T["BottomLeft"] =  [0,1,6,7,4,5,10,11,8,9,14,15,12,13,2,3,16,17,18,19,21,23,20,22]
T["BottomRight"] = [0,1,14,15,4,5,2,3,8,9,6,7,12,13,10,11,16,17,18,19,22,20,23,21]

T
T["BottomRight"]

[A[i] for i in T["BottomRight"]]

from operator import itemgetter
list(itemgetter(*T["BottomRight"])(A))

# 0 Black # 1 Blue # 2 Yellow # 3 Green # 4 Orange # 5 Red
I = [4,3,0,0,5,5,1,5,2,2,2,2,4,1,4,4,1,1,0,0,3,5,3,3]
len(I)

list(itemgetter(*T["BottomRight"])(I))
list(itemgetter(*T[Tk[random.choice(range(8))]])(I))


t = Tk[random.choice(range(8))]
print(t)
It = list(itemgetter(*T[t])(I))

t = Tk[random.choice(range(8))]
print(t)
It = list(itemgetter(*T[t])(It))
len(set(It[0:4])) == 1

e = sum([len(set(It[i*4:i*4+4])) for i in range(6)])
if e == 6:
  return Ts

for i in range(10):
  Ts = []
  It = I
  E = []
  for j in range(10000):
    t = Tk[random.choice(range(8))]
    Ts.append(t)
    It = list(itemgetter(*T[t])(It))
    e = sum([len(set(It[i*4:i*4+4])) for i in range(6)])
    E.append(e)
    if e == 6:
      print(Ts)


from matplotlib import pyplot as plt
plt.plot(E)
plt.show()

# 0 Black # 1 Blue # 2 Yellow # 3 Green # 4 Orange # 5 Red
I = [1,2,4,0, 5,1,1,3, 5,3,4,1, 5,0,4,2, 0,2,4,3, 3,5,2,0]
len(I)

for i in range(10000):
  It = I
  Ts = []
  E = []
  for j in range(30):
    et = 100
    tt = "LeftUp"
    if random.random() >.67:
      tt = Tk[random.choice(range(8))]
    else:
      for k in range(8):
        t = Tk[k]
        Itt = list(itemgetter(*T[t])(It))
        x = sum([len(set(Itt[i*4:i*4+4])) for i in range(6)])
        if x < et:
          et = x
          tt = t
    
    It = list(itemgetter(*T[tt])(It))
    e = sum([len(set(It[i*4:i*4+4])) for i in range(6)])
    if e < 10:
      print(Ts)
      print(E)
      print(e)
      break
    
    E.append(e)
    Ts.append(tt)




plt.plot(E)
plt.show()
Ts

min(E)


#loop to try 4-10 long random sequence then only evaluate and move on with it if entropy is lower
import random
from operator import itemgetter

Tk = ["LeftUp","LeftDown","RightUp","RightDown","TopLeft","TopRight","BottomLeft","BottomRight","FrontLeft","FrontRight","BackLeft","BackRight"]
Tk[random.choice(range(12))]

T = {}
T["LeftUp"]    =   [20,1,22,3,4,5,6,7,8,18,10,16,13,15,12,14,0,17,2,19,11,21,9,23]
T["LeftDown"]  =   [16,1,18,3,4,5,6,7,8,22,10,20,14,12,15,13,11,17,9,19,0,21,2,23]
T["RightUp"]   =   [0,21,2,23,6,4,7,5,19,9,17,11,12,13,14,15,16,1,18,3,20,10,22,8]
T["RightDown"] =   [0,17,2,19,5,7,4,6,23,9,21,11,12,13,14,15,16,10,18,8,20,1,22,3]
T["TopLeft"]   =   [4,5,2,3,8,9,6,7,12,13,10,11,0,1,14,15,18,16,19,17,20,21,22,23]
T["TopRight"]  =   [12,13,2,3,0,1,6,7,4,5,10,11,8,9,14,15,17,19,16,18,20,21,22,23]
T["BottomLeft"] =  [0,1,6,7,4,5,10,11,8,9,14,15,12,13,2,3,16,17,18,19,21,23,20,22]
T["BottomRight"] = [0,1,14,15,4,5,2,3,8,9,6,7,12,13,10,11,16,17,18,19,22,20,23,21]
T["FrontLeft"]  =  [1,3,0,2,21,5,20,7,8,9,10,11,12,19,14,18,16,17,4,6,13,15,22,23]
T["FrontRight"] =  [2,0,3,1,18,5,19,7,8,9,10,11,12,20,14,21,16,17,15,13,6,4,22,23]
T["BackLeft"]  =   [0,1,2,3,4,23,6,22,10,8,11,9,17,13,16,15,5,7,18,19,20,21,12,14]
T["BackRight"] =   [0,1,2,3,4,16,6,17,9,11,8,10,22,13,23,15,14,12,18,19,20,21,7,5]

# 0 Black # 1 Blue # 2 Yellow # 3 Green # 4 Orange # 5 Red
I = [0,0,0,0, 1,2,1,3, 1,5,2,4, 3,3,2,3, 2,5,4,4, 5,5,1,4] #initial setup#


for m in range(20):
  Ei = sum([len(set(I[i*4:i*4+4])) for i in range(6)]) #calculated from initial
  print("\n"+"\n"+"-------"+"Attempt--"+str(m)+"........."+"init error: "+str(Ei), flush=True)
  It = I
  Ts = []           #successful transformation step to be collected
  for j in range(6): #transformations starting from initial setup
    E = sum([len(set(It[i*4:i*4+4])) for i in range(6)])
    for i in range(10,4,-1): #gradually decrease! (so prefer longer ones) the number of spins between evaluations
      r = min(2*8**i,3000)
      for l in range(r): #try random spins many times per each length (i)
        Itt = It
        Tst = []
        for k in range(i):
          tt = Tk[random.choice(range(8))]    #random selection of the transformation
          Itt = list(itemgetter(*T[tt])(Itt)) #transformation applied -> Itt
          Tst.append(tt)
        Et = sum([len(set(Itt[i*4:i*4+4])) for i in range(6)])
        if Et<E:
          It = Itt        #accept the transformations sequence (1-10 steps long)
          Ts.append(Tst)  #store the successful sequence
          print("STEP-"+str(j)+" ERROR: " + str(Et)+" seqlen-"+str(i)+" iteration-"+str(l), flush=True)
          break           # l loop - random search with i lenght - was successful
      if Et<E:
        break  # i loop has to be interrupted as well!
    if Et==6:
      print(Ts, flush=True)
      break
    else:
      continue
  if Et==6:
    break


# 0 Black # 1 Blue # 2 Yellow # 3 Green # 4 Orange # 5 Red
I = [0,0,0,0, 1,2,1,3, 1,5,2,4, 3,3,2,3, 2,5,4,4, 5,5,1,4] #initial setup#
[
['BottomLeft', 'BottomRight', 'LeftDown', 'RightDown', 'RightDown', 'LeftDown', 'TopLeft', 'BottomLeft', 'LeftDown', 'LeftDown'], 
['BottomLeft', 'RightDown', 'BottomLeft', 'LeftDown', 'BottomRight', 'TopLeft', 'BottomLeft', 'BottomRight', 'BottomLeft', 'RightDown'], 
['RightDown', 'RightDown', 'LeftDown', 'BottomLeft', 'TopLeft', 'RightUp', 'LeftDown', 'BottomLeft', 'LeftUp', 'LeftUp'], 
['BottomRight', 'TopLeft', 'RightDown', 'RightDown', 'TopRight', 'BottomRight', 'BottomLeft', 'BottomLeft', 'TopRight'], 
['LeftDown', 'LeftDown', 'TopLeft', 'TopLeft', 'RightUp', 'LeftUp', 'RightDown', 'LeftDown', 'RightDown', 'RightDown']
]

def rubik(I):
  for m in range(20):
    Ei = sum([len(set(I[i*4:i*4+4])) for i in range(6)]) #calculated from initial
    print("\n"+"\n"+"-------"+"Attempt--"+str(m)+"........."+"init error: "+str(Ei), flush=True)
    It = I
    Ts = []           #successful transformation step to be collected
    for j in range(6): #transformations starting from initial setup
      E = sum([len(set(It[i*4:i*4+4])) for i in range(6)])
      for i in range(10,4,-1): #gradually decrease! (so prefer longer ones) the number of spins between evaluations
        r = min(2*8**i,3000)
        for l in range(r): #try random spins many times per each length (i)
          Itt = It
          Tst = []
          for k in range(i):
            tt = Tk[random.choice(range(8))]    #random selection of the transformation
            Itt = list(itemgetter(*T[tt])(Itt)) #transformation applied -> Itt
            Tst.append(tt)
          Et = sum([len(set(Itt[i*4:i*4+4])) for i in range(6)])
          if Et<E:
            It = Itt        #accept the transformations sequence (1-10 steps long)
            Ts.append(Tst)  #store the successful sequence
            print("STEP-"+str(j)+" ERROR: " + str(Et)+" seqlen-"+str(i)+" iteration-"+str(l), flush=True)
            break           # l loop - random search with i lenght - was successful
        if Et<E:
          break  # i loop has to be interrupted as well!
      if Et==6:
        print(Ts, flush=True)
        break
      else:
        continue
    if Et==6:
      break


# 0 Black # 1 Blue # 2 Yellow # 3 Green # 4 Orange # 5 Red
I = [0,4,4,0,1,3,1,4,5,3,3,1,2,3,2,0,5,0,4,2,1,5,5,2]
for i in range(6):[j for j in I if j==i]

rubik(I)

import random
from operator import itemgetter
import re

def rubik(I, max_attempts=20, max_seqs=6,random_spins=3000,max_spins=10,min_spins=4):
  """
  Help on rubik solver function
  
  this functions tries to solve Rubik cubes. 
  When you provide the current colors on the cube the function runs random emulations 
    of cube transformation series and evaulates the outcome.
  
  max_attemps: number of complete restarts (if attempt is not successful)
  max_seqs: maximum number of evaluations
  random_spins: number of random transformation series per iteration
  max_spins: maximum lenght of an evaluation sequence
  min_spins: minimum lenght of an evaluation sequence
  """
  for attempt in range(max_attempts):
    Ei = sum([len(set(I[i*4:i*4+4])) for i in range(6)]) #calculated from initial
    print("\n"+"\n"+"-------"+"Attempt--"+str(attempt)+"........."+"init error: "+str(Ei), flush=True)
    It = I
    Ts = []           #successful transformation steps to be collected
    for seq in range(max_seqs): #transformations starting from initial setup
      E = sum([len(set(It[i*4:i*4+4])) for i in range(6)])
      #for spins in range(max_spins,min_spins,-1): #gradually decrease! (so prefer longer ones) the number of spins between evaluations
      for spins in range(min_spins,max_spins):
        for random_spin in range(random_spins): #try random spins many times per each length (i)
          Itt = It
          Tst = []
          for k in range(spins):
            tt = Tk[random.choice(range(12))]    #random selection of the transformation
            Itt = list(itemgetter(*T[tt])(Itt)) #transformation applied -> Itt
            Tst.append(tt)
          Et = sum([len(set(Itt[i*4:i*4+4])) for i in range(6)])
          if Et<E:
            It = Itt        #accept the transformations sequence (1-10 steps long)
            Ts.append(Tst)  #store the successful sequence
            print("STEP-"+str(seq)+" ERROR: " + str(Et)+" seqlen-"+str(spins)+" iteration-"+str(random_spin), flush=True)
            break           # l loop - random search with i lenght - was successful
        if Et<E:
          break  # i loop has to be interrupted as well!
      if Et==6:
        #print(Ts, flush=True)
        A = []
        for ts in Ts:
          for t in ts:A.append(t)
        
        for i in range(len(A)):
          for j in range(len(A)):
            if j<len(A)-1 and \
            re.findall('[A-Z][^A-Z]*',A[j])[0]==re.findall('[A-Z][^A-Z]*',A[j+1])[0] and \
            re.findall('[A-Z][^A-Z]*',A[j])[1]!=re.findall('[A-Z][^A-Z]*',A[j+1])[1]:
              A[j:j+2]
              del A[j:j+2]
              break
            else:
              continue
        
        x = 0
        for a in A:
          print("\n"+"Solution"+"\n")
          print(str(x)+" "+a)
          x+=1
        
        return A
        
        break
      else:
        continue
    if Et==6:
      break




# 0 Black # 1 Blue # 2 Yellow # 3 Green # 4 Orange # 5 Red
I = [3,3,0,0,0,2,1,3,4,5,2,1,3,0,2,1,2,1,5,4,4,5,5,4]
rubik(I, max_seqs=10)
rubik(I, max_seqs=10, min_spins=1)

I = [4,1,5,0,4,2,1,3,4,3,4,5,5,3,1,3,0,1,2,0,2,5,2,0]
for i in range(6):[j for j in I if j==i]

rubik(I, max_seqs=10, min_spins=1)

A = rubik(I, max_seqs=10, min_spins=1)








import random
from operator import itemgetter
import re

def rubik(I, max_attempts=20, max_steps=6,random_spins=3000,max_spins=10,min_spins=4):
  """
  Help on rubik solver function
  
  this functions tries to solve Rubik cubes. 
  When you provide the current colors on the cube the function runs random emulations 
    of cube transformation series and evaulates the outcome.
  
  max_attemps: number of complete restarts (if attempt is not successful)
  max_seqs: maximum number of evaluations
  random_spins: number of random transformation series per iteration
  max_spins: maximum lenght of an evaluation sequence
  min_spins: minimum lenght of an evaluation sequence
  """
  for attempt in range(max_attempts):
    Ei = sum([len(set(I[i*4:i*4+4])) for i in range(6)]) #calculated from initial
    print("\n"+"\n"+"-------"+"Attempt--"+str(attempt)+"........."+"init error: "+str(Ei), flush=True)
    It = I
    Ts = []           #successful transformation steps to be collected
    for step in range(max_steps): #transformations starting from initial setup
      E = sum([len(set(It[i*4:i*4+4])) for i in range(6)])
      #for spins in range(max_spins,min_spins,-1): #gradually decrease! (so prefer longer ones) the number of spins between evaluations
      for spins in range(min_spins,max_spins):
        found = False
        for random_spin in range(random_spins): #try random spins many times per each length (i)
          Itt = It
          Tst = []
          for k in range(spins):
            tt = Tk[random.choice(range(12))]    #random selection of the transformation
            Itt = list(itemgetter(*T[tt])(Itt)) #transformation applied -> Itt
            Tst.append(tt)
          Et = sum([len(set(Itt[i*4:i*4+4])) for i in range(6)])
          if Et<E:
            found = True
            It = Itt        #accept the transformations sequence (1-10 steps long)
            Ts.append(Tst)  #store the successful sequence
            print("STEP-"+str(step)+" ERROR: " + str(Et)+" seqlen-"+str(spins)+" iteration-"+str(random_spin), flush=True)
            break           # l loop - random search with i lenght - was successful
        if Et<E:
          break  # minmax spins loop has to be interrupted as well!
      if Et==6:
        #print(Ts, flush=True)
        A = []
        for ts in Ts:
          for t in ts:A.append(t)
        
        for i in range(len(A)):
          for j in range(len(A)):
            if j<len(A)-1 and \
            re.findall('[A-Z][^A-Z]*',A[j])[0]==re.findall('[A-Z][^A-Z]*',A[j+1])[0] and \
            re.findall('[A-Z][^A-Z]*',A[j])[1]!=re.findall('[A-Z][^A-Z]*',A[j+1])[1]:
              A[j:j+2]
              del A[j:j+2]
              break
            else:
              continue
        
        print("\n"+"Solution"+"\n")
        x = 0
        for a in A:
          print(str(x)+" "+a)
          x+=1
        
        print("\n"+"List returned"+"\n")
        
        return A



I = [4,1,5,0,4,2,1,3,4,3,4,5,5,3,1,3,0,1,2,0,2,5,2,0]
for i in range(6):[j for j in I if j==i]

rubik(I, max_steps=10, min_spins=1)

I = [i for i in range(6) for j in range(4)]
rubik(I, max_steps=10, min_spins=1)


I = [5,0,4,0,1,5,1,0,2,1,5,2,2,2,4,3,4,1,3,4,0,5,3,3]
for i in range(6):[j for j in I if j==i]

rubik(I, max_steps=10, min_spins=1)


I = [i for i in range(6) for j in range(4)]
rubik(I, max_steps=10, min_spins=1)

#from solved cube to max entropy in only 5 steps
#0 LeftDown
#1 BackLeft
#2 RightUp
#3 FrontRight
#4 RightUp

# 0 Black # 1 Blue # 2 Yellow # 3 Green # 4 Orange # 5 Red
#from max entropy to solution?
I = [4,2,2,0,3,5,1,5,3,1,3,0,2,0,4,1,4,2,3,4,5,5,1,0]
for i in range(6):[j for j in I if j==i]

rubik(I, max_steps=10, min_spins=1)



#-------Attempt--0.........init error: 21
#STEP-0 ERROR: 17 seqlen-1 iteration-1
#STEP-1 ERROR: 16 seqlen-1 iteration-0
#STEP-2 ERROR: 15 seqlen-3 iteration-196
#STEP-3 ERROR: 14 seqlen-4 iteration-798
#STEP-4 ERROR: 12 seqlen-4 iteration-111
#STEP-5 ERROR: 10 seqlen-8 iteration-2584
#STEP-6 ERROR: 6 seqlen-1 iteration-1

