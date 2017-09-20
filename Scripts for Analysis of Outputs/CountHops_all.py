import csv


bftime = []
bfhops= []

mfcrtime=[]
mfcrhops=[]

mfrtime=[]
mfrhops=[]

omfcrtime=[]
omfcrhops=[]




Folders = ["BF","MFCR","MFR","OMFCR"]
for folder in Folders:
    t=[]
    nh=[]
    for p in range(0,2):
        

        c=[]
        c1 =[]

        f=open(str(folder)+"\\"+str(p)+"\\Network_LogFile.txt","r")
        f1=open("OMFCR\\"+str(p)+"\\Traffic_LogFile.txt","r")
        c = csv.reader(f, delimiter='\t', skipinitialspace=True)
        c1 = csv.reader(f1, delimiter='\t', skipinitialspace=True)

        send_message = dict()
        arrive_message = dict()
        num_hops=[]
        for i in c1:
            send_message[i[0]+i[1]+i[2]+i[3]+i[4]]=i[5] # message:timeslot
            
            
        for j in c:
            arrive_message[j[5]+j[6]+j[7]+j[8]+j[9]]=j[18]
            num_hops.append(int(j[14]))
            nh.append(int(j[14]))
        

        
        k=0
        time =[]
        for m in send_message.keys():
            if m in arrive_message.keys():
                #print(m)
                if int(arrive_message[m])-int(send_message[m])>=0:
                    time.append(int(arrive_message[m])-int(send_message[m]))
                    t.append(int(arrive_message[m])-int(send_message[m]))
                    #print(m,"arrived after: ",int(arrive_message[m])-int(send_message[m]))
                    
            else:
                k=k+1


        #print("i lost : ",k," packets out of :",len(send_message))
        
        
     
        ########################################################################3
        '''
        fm = open(str(folder)+'_HopsStatistics.txt','a+')
        fm.write("--------------"+str(p)+"--------------------\n")
        fm.write("Average number of timeslots:  "+str(np.average(time))+"\nMax:  "+str(max(time))+"\nThe 80% of packets arrived before: "+str(time[int(len(arrive_message)*0.8)])+" \n")
        fm.write("Average number of hops: "+str( np.average(num_hops))+"\nMax number of steps: "+str(max(num_hops))+"\n")
        fm.close()
        '''
        del c
        del c1
        del send_message
        del arrive_message

    f.close()
    f1.close()
    ####################
    if folder =="BF":
        bftime = t
        bfhops= nh
    if folder == "MFCR":
        mfcrtime=t
        mfcrhops=nh
    if folder=="MFR":
        mfrtime=t
        mfrhops=nh
    if folder =="OMFCR":
        omfcrtime=t
        omfcrhops=nh
    
############################################3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerLine2D
time1, bin_edges = np.histogram(bftime, bins=max(bftime), normed=True)
cdf1 = np.cumsum(time1)

time2, bin_edges = np.histogram(mfcrtime, bins=max(mfcrtime), normed=True)
cdf2 = np.cumsum(time2)

time3, bin_edges = np.histogram(mfrtime, bins=max(mfrtime), normed=True)
cdf3 = np.cumsum(time3)

time4, bin_edges = np.histogram(omfcrtime, bins=max(omfcrtime), normed=True)
cdf4 = np.cumsum(time4)

line1,=plt.plot(cdf1,c="red",label="DM")
line2,=plt.plot(cdf2,c="blue",label="MFCR")
line3,=plt.plot(cdf3,c="green",label="MFR")
line4,=plt.plot(cdf4,c="black",label="OMFCR")
plt.grid()
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.title("CDF-Number of Time-Slots")
plt.xlabel("Time (in time slots)")
plt.ylabel("Probability")
plt.show()


hop1, bin_edges = np.histogram(bfhops, bins=max(bftime), normed=True)
cdf11 = np.cumsum(time1)

hop2, bin_edges = np.histogram(mfcrhops, bins=max(mfcrtime), normed=True)
cdf22 = np.cumsum(time2)

hop3, bin_edges = np.histogram(mfrhops, bins=max(mfrtime), normed=True)
cdf33 = np.cumsum(time3)

hop4, bin_edges = np.histogram(omfcrhops, bins=max(omfcrtime), normed=True)
cdf44 = np.cumsum(time4)


line1,=plt.plot(cdf11,c="red",label="DM")
line2,=plt.plot(cdf22,c="blue",label="MFCR")
line3,=plt.plot(cdf33,c="green",label="MFR")
line4,=plt.plot(cdf44,c="black",label="OMFCR")
plt.grid()
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.title("CDF - Number of Hops")
plt.xlabel("Hops - (Number of nodes)")
plt.ylabel("Probability")
plt.show()


