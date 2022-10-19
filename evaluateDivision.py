import collections

def calcEquation(equations, values, queries):
    G = collections.defaultdict(dict)
    for (x, y), v in zip(equations, values):
        G[x][y] = v
        G[y][x] = 1/v

    def bfs(src, dst):
        # neither x not y exists
        if (not (src in G and dst in G)):
            return -1.0

        queue = [(src, 1.0)]
        seen = set()
        for x, v in queue:

            # src points to dst
            if x == dst:
                print(v) 
                return v

            seen.add(x)

            # maybe src is connected to dst through other nodes
            # use dfs to see if there is a path from src to dst
            for y in G[x]:
                if y not in seen: 
                    queue.append((y, v*G[x][y])); 
                    print(x,y,v,G[x][y],"product: ",v*G[x][y])
            else:
                print("exited")
        return -1.0
    return [bfs(s, d) for s, d in queries]

print(calcEquation([["a","b"],["b","c"]],[2.0,3.0], [["a","c"]]))
