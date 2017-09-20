def Graph(n):

    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.random_geometric_graph(n,0.15,2)
    pos = nx.get_node_attributes(G,'pos')
    nx.write_gml(G,"network50_3.gml")

Graph(100)
