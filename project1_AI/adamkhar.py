from  problem import problem
import numpy as np
from  node import node
import bfs
import dfs


class p3(problem):

    def __init__(self):
        self.a=np.zeros(shape=(5))
        self.a[0]=3
        self.a[1]=3
        self.a[2]=0
        self.a[3]=0
        self.a[4]=0




    def initialstate(self):
        y=node(self.a,None,1)
        return y

    def actions(self,node1):   #0= 1a 1m   1=2a 2=2m   3=1a  4=1m
        lis_soh_ser=[]
        if(node1.state[0]==3 and node1.state[1]==3 and node1.state[4]==0):
            lis_soh_ser.append(0)
            lis_soh_ser.append(1)
        elif(node1.state[0]==2 and node1.state[1]==3 and node1.state[4]==0):
            lis_soh_ser.append(1)
            lis_soh_ser.append(3)
            lis_soh_ser.append(4)
        elif(node1.state[0]==1 and node1.state[1]==3 and node1.state[4]==0):
            lis_soh_ser.append(2)
            lis_soh_ser.append(3)
        elif(node1.state[0]==2 and node1.state[1]==2 and node1.state[4]==0):
            lis_soh_ser.append(0)
            lis_soh_ser.append(2)
        elif(node1.state[0]==1 and node1.state[1]==1 and node1.state[4]==0):
            lis_soh_ser.append(0)
            lis_soh_ser.append(4)
        elif(node1.state[0]==2 and node1.state[1]==0 and node1.state[4]==0):
            lis_soh_ser.append(1)
            lis_soh_ser.append(3)
        elif(node1.state[0]==3 and node1.state[1]==0 and node1.state[4]==0):
            lis_soh_ser.append(1)
            lis_soh_ser.append(3)
        elif(node1.state[0]==1 and node1.state[1]==0 and node1.state[4]==0):
            lis_soh_ser.append(3)
        elif(node1.state[2]==3 and node1.state[3]==3 and node1.state[4]==1):
            lis_soh_ser.append(0)
            lis_soh_ser.append(1)
        elif(node1.state[2]==2 and node1.state[3]==3 and node1.state[4]==1):
            lis_soh_ser.append(1)
            lis_soh_ser.append(3)
            lis_soh_ser.append(4)
        elif(node1.state[2]==1 and node1.state[3]==3 and node1.state[4]==1):
            lis_soh_ser.append(2)
            lis_soh_ser.append(3)
        elif(node1.state[2]==2 and node1.state[3]==2 and node1.state[4]==1):
            lis_soh_ser.append(0)
            lis_soh_ser.append(2)
        elif(node1.state[2]==1 and node1.state[3]==1 and node1.state[4]==1):
            lis_soh_ser.append(0)
            lis_soh_ser.append(4)
        elif(node1.state[2]==2 and node1.state[3]==0 and node1.state[4]==1):
            lis_soh_ser.append(1)
            lis_soh_ser.append(3)
        elif(node1.state[2]==3 and node1.state[3]==0 and node1.state[4]==1):
            lis_soh_ser.append(1)
            lis_soh_ser.append(3)
        elif(node1.state[2]==1 and node1.state[3]==0 and node1.state[4]==1):
            lis_soh_ser.append(3)


        return lis_soh_ser



    def result(self,node1,action):

        li=np.zeros(shape=(5))
        if(action==0 and node1.state[4]==0):
            li[0]=node1.state[0]-1
            li[1]=node1.state[1]-1
            li[2]=node1.state[2]+1
            li[3]=node1.state[3]+1
            li[4]=1
        elif(action==1 and node1.state[4]==0):
            li[0]=node1.state[0]-2
            li[1]=node1.state[1]
            li[2]=node1.state[2]+2
            li[3]=node1.state[3]
            li[4]=1
        elif(action==2 and node1.state[4]==0):
            li[0]=node1.state[0]
            li[1]=node1.state[1]-2
            li[2]=node1.state[2]
            li[3]=node1.state[3]+2
            li[4]=1

        elif(action==3 and node1.state[4]==0):
            li[0]=node1.state[0]-1
            li[1]=node1.state[1]
            li[2]=node1.state[2]+1
            li[3]=node1.state[3]
            li[4]=1
        elif(action==4 and node1.state[4]==0):
            li[0]=node1.state[0]
            li[1]=node1.state[1]-1
            li[2]=node1.state[2]
            li[3]=node1.state[3]+1
            li[4]=1
        elif (action == 0 and node1.state[4] ==1):
            li[0] = node1.state[0] + 1
            li[1] = node1.state[1] + 1
            li[2] = node1.state[2] - 1
            li[3] = node1.state[3] - 1
            li[4]=0
        elif (action == 1 and node1.state[4] ==1):
            li[0] = node1.state[0] + 2
            li[1] = node1.state[1]
            li[2] = node1.state[2] - 2
            li[3] = node1.state[3]
            li[4]=0
        elif (action == 2 and node1.state[4] ==1):
            li[0] = node1.state[0]
            li[1] = node1.state[1] + 2
            li[2] = node1.state[2]
            li[3] = node1.state[3] - 2
            li[4]=0
        elif (action == 3 and node1.state[4] ==1):
            li[0] = node1.state[0] + 1
            li[1] = node1.state[1]
            li[2] = node1.state[2] - 1
            li[3] = node1.state[3]
            li[4]=0
        elif (action == 4 and node1.state[4] ==1):
            li[0] = node1.state[0]
            li[1] = node1.state[1] + 1
            li[2] = node1.state[2]
            li[3] = node1.state[3] - 1
            li[4]=0
        y=node(li,node1,1)
        return y



    def goal(self,node1):
        if(node1.state[0]==0 and node1.state[1]==0 and node1.state[2]==3 and node1.state[3]==3 and node1.state[4]==1):
            return True
        else:
            return False






x=p3()

#bfs.bfs(x,False)

dfs.dfs(x,1,2)






