import sympy as sym


def firstElemZero(M , i, j):
    #todo
    print("first elem zero!")
    return

def allRowZero(M, i):
    #todo
    print("all row zero")
    return

k = sym.Symbol("k")

#Must have same length
firstRow  = [1 ,2*k]
secondRow = [-1+k, k  ]

#Model
M = sym.Matrix([firstRow, secondRow, sym.zeros(2*len(secondRow)-2,len(secondRow) )])

#Logic
i = 0
det = 1
while i < 2*len(firstRow)-2:
    j = 0
    while  j < len(firstRow)-1:
        sub_m = sym.Matrix([ 
        [M[i,0], M[i,j+1]]
        ,[M[i+1, 0], M[i+1,j+1]]
        ])
        det = sym.simplify((-1*sub_m.det()/M[i+1, 0]))
        if(det == 0 and j == 0):
            firstElemZero(M, i, j)
            continue
        M[i+2, j] = det
        j += 1
    if M.row(i) == sym.zeros(1, len(firstRow)-1):
        allRowZero(M, i)
    i += 1



#Plotting Table
for i in range(len(M)//len(firstRow)):
    row = list(M.row(i))
    print(i, ": ",end = "")
    for elem in row:
        print(elem ,"\t\t", end = "")
    print("\n")

