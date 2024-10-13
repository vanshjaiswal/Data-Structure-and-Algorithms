from collections import deque
class Graph:
    def adjacency_list(self, n, edges):
        adj_list={}
        for i in range(n+1):
            adj_list[i] = []

        for (i,j) in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        return adj_list

    def cycle_bfs(self, node, adj_list, visited_arr):
        # adj_list = self.adjacency_list(n, edges)
        q = deque()
        # visited_arr = [0] * (n+1)

        q.append((node, -1))
        visited_arr[node] = 1

        while q:
            print(q)
            node, parent = q.popleft()
            neighbours = adj_list[node]

            for connected_node in neighbours:
                if connected_node == parent:
                    continue
                if visited_arr[connected_node] != 1 :
                    q.append((connected_node, node))
                    visited_arr[connected_node] = 1
                else:
                    return True

        return False

    def bfs_cycle_undirected(self, node, adj_list, visited_arr):
        
        q=deque()
        q.append((node, -1))
        visited_arr[node] = 1

        while q:
            current_node, parent = q.popleft()

            neighbours = adj_list[current_node]

            for n_cur in neighbours:
                if n_cur == parent:
                    continue
                if visited_arr[n_cur] != 1:
                    q.append((n_cur, current_node))
                    visited_arr[n_cur] == 1   
                else:
                    return True

        return False



    def bfs_cycle_undirected_driver(self, n, edges):
        adj_list = self.adjacency_list(n, edges)
        visited_arr = [0] * (n+1)

        for i in range(1, n+1):
            if visited_arr[i] != 1:
                if self.cycle_bfs(i, adj_list, visited_arr):
                    return True
                
        return False



edges = [(1,2), (1,3), (2,5), (6,7), (3,4)]
n=7

sol = Graph()

print(sol.bfs_cycle_undirected_driver(n, edges))


                


