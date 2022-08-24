from Matris.matris import Matris

matrisA = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

matrisB = [
    [1,0,1],
    [1,0,5],
    [1,0,1]
]


A = Matris(matrisB) # Random data
B = Matris(matrisA)

print(A + B)
