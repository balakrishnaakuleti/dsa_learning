from collections import deque


class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        # Code here
        N = len(adj)
        topological_order_list=[]
        degree=[0 for _ in range(N)]
        for adj_list in adj:
            for item in adj_list:
                degree[item]+=1
        print(degree)
        queue = deque()
        for i in range(N):
            if degree[i] == 0:
                queue.append(i)  
        print(queue)
        while queue:
            current_element = queue.popleft()
            topological_order_list.append(current_element)

            for child in adj[current_element]:
                degree[child] -=1
                if degree[child] == 0:
                    queue.append(child)

        if len(topological_order_list) == len(adj):
            return topological_order_list
            
                

            
        return topological_order_list
if __name__ == '__main__':
    adj = [[],[0],[0,1],[4],[0,5],[2],[0],[5],[],[8]]
    ob = Solution()

    res = ob.topologicalSort(adj)

    print("~", res)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends