#https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?page=1&category=Graph&sortBy=submissions

def identify_loop_in_graph(adj_lists):
    N = len(adj_lists)
    #Check cycle for all nodes one by one
    for node in range(N):
            visited_array = [False for _ in range(N)]
            if detect_cycle(node, adj_lists, visited_array):
                return True
    return False
        
def detect_cycle(node, adj_lists, vis):
    vis[node] = True
    for adj_node in adj_lists[node]:
        #Case 2: Not parent but visited already - RED FLAG
        if vis[adj_node]:
            return True
        else:
            #Case 3: f no loop check if loop exists for the child node
            if detect_cycle(adj_node, adj_lists,vis):
                return True


def print_ad_list(adj_lists):
    for adj_list in adj_lists:
        print(adj_list)

# Initialize the graph
N=5
adj_lists = [ [] for _ in range(N)]
adj_lists[0]=[]
adj_lists[1]=[2]
adj_lists[2]=[]
adj_lists[3]=[0]
adj_lists[4]=[2]

#Print Graph
print("Graph in adjacency list format")
print_ad_list(adj_lists)

#Check for loop
print("Is there a loop in the graph ?")
print(identify_loop_in_graph(adj_lists))