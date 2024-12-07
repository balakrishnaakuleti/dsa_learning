#User function Template for python3

class Solution:
    
    def print_adj(self,adj):
        for adj_list in adj:
            print(adj_list)
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        traversed_array = []
        N = len(adj)
        visited_vertices = [False for _ in range(N)]
        to_be_visited_stack = []
        to_be_visited_stack.append(0)
        print(" Intial Stack: ", to_be_visited_stack)
        while to_be_visited_stack:
            current_vertex = to_be_visited_stack.pop()
            print("Processing node : ", current_vertex)
            if not visited_vertices[current_vertex]:
                visited_vertices[current_vertex] = True
                traversed_array.append(current_vertex)
                print("Considering not visited children in reverse order for the stack - ",reversed(adj[current_vertex]))
                for adjacent_node in reversed(adj[current_vertex]):
                    if not visited_vertices[adjacent_node] and adjacent_node not in to_be_visited_stack:
                        to_be_visited_stack.append(adjacent_node)
                print(" Updated stack : ",to_be_visited_stack)
                print("Traversed elements as of now: ",traversed_array)
        return traversed_array

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

    # Create an object of Solution class
    ob = Solution()
    ob.print_adj(adj)
    ans = ob.dfsOfGraph(adj)

    print(ans)
    print("~")
# } Driver Code Ends