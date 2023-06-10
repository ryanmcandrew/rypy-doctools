
Prims minimal spanning tree
===========================
1. First, make sure you have Python version 3.10 installed on your computer. You can download it from the official Python website.

2. Import the necessary modules: 

```python
from typing import Tuple, List
from heapq import heappush, heappop
```

3. Define a function that takes the graph as an input and returns the minimum spanning tree.

```python
def prim_mst(graph: List[List[Tuple[int]]]) -> List[Tuple[int, int]]:
    
    # Initialize MST, heap and visited vertices
    mst = []
    heap = []
    visited = set()
    
    # Start with vertex 0
    start_vertex = 0
    
    # Add the edges from the starting vertex to the heap
    for edge in graph[start_vertex]:
        heappush(heap, (edge[1], start_vertex, edge[0]))
    
    # Add the starting vertex to visited
    visited.add(start_vertex)
    
    # Loop until the heap is empty
    while heap:
        
        # Pop the smallest edge from the heap
        weight, vertex1, vertex2 = heappop(heap)
        
        # If vertex2 has already been visited, skip this edge
        if vertex2 in visited:
            continue
        
        # Add the edge to the MST and mark vertex2 as visited
        mst.append((vertex1, vertex2))
        visited.add(vertex2)
        
        # Add all edges from vertex2 to the heap, except for the ones that connect back to already visited vertices
        for edge in graph[vertex2]:
            if edge[0] not in visited:
                heappush(heap, (edge[1], vertex2, edge[0]))
    
    return mst
```

4. To test the function, create a graph as a list of adjacency lists.

```python
graph = [
    [(1, 4), (7, 8)],
    [(0, 4), (2, 8), (7, 11)],
    [(1, 8), (3, 7), (5, 4), (8, 2)],
    [(2, 7), (4, 9), (5, 14)],
    [(3, 9), (5, 10)],
    [(2, 4), (3, 14), (4, 10), (6, 2)],
    [(5, 2), (7, 1), (8, 6)],
    [(0, 8), (1, 11), (6, 1), (8, 7)],
    [(2, 2), (6, 6), (7, 7)]
]
```

5. Call the `prim_mst` function with the graph as an argument.

```python
mst = prim_mst(graph)
print(mst)
```

This should print out the minimum spanning tree as a list of edges.