#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        traversed_array = []
        N = len(adj)
        visited_vertices = [False for _ in range(N)]
        to_be_visited_stack = []
        to_be_visited_stack.append(0)
        while to_be_visited_stack:
            current_vertex = to_be_visited_stack.pop()
            if not visited_vertices[current_vertex]:
                visited_vertices[current_vertex] = True
                traversed_array.append(current_vertex)
                for adjacent_node in reversed(adj[current_vertex]):
                    if not visited_vertices[adjacent_node]:
                        to_be_visited_stack.append(adjacent_node)
                print(to_be_visited_stack)
        return traversed_array

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

    # Create an object of Solution class
    ob = Solution()
    ans = ob.dfsOfGraph(adj)

    print(ans)
    print("~")
# } Driver Code Ends