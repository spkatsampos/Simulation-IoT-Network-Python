
import networkx as nx
import copy     

def mincutd(G,s,d, timeslot):
    
    Graph = copy.deepcopy(G[0])
    edges = Graph.edges()
    #print(edges)
    for e in edges:
        Graph.add_edge(e[0], e[1], weight=1)
        #print("---",int(Graph.get_edge_data(e[0],e[1])["weight"])+1 )
    for i in range(timeslot,timeslot+50):
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
        
########################################################################################################3
    #Here I have the graph with the weights
    #So, I have to calculate the  smallest set of contacts/edges with the smallest sum of weight
    #whose removal will disconnect the source from the destination


    #FIND A SET OF CONDUCTS S* WITH THE SMALLEST SUM OF WEIGHT WHOSE REMOVAL CAUSE DISJOITNESS S-D
    
    
    flag =0
    count=0
    S=[]
    while flag == 0:
        di=dict()
        for g in Graph.edges():
            di[g]=Graph[g[0]][g[1]]['weight']
            
        #print("\n\n",Graph.edges(data=True))
        a=min(di, key=lambda k: di[k])
           
        Graph.remove_edge(int(a[0]),int(a[1]))
        S.append(a)
        del di[a]
        #print("+++removed: ",a)
        
        count = count+1
        del di
        
        
        if not nx.has_path(Graph,s,d):
            flag = 1
        
        print("count: ",count)
    #FIND ALL AVAILABLE PATHS
    return S,count
   
