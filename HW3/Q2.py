import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

level = 15 #三角形图共15层
G = nx.Graph()

for i in range(level):
    for j in range(i+1):
        if i+1 < level: #非最后一排
            #向下连接
            G.add_edge(str(int(i*(i+1)/2+j+1)),str(int(i*(i+1)/2+j+1+i+1)), length=2)
            G.add_edge(str(int(i*(i+1)/2+j+1)),str(int(i*(i+1)/2+j+1+i+2)), length=2)
            if i != j: # 横向连接
                G.add_edge(str(int(i*(i+1)/2+j+1)),str(int(i*(i+1)/2+j+2)), length=20)
        else: #最后一排，只做横向连接
            if i != j:
                G.add_edge(str(int(i*(i+1)/2+j+1)),str(int(i*(i+1)/2+j+2)), length=20)

positions=nx.spectral_layout(G)
fig, ax = plt.subplots()
nx.draw(G, ax=ax, with_labels=True, pos=positions, node_color='y')
plt.show()

A = nx.to_numpy_array(G)
# print(A)
nodes_num = G.number_of_nodes()
D = np.zeros(shape=(nodes_num, nodes_num))
degree_list = G.degree
# print(G.degree)
for i, pair in enumerate(degree_list):
    D[i, i] = pair[1]
# print(D)
Lapac = D - A
Lapac_eig, eigvec = np.linalg.eig(Lapac)
zipped = zip(Lapac_eig, eigvec) #合并起来
sort_zipped = sorted(zipped, key=lambda x:(x[0])) #按特征值大小排序
result = zip(*sort_zipped) #拆分
L_eigvalues, L_eigvetors = [list(x) for x in result]
L_eigvetors = [x.tolist() for x in L_eigvetors]
L_eigvalues = [round(i,3) for i in L_eigvalues]
L_eigvetors = [[round(j,3) for j in L_eigvetors[i]] for i in range(len(L_eigvetors))]

# print("特征值：", L_eigvalues)
# print("特征向量：", L_eigvetors)
print("最大两个特征值及特征向量：", L_eigvalues[-1], L_eigvetors[-1], L_eigvalues[-2], L_eigvetors[-2])
print('==============')
print("最小两个特征值及特征向量：", L_eigvalues[0], L_eigvetors[0], L_eigvalues[1], L_eigvetors[1])