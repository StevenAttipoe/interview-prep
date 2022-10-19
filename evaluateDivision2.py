
class Solution:
    def addEdge(graph,from_, to, val):
        if from_ in graph:
            graph[from_].append((to, val))
        else:
            graph[from_] = [(to, val)]
            
    def createGraph(equations, values): 
        graph = {}
        
        for (from_,to), val in zip(equations,values):
            Solution.addEdge(graph, from_, to, val)
            Solution.addEdge(graph, to, from_, 1/val)
        return graph
    
    def calcEquation(equations , values, queries):
        graph = Solution.createGraph(equations, values)
        
        results = []
        
        for from_,to in queries:
            if not (from_ in graph) or not (to in graph):
                results.append(-1)
                continue

            if from_ == to:
                results.append(1)
                continue
                
            seen = set()    
            toVisit = [(from_,1)]
            
            while(len(toVisit) > 0):
                curr_unit, curr_val = toVisit.pop(0)
                
                if curr_unit is to:
                    results.append(curr_val)
                    break

                for neighbour,val in graph[curr_unit]:
                    if not (neighbour in seen):
                        toVisit.append((neighbour,curr_val * val))
                        seen.add(neighbour)
            else:
                results.append(-1.0)
        return results
                
print(Solution.calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    
                    
        
        
        