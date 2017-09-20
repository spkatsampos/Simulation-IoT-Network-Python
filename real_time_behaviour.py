class real_time_behaviour:
    
    #The "current_graph_state" take an object ClassOf Nodes
    #and disable the edges between this node and its neighbors.
    #Also, enable the edges when a node wakes up.



    def current_graph_state(G):
        import networkx as nx
	import settings
	
        R = 0.15
        pos = nx.get_node_attributes(G,'pos')
        ########################################################
        
        for i in range(0,len(settings.nodesList)):
            if settings.nodesList[i].node_state == 0:
                neighbors = G.neighbors(settings.nodesList[i].node_name)
                #print("neighbors of :",i,"-->",neighbors)
                for j in range(0,len(neighbors)):
                    G.remove_edge(settings.nodesList[i].node_name,neighbors[j])
                    #print("the ",i,"-->",neighbors[j],"removed")
            else:               
                #if not G.neighbors(nodeslist[i].node_name):
                    for e in range(0,len(settings.nodesList)):
                        #eucledian distance between pairs
                        if settings.nodesList[e].node_state == 1:
                            eucledian_distance = ((pos[settings.nodesList[e].node_name][0]-pos[settings.nodesList[i].node_name][0])**2)+ ((pos[settings.nodesList[e].node_name][1]-pos[settings.nodesList[i].node_name][1])**2)
                            if eucledian_distance <= R**2:
                                 G.add_edge(settings.nodesList[e].node_name, settings.nodesList[i].node_name)

        return G





























    ##########################################################
    def find_neighbors(G,nodeslist,n,R):
        import networkx as nx
        pos = nx.get_node_attributes(G,'pos')
        for e in range(0,len(nodeslist)):
                        #eucledian distance between pairs
                        if nodeslist[e].node_state == 1:
                            eucledian_distance = ((pos[nodeslist[e].node_name][0]-pos[nodeslist[n].node_name][0])**2)+ ((pos[nodeslist[e].node_name][1]-pos[nodeslist[n].node_name][1])**2)
                                                    
                            if eucledian_distance <= R**2:
                                 G.add_edge(nodeslist[e].node_name, nodeslist[n].node_name)
 
                
        return G        
 
    #############################################################
