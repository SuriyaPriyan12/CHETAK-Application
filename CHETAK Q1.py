# CHETAK question 1 program to implement traveling salesman  
from sys import maxsize 
from itertools import permutations

#size of the matrix 
v = 5 

#starting point
s=0

def tsp(matrix, s): 
 
    # the path of salesman
    list = [] 
    for i in range(v): 
        if i != s: 
            list.append(i) 
 
    # stores the minimum weight of the permutated paths 
    min_cost = maxsize 
    permutation=permutations(list)
    for i in permutation:
 
        current_cost = 0
        current_route = [s]
 
        # compute current path and cost
        k = s 
        for j in i: 
            current_cost += matrix[k][j] 
            k = j
            current_route.append(k)
        current_cost+= matrix[k][s]
        
 
        # update min
        if current_cost < min_cost:
            min_cost = current_cost
            
            # best path for min_cost 
            best_route = current_route

    return min_cost, best_route

   
 
 
# matrix representation of graph
# atributes represents cost
matrix = [[0, 10, 15, 20, 18],
         [10, 0, 35, 25, 20], 
         [15, 35, 0, 30, 15], 
         [20, 25, 30, 0, 20],
         [20, 25, 15, 10, 0]] 
print(tsp(matrix, s))

    
      