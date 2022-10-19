# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
# find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i 
# (i.e., there is a directed edge from node i to node graph[i][j]).

from calendar import c


class Solution:
    # O(E+V) Time Complexity
    # V = number of verticies/nodes 
    # E = max number of edges a node has
    def allPathsSourceTarget(graph):
        target = len(graph) - 1
        allPaths = []

        def dfs(nodeNum,path):
            if nodeNum == target:
                allPaths.append(list(path + [nodeNum]))
                return
            else:
                for neighbour in graph[nodeNum]:
                    dfs(neighbour, path+[nodeNum])
        dfs(0,[])            

        return allPaths

    def allPathsSourceTarget2(graph):
        target = len(graph) - 1
        
        def dfs(node, path, allPaths):
            if node is target:
                allPaths.append(path)
                return
                    
            for neighbour in graph[node]:
                dfs(neighbour,path + [neighbour], allPaths)
                
        allPaths = []
        dfs(0,[0],allPaths)
        return allPaths

    def allPathsSourceTarget3(graph):
        target = len(graph) - 1
        stack = [(0,[0])]
        allPaths = []
        while(stack):
            curr,route = stack.pop()

            if curr == target:
                allPaths.append(route)
            else:
                for neighbour in graph[curr]:
                    # print(neighbour, graph[curr])
                    # print(neighbour, route , route + [neighbour])
                    stack.append((neighbour, route + [neighbour]))
        return allPaths

    print(allPathsSourceTarget([[1,2],[3],[3],[]]))

