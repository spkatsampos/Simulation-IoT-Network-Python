import csv

for p in range(0,5):
    

    c=[]
    c1 =[]

    f=open(str(p)+"\\Network_LogFile.txt","r")
    f1=open(str(p)+"\\Traffic_LogFile.txt","r")
    c = csv.reader(f, delimiter='\t', skipinitialspace=True)
    c1 = csv.reader(f1, delimiter='\t', skipinitialspace=True)

    send_message = dict()
    arrive_message = dict()
    num_hops=[]
    for i in c1:
        send_message[i[0]+i[1]+i[2]+i[3]+i[4]+i[6]]=i[5] # message:timeslot
        
        
    for j in c:
        arrive_message[j[5]+j[6]+j[7]+j[8]+j[9]+j[23]]=j[18]
        num_hops.append(int(j[14]))
    

    print(send_message)
    k=0
    time =[]
    for m in send_message.keys():
        if m in arrive_message.keys():
            time.append(int(arrive_message[m])-int(send_message[m]))
            print(m,"arrived after: ",int(arrive_message[m])-int(send_message[m]))
            
        else:
            k=k+1


    print("i lost : ",k," packets out of :",len(send_message))

    import numpy as np
 
    ########################################################################3
    fm = open('HopsStatistics.txt','a+')
    fm.write("--------------"+str(p)+"--------------------\n")
    fm.write("Average number of timeslots:  "+str(np.average(time))+"\nMax:  "+str(max(time))+"\nThe 80% of packets arrived before: "+str(time[int(len(arrive_message)*0.8)])+" \n")
    fm.write("Average number of hops: "+str( np.average(num_hops))+"\nMax number of steps: "+str(max(num_hops))+"\n")
    fm.close()
    del c
    del c1
    del send_message
    del arrive_message

f.close()
f1.close()
