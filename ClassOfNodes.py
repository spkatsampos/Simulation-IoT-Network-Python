class node_state_class:

    
    
    def __init__(self,node_name, sleep_time, mobility_class):
        self.node_name = node_name
        self.sleep_time = sleep_time
        self.mobility_class = mobility_class
        self.node_buffer_packets=[]
        self.node_memory=[]
    
    def active_state(self,state):
        self.node_state = state
	
    def set_time_slot(self):
        self.time=100

    def add_to_buffer(self,m):
        if len(self.node_buffer_packets)<=100:
            self.node_buffer_packets.append(m)
            return 1
        else:
            return -1
        
    def add_to_memory(self,m):
        if len(self.node_memory)<50:
            self.node_memory.append(m)
            
        else:
            self.node_memory.pop(0)
            self.node_memory.append(m)
            
