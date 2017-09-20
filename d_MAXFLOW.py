'''
Input:
G: the time-varying graph;
(s; d): the source-destination pair;
δ: the degree of temporal disjointness;
Output:
J1... Jm: a set δ-disjoint journeys.
1: Initialize m = 0;
2: Compute the Line Graph of G;
3: if s and d is disconnected in the Line Graph then
4: Go to step 10;
5: end if
6: m   m + 1;
7: In the Line Graph, find an s - d path Pm that passes the least
number of nodes (the corresponding journey is denoted by Jm);
8: Remove all the interfering contacts of Jm from G;
9: Go to step 2;
10: END.
'''
import networkx as nx
import copy

def maxflow(G, s, d,timeslot):
###############################################################
    Graph = copy.deepcopy(G[0])
    edges = Graph.edges()
    #print(edges)
    for e in edges:
        Graph.add_edge(e[0], e[1], weight=1)
        #print("---",int(Graph.get_edge_data(e[0],e[1])["weight"])+1 )
    for i in range(timeslot, timeslot+50):
        edges = Graph.edges()
        ed = G[i].edges()
        for k in iter(edges):
            for l in iter(ed):
                if k == l:
                    Graph[l[0]][l[1]]['weight']=(int(Graph.get_edge_data(l[0],l[1])["weight"])+1)
                    ed.remove(l)
        #print("ed",ed)        
        for e in ed:
            Graph.add_edge(e[0], e[1], weight=1)

#################################################################
    m = 0
    stop = 0    
    J = []
    
    while stop == 0:
        if not nx.has_path(Graph,s,d):
            #print("\n There not exists a path between source:",s," and destination: ",d," After removing:",m," paths.\n")
            stop = 1
        else:
            
            m = m + 1
            path = nx.shortest_path(Graph, source=s, target=d)
            J.append(path)
            Graph.remove_edges_from(J)
    #print("All the paths are:",J) 

    for a in J:
        for b in J:
            if a!=b:
                for i in range(0,len(a)-1):
                    for j in range(0,len(b)-1):
                        if a[i]==b[j] and a[i+1] == b[j+1]:
                            if b in J:
                                J.remove(b)
                            
                
        
        
    #all_simple_paths(G, source, target, cutoff=None)
    return J

