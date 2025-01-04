def search_graph(adj_list):
    n = len(adj_list)
    visited_nodes = [False for _ in range(0,n)]
    stack = []
    stack.append(0)
    while stack:
        current_node = stack.pop()
        print(current_node)
        if visited_nodes[current_node] == True:
            print("loop found at ", current_node)
            return
        visited_nodes[current_node] = True
        for i in adj_list[current_node]:
            if visited_nodes[current_node] == True:
                print("loop found")
                print(current_node)
                return
            print('no loop found')


adj_list= [[1], [0,2,4], [1,3], [2,4], [1,3]]
search_graph(adj_list) 
 