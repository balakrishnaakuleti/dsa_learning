from collections import deque

def add_edge(matrix,i,j):
    matrix[i][j] = 1
    matrix[j][i] = 1

def remove_edge(matrix,i,j):
    matrix[i][j] = 0
    matrix[j][i] = 0

def print_matrix(matrix):
    for row in matrix:
        print(row)

def remove_vertex(matrix,vertex):
    updated_matrix = []
    #removing row
    for i in range(0,len(matrix)):
        if vertex != i:
            updated_matrix.append(matrix[i])
    #removing column
    updated_matrix_2 = []
    for row in updated_matrix:
        updated_row = []
        for i in range(0,len(row)):
            if i !=vertex:
                updated_row.append(row[i])
        updated_matrix_2.append(updated_row)
    return updated_matrix_2

def add_vertex(matrix):
    row_to_be_added = [[0,0,0,0]]
    #Adding new column to the existing matrix
    for row in matrix:
        row.append(0)
    #Adding new row
    updated_matrix = matrix + row_to_be_added

    return updated_matrix

def search_vertex_bfs(matrix, vertex_to_search):
    queue_to_visit = deque()
    queue_to_visit.append(0)
    visited_vertices = [False for _ in range(len(matrix))]
    print(visited_vertices)
    while queue_to_visit:
        current_vertex = queue_to_visit.popleft()
        print("current vertex:",current_vertex)
        if current_vertex == vertex_to_search:
            print("item found: ",vertex_to_search)
            return
        visited_vertices[current_vertex] = True
        current_vertex_neighbours = matrix[current_vertex]
        #print(current_vertex_neighbours)
        for i in range(0,len(matrix)):
            if current_vertex_neighbours[i] == 1 and visited_vertices[i] is False and i not in queue_to_visit:
                queue_to_visit.append(i)            
    print("item not found")
    

#def search_vertex_dfs(matrix, vertex_to_search):
    

matrix = [[0,1,0,1,0],[1,0,1,0,0],[0,1,0,0,0],[1,0,0,0,1],[0,0,0,1,0]]
print("Default Graph:")
print_matrix(matrix)
#A edges
#add_edge(matrix,0,1)
#add_edge(matrix,0,2)
#add_edge(matrix,0,3)

#B edges
#add_edge(matrix,1,2)
#add_edge(matrix,1,3)
#print("Graph after adding all Edges:")
#print_matrix(matrix)

#remove edge edge A to D
#print("removing edge A to D:")
#remove_edge(matrix,0,3)
#print_matrix(matrix)

#print("Removing vertex")
#matrix=remove_vertex(matrix,3)
#print_matrix(matrix)

#print("adding vertex:")
#matrix = add_vertex(matrix)
#print_matrix(matrix)

search_vertex_bfs(matrix,4)
