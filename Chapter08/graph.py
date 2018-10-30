graph = dict() 
graph['A'] = ['B', 'C'] 
graph['B'] = ['E','C', 'A'] 
graph['C'] = ['A', 'B', 'E','F'] 
graph['E'] = ['B', 'C'] 
graph['F'] = ['C']

matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)  

adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)] 

edges_list = [] 


for key in matrix_elements: 
    for neighbor in graph[key]: 
       edges_list.append((key,neighbor)) 


print(edges_list)



for edge in edges_list: 
        index_of_first_vertex = matrix_elements.index(edge[0]) 
        index_of_second_vertex = matrix_elements.index(edge[1]) 
        adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1 


println(adjacency_matrix)
