from collections import deque
class Graph:
    def topo_sort_dfs(self, node, visited_array, adjacency_list, stack):
        visited_array[node] = 1
        neighbours = adjacency_list[node]

        for current_node in neighbours:
            if visited_array[current_node] != 1:
                self.topo_sort_dfs(current_node, visited_array, adjacency_list, stack)
        
        stack.append(node)
        return

    def topo_sort_driver(self, V, adj_list):
        visited_array = [0] * (V+1)
        stack = deque()

        for node in range(V):
            if visited_array[node] != 1:
                self.topo_sort_dfs(node, visited_array, adjacency_list, stack)
        output = list(stack)
        return output[::-1]

