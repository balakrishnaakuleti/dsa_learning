
from collections import deque
from typing import List

#User function Template for python3
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        # code here
        traversed_array =[]
        N = len(adj)
        visited_vertices = [False for _ in range(N)]
        to_be_visted_vertices = deque()
        to_be_visted_vertices.append(0)
        while to_be_visted_vertices:
            current_vertex = to_be_visted_vertices.popleft()
            traversed_array.append(current_vertex)
            visited_vertices[current_vertex] = True
            for adjacent_node in adj[current_vertex]:
                if not visited_vertices[adjacent_node] and adjacent_node not in to_be_visted_vertices:
                    to_be_visted_vertices.append(adjacent_node)
        return traversed_array


#{ 
 # Driver Code Starts
if __name__ == '__main__':

    adj = [[2,3,1], [0], [0,4], [0],[2]]
    ob = Solution()
    ans = ob.bfsOfGraph(adj)
    print(ans)
    print(" ".join(map(str, ans)))  # Print the BFS traversal result

# } Driver Code Ends