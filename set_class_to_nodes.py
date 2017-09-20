class set_class_to_nodes:

        import networkx as nx

        #################################
        def choose_random_mobility_class():
                from random import randint
                p = randint(0, 100)
            
                if p < 10:
                        c = 'mobile'
                else:
                        c = 'stable'
                return c
        #################################
        def choose_random_sleep_time():
                import random 
                sleep_time = [1,2,3,4]
                sleep = random.choice(sleep_time)
                return sleep

        #################################
        def set_nodes_specifications(G):
            from ClassOfNodes import node_state_class   
            node_specifications = list();
            
            for i in G.nodes():

                mobility_class = set_class_to_nodes.choose_random_mobility_class()

                sleep_time = set_class_to_nodes.choose_random_sleep_time()
                #  #  #  # 
                x = node_state_class(i,sleep_time,mobility_class)
                node_specifications.append(x)

            return node_specifications
        ##################################
            

