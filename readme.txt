The python code of this project simulates a time-varying IoT network 
and four different methods of multi-hop communication between the nodes.

The network is self-organazied and easily deployed. It is not required fixed
infrastractures such as base stations or coordinators. 

The nodes are objects in python environment that have all the necessary information 
and characteristics such as memory, address, some functionality etc.

The available conections (links)  based  on the eucledian distance among the devices 
as well as the state of the nodes (active or inactive/sleep)

The algorithm of the communication methods: 
1: Every Node:
2: If the node is mobile then
3: Implement the mobility model
4: If the node is active then
5: Broadcast a “Hello” Message
15
6: Receive the Responses of the “Hello Messages” and store in the table of neighbours the nodes which response.
7: Reduce the life time of all the packets in your buffer
8: If you have any packets to be transmitted, then
9: Append the packet/s into your buffer following a FIFO queueing technique.
10: count = 0
11: If your buffer has packet/s for forwarding then
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
(DM model)
12: If the packet has destination any of the neighbours then
13: Send the packet to this node only
14: count = count + 1
15: else
16. Multicast the packet to all the neighbours that it has not been visited again.
17: count = count + 1
18: If count < 5 then
19: Go to step 11
---------------------------------------------------------------------------------
(MFR model)
12: If the packet has destination any of the neighbours then
13: Send the packet to this node only
14: count = count + 1
15: else
16. Choose randomly the 50% of the neighbours and multicast the packet to them.
16
17: count = count + 1
18: If count < 5 then
19: Go to step 10
---------------------------------------------------------------------------------
(MFC model)
12: If the packet has destination any of the neighbours then
13: Send the packet to this node only
14: count = count + 1
15: else
16. Choose randomly the 50% of the neighbours that the packet has not passed already and multicast the packet to them.
17: count = count + 1
18: If count < 5 then
19: Go to step 10
----------------------------------------------------------------------------------
(OMFCR model)
12: If the packet has destination any of the neighbours then
13: Send the packet to this node only
14: count = count + 1
15: else
16. Choose randomly N- nodes of the neighbours that the packet has not visited and multicast the packet to them.
17: count = count + 1
18: If count < 5 then
19: Go to step 10 

