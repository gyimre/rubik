import random
from operator import itemgetter
import re


Tk = ["LeftUp","LeftDown","RightUp","RightDown","TopLeft","TopRight","BottomLeft",
"BottomRight","FrontLeft","FrontRight","BackLeft","BackRight"]
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


# 0 Black  # 1 Blue # 2 Yellow # 3 Green # 4 Orange # 5 Red
>>> ColorsInitial = [4,2,1,0,3,2,1,5,4,3,2,5,5,0,1,4,0,1,3,4,0,5,2,3]
>>> ErrorInitial = sum([len(set(Colors[i*4:i*4+4])) for i in range(6)])
>>> ErrorInitial
>>> 24

def rubik_solve_rnd(I, max_attempts=30, max_steps=6,random_spins=3000,max_spins=10,min_spins=4):
  """
  Help on rubik solver function
  
  When you provide the current colors on the cube the function runs random emulations 
    of cube rotation series and evaulates the outcome.
  
  I: is the initial list of colors, the starting position
  max_attemps: number of complete restarts (if attempt is not successful)
  max_seqs: maximum number of evaluations
  random_spins: number of random transformation series per iteration
  max_spins: maximum lenght of an evaluation sequence
  min_spins: minimum lenght of an evaluation sequence
  """
  for attempt in range(max_attempts):
    It = I
    Ei = sum([len(set(It[i*4:i*4+4])) for i in range(6)]) #calculated from initial
    print("\n"+"\n"+"-------"+"Attempt--"+str(attempt)+"........."+"init error: "+str(Ei), flush=True)
    Ts = []           #successful rotation series to be collected
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
