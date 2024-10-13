#Adjacency matrix

import numpy as np
def adjacency_matrix(n, m, edges):
    #undirected grah
    adj_mat = np.zeros(shape = (n+1, n+1))

    for (i,j) in edges:
        adj_mat[i][j] = 1
        adj_mat[j][i] = 1 #In directed this line will be removed 

    return adj_mat

#undirected
def adjacency_list(n, m, edges):
    adj_list = {}
    for i in range(n+1):
        adj_list[i] = []
    
    for (i,j) in edges:
        adj_list[i].append(j)
        adj_list[j].append(i)

    return adj_list

#directed
def adjacency_list_directed(n, m, edges):
    adj_list = {}
    for i in range(n+1):
        adj_list[i] = []
    
    for (i,j) in edges:
        adj_list[i].append(j)
        
    return adj_list

def adjacency_matrix_weighted(n,m,edges):
    adj_mat = np.zeros(shape=(n+1, n+1))
    #for undirected
    for (i, j, wt) in edges:
        adj_mat[i][j] = wt
        adj_mat[j][i] = wt
    return adj_mat

def adjacency_list_weighted(n,m,edges):
    adj_list = {}

    for i in range(n+1):
        adj_list[i] = []

    for (i,j,wt) in edges:
        adj_list[i].append((j, wt))
    return adj_list



n=5
m=6
# edges= [(1,2), (1,3), (2,4), (3,4), (3,5), (4,5)]

# print(adjacency_matrix(n, m, edges))
# print(adjacency_list(n, m, edges))

weighted_edges = [(1,2,2), (1,3,3), (2,4,1), (3,4,4), (3,5,2), (4,5,1)]
print(adjacency_matrix_weighted(n, m, weighted_edges))
print(adjacency_list_weighted(n, m, weighted_edges))
