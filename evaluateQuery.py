

def addEdge(graph,from_,to,val):
    if from_ in graph:
        graph[from_].append((to,val)) 
    else:
        graph[from_] = [(to,val)]

def getGraph(facts):
    graph = {}

    for (from_,to,val) in facts:
        #Add to and from the each unit
        addEdge(graph, from_, to, val)
        addEdge(graph, to, from_, 1/val)

    return graph

def evaluateQuery(facts,from_,to,n=1):
    graph = getGraph(facts)

    if not (from_ or to in graph):
        return None

    queue = [(from_,n)]
    seen = set()

    while(len(queue) > 0):
        curr_unit, curr_running_val = queue.pop()
        if curr_unit == to:
            return curr_running_val

        seen.add(curr_unit)
        for neighbour,val in graph[curr_unit]:
            queue.append((neighbour,curr_running_val * val))
            seen.add(neighbour)
    return None


print(evaluateQuery([["hr","min",60],["min","sec",60]],"hr","sec"))
