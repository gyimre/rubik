#import os
#os.getcwd() #home/imre
#os.chdir('/home/imre/Dokumentumok')
from rubik.rubik_solve import T, Tk, rubik_solve_rnd

# 0 Black Fekete # 1 Blue Kék # 2 Yellow Sárga # 3 Green Zöld # 4 Orange Narancs # 5 Red Piros
rubik_solve_rnd([4,2,2,0,3,5,1,5,3,1,3,0,2,0,4,1,4,2,3,4,5,5,1,0], min_spins=1, max_steps=10)
rubik_solve_rnd([0,2,3,0,1,2,1,5,4,2,3,0,5,3,4,4,3,1,4,5,2,5,1,0], min_spins=1, max_steps=10)
rubik_solve_rnd([5,1,4,0,2,4,1,1,0,2,2,3,5,3,2,3,3,1,0,4,0,5,4,5], min_spins=1, max_steps=11)
rubik_solve_rnd([5,0,3,0,1,5,1,4,3,1,2,0,5,3,3,4,2,2,0,4,2,5,4,1], min_spins=1, max_steps=11)
rubik_solve_rnd([0,0,0,0,1,2,1,4,5,2,2,4,1,3,3,3,5,3,4,4,5,5,2,1], min_spins=1, max_steps=11)
rubik_solve_rnd([5,2,3,0,3,5,1,4,3,3,2,4,0,1,1,5,4,2,2,4,0,5,0,1], min_spins=1, max_steps=11)


rubik_solve_rnd([4,4,3,0,4,1,1,4,5,5,1,5,3,2,3,3,2,2,1,2,0,5,0,0], min_spins=1, max_steps=11)

