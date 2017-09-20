class Packets:    
    
    def __init__(self,source, destination, msg, seq_number):
        self.source = source
        self.destination = destination
        self.msg = msg
        self.LifeTime = 100
        self.seq_number = seq_number        
        self.node_list=[]

    def next_nodes(self,n):
        self.nextnode = n
        
    def previous_node(self,n):
        self.previousnode = n
        
    def add_node(self,node):
        self.node_list.append(node)
	
    def set_timestamp(self, time):
        self.timestamp=time
        
            

    def __eq__(self, other):
        if self.source == other.source and self.destination == other.destination and self.seq_number == other.seq_number:
            return True
        else:
            return False
