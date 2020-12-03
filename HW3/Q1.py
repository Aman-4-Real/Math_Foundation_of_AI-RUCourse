import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import time
from tqdm import *

nodenum = 500

def RandGenerate(nodesnum):
    G = nx.Graph()
    #随机生成邻接矩阵
    AdjMatrix = np.array(random.randint((2),size=(nodesnum, nodesnum)))
    for i in range(len(AdjMatrix)):
        for j in range(len(AdjMatrix)):
            if AdjMatrix[i, j]!= 0:
                AdjMatrix[j, i] = 1
                G.add_edge(i, j)
#     print(AdjMatrix)
#     nx.draw(G)
#     plt.show()
    D = np.zeros((nodesnum, nodesnum))
    for i in range(nodesnum):
        D[i][i] = sum(AdjMatrix[i])
    return D, AdjMatrix

def Calculator(D, AdjMatrix):
    A = AdjMatrix
    epsilon = 0.000000000001
    Laplacian = D - A
#     print(D)
    D_inv = np.linalg.inv(D)
    D_inv_A = np.matmul(D_inv, A)
    D_inv_A_eig = np.linalg.eigvals(D_inv_A)
    Laplacian_eig = np.linalg.eigvals(Laplacian)
    D_inv_A_eig = sorted(D_inv_A_eig, reverse=True)
    Laplacian_eig = sorted(Laplacian_eig, reverse=True)
    r = D_inv_A_eig[0] / (D_inv_A_eig[1] + epsilon)
    return r, Laplacian_eig[-2]

res = []
with tqdm(total=nodenum, ncols = 100) as pbar:
    for i in range(5, nodenum, 1):
        pbar.update(1)
        # time.sleep(0.5)
        D, A = RandGenerate(i)
        tmp = [D[j][j] for j in range(i)]
        #排除奇异矩阵
        if 0 in tmp:
            continue
        else:
            r, eig = Calculator(D, A)
        if np.dtype(r) == int or np.dtype(r) == float:
            res.append(np.array([r, eig]))
        else:
            print("随机生成的矩阵计算后包含虚数，请重试！")
            exit(0)

res = sorted(res, key= lambda x: x[0])
res = np.array(res)
# print(res)
plt.scatter(res[:, 0], res[:, 1], marker="o", s=5)
plt.xlabel("Ratio r")
plt.ylabel("2nd smallest λ")
plt.show()