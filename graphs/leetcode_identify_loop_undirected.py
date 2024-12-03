from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        N = V
        visited_array = [False for _ in range(N)]
        #Check cycle for all nodes one by one
        for node in range(N):
            if visited_array[node] == False:
                if self.detect_cycle(node, -1, adj, visited_array):
                    return True
        return False
    
    def detect_cycle(self, node, parent, adj_lists, vis):
        vis[node] = True
        for adj_node in adj_lists[node]:
            #Case 1: It is parent - Nothing to do
            if adj_node == parent:
                continue
            #Case 2: Not parent but visited already - RED FLAG
            elif vis[adj_node]:
                return True
            else:
                #Case 3: f no loop check if loop exists for the child node
                if self.detect_cycle(adj_node, node, adj_lists, vis):
                    return True

#{ 
 # Driver Code Starts
if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")
        print("~")

# } Driver Code Ends