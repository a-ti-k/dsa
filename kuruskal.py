parent = dict()
rank = dict()
def make_set(vertice):
    parent[vertice]=vertice
    rank[vertice]=0
def find (vertice):
    if(parent[vertice] != vertice):
        parent[vertice]=find(parent[vertice])
    return parent[vertice]
def union (vertice1,vertice2):
    root1=find(vertice1)
    root2=find(vertice2)
    if root1 != root2:
        if(rank[root1]> rank[root2]):
            parent[root2]=root1
        else:
            parent[root1]=root2
    if rank[root1]==rank[root2]:
        rank[root2]+=1

def kruskal(graph):
    for vertice in graph['vertices']:
            make_set(vertice)
            minimum_spanning_tree = set()
            edges = list(graph['edges'])
            edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if (find(vertice1) != find(vertice2)):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return sorted(minimum_spanning_tree)

graph = {
        'vertices': ['0','1','2','3','4','5','6'],
        'edges': set([
                    (25, '0', '1'),
                    (25, '1' ,'0'),
                    (12, '1', '6'),
                    (12, '6', '1'),
                    (14, '1', '2'),
                    (14, '2', '1'),
                    (11, '2', '3'),
                    (11, '3', '2'),
                    (17, '6', '3'),
                    (17, '3', '6'),
                    (22, '6', '4'),
                    (22, '4', '6'),
                    (20, '3', '4'),
                    (20, '4', '3'),
                    (23, '4', '5'),
                    (23, '5', '4'),
                    (10, '0', '5'),
                    (10, '5', '0'),
                ])
            }
#find shortest path and show display
print("Shortest path from graph: ",kruskal(graph))
