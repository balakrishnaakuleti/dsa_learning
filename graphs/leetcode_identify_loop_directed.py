
import sys

sys.setrecursionlimit(10**6)
#User function Template for python3
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        for i in range(V):
            if len(adj[i])>0:
                visited_array = [False for _ in range(V)]
                recStack = [False for _ in range(V)]
                if self.isCyclicUtil(i, adj, visited_array, recStack):
                    return True
        return False

    def isCyclicUtil(self, node, adj, vis, rec):
        vis[node]=True
        rec[node]=True
        for child in adj[node]:
            if not vis[child] and self.isCyclicUtil( child, adj, vis, rec):
                return True
            elif rec[child]:
                return True
        rec[node]=False

#{ 
 # Driver Code Starts
#Initial Template for Python 3
'''
5 6
2 0
1 0
3 2
4 2
3 4
3 1
'''
if __name__ == '__main__':
        N=5
        V=N
        adj_lists = [ [] for _ in range(N)]
        adj_lists[0]=[]
        adj_lists[1]=[0]
        adj_lists[2]=[0]
        adj_lists[3]=[1,2,4]
        adj_lists[4]=[2]
        ob = Solution()

        if ob.isCyclic(V, adj_lists):
            print(1)
        else:
            print(0)
        print("~")
# } Driver Code Ends