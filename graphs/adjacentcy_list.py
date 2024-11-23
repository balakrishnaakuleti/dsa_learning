from collections import deque

def add_edge(adj_list,i,j):
    adj_list[i].append(j)
    adj_list[j].append(i)

def remove_edge(adj_list,u,v):
    for i in range(len(adj_list[u])):
     if (adj_list[u][i] == v):
        adj_list[u].pop(i)
        break

    for i in range(len(adj_list[v])):
     
        if (adj_list[v][i] == u):
             
            adj_list[v].pop(i)
            break

def add_vertex(adj_list):
    vertex = []
    adj_list.append(vertex)
    return adj_list

def remove_vertex(adj_list: list,vertex):
    for row in adj_list:
        if vertex in row:
            row.remove(vertex)
    
    updated_list = []
    for i in range(0,len(adj_list)):
        if vertex != i:
            updated_list.append(adj_list[i])

            
    return updated_list


def print_list(adj_list):
    for row in adj_list:
        print(row)

def search_vertex_bfs(adj_list, vertex_to_search):
    queue_to_visit = deque()
    queue_to_visit.append(0)
    visited_nodes = [False for _ in range(len(adj_list))]
    while queue_to_visit:
        current_vertex = queue_to_visit.popleft()
        visited_nodes[current_vertex] = True
        print("current vertex: ",current_vertex)
        if vertex_to_search == current_vertex:
            print("Item found ",current_vertex)
            return
        if len(adj_list[current_vertex]) > 0:
            for vertex in adj_list[current_vertex]:
                if visited_nodes[vertex] is False and vertex not in queue_to_visit:
                    queue_to_visit.append(vertex)
    print("item not found")
    return


def search_vertex_dfs(adj_list, vertex_to_search):
    n = len(adj_list)
    visited_nodes = [False for _ in range(0,n)]
    to_visited_stack = []
    to_visited_stack.append(0)
    while to_visited_stack:
        currrent_vertex = to_visited_stack.pop()
        visited_nodes[currrent_vertex] = True
        print("Current vertex: ",currrent_vertex)
        if vertex_to_search == currrent_vertex:
            print("item found: ",currrent_vertex)
            return
        if len(adj_list[currrent_vertex]) > 0:
            for vertex in adj_list[currrent_vertex]:
                if visited_nodes[vertex] is False and vertex not in to_visited_stack:
                    to_visited_stack.append(vertex)
    print("item not found")
    return


adj_list = [[] for _ in range(4)]

print_list(adj_list)
print("adding edges")
add_edge(adj_list,0,1)
add_edge(adj_list,0,2)
add_edge(adj_list,0,3)
add_edge(adj_list,1,2)
add_edge(adj_list,1,3)
add_edge(adj_list,2,3)

print_list(adj_list)

print("removing edges 2-3")
remove_edge(adj_list,2,3)
print_list(adj_list)

print("adding vertex")
adj_list = add_vertex(adj_list)
print_list(adj_list)

print("removing vertex")
#adj_list = remove_vertex(adj_list,1)
print_list(adj_list)

search_vertex_bfs(adj_list, 4)
search_vertex_dfs(adj_list, 0)