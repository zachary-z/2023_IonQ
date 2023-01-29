import numpy as np
import random

seed = 100

random.seed(seed)

# list of elements
size = 128
frames = 128
iterations_per_frame = 4000

Lattice = [[random.choice([-1,1]) for x in range(size)] for y in range(size)]

def update(i):
    for _ in range(iterations_per_frame):
        x, y = random.randint(0,size-1), random.randint(0,size-1)
        
        C = Lattice[y][x]
        N = Lattice[(y-1)%size][x]
        E = Lattice[y][(x+1)%size]
        S = Lattice[(y+1)%size][x]
        W = Lattice[y][(x-1)%size]

        H = (C==N) + (C==E) + (C==S) + (C==W) # low H corresponds to high energy
        if H < 1:
            Lattice[y][x] *= -1
        elif random.uniform(0,1) < 2**(-4*(H-2)):
            Lattice[y][x] *= -1

for i in range(1,frames):
    update(i)

# delete lone pixels
for x in range(size):
    for y in range(size):
        C = Lattice[y][x]
        N = Lattice[(y-1)%size][x]
        E = Lattice[y][(x+1)%size]
        S = Lattice[(y+1)%size][x]
        W = Lattice[y][(x-1)%size]

        H = (C==N) + (C==E) + (C==S) + (C==W)

        if H < 1: Lattice[y][x] *= -1

for x in range(size):
    for y in range(size):
        if Lattice[y][x] == -1:
            Lattice[y][x] = 0

print(Lattice)