from  problem import problem
import numpy as np
from  node import node
import bfs
import dfs
import uniform_cost
import a_star
import bidirectional

class p2(problem):

    def __init__(self):

        self.b=np.zeros(shape=(3,3))
        self.a=self.b.tolist()
        self.a[0][0]=1
        self.a[0][1]=2
        self.a[0][2]=3
        self.a[1][0]=0
        self.a[1][1]=4
        self.a[1][2]=5
        self.a[2][0]=6
        self.a[2][1]=7
        self.a[2][2]=8




    def initialstate(self):
        y=node(self.a,None,1)
        return y




    def actions(self,node1):   #0=up   1=down 2=right   3=left
        lis_soh_ser=[]

        if(node1.state[0][0]!=0 and node1.state[0][1]!=0 and node1.state[0][2]!=0):
            lis_soh_ser.append(0)


        if(node1.state[2][0]!=0 and node1.state[2][1]!=0 and node1.state[2][2]!=0):
            lis_soh_ser.append(1)



        if(node1.state[0][2]!=0 and node1.state[1][2]!=0 and node1.state[2][2]!=0):
            lis_soh_ser.append(2)


        if(node1.state[0][0]!=0 and node1.state[1][0]!=0 and node1.state[2][0]!=0):
            lis_soh_ser.append(3)


        return lis_soh_ser




    def result(self,node1,action):
        il=np.zeros(shape=(3,3))
        li=il.tolist()
        for i in range(0,3):
            for j in range(0,3):
                li[i][j]=node1.state[i][j]
        for i0 in range(0,3):
            for j0 in range(0,3):
                if(node1.state[i0][j0]==0):
                    i=i0
                    j=j0

        if(action==0):
            li[i][j]=li[i-1][j]
            li[i-1][j]=0

        elif(action==1):
            li[i][j]=li[i+1][j]
            li[i+1][j]=0

        elif(action==2):
            li[i][j]=li[i][j+1]
            li[i][j+1]=0

        elif(action==3):
            li[i][j]=li[i][j-1]
            li[i][j-1]=0

        y=node(li,node1,1)
        return y



    def goal(self,node1):
        if(node1.state[0][0]==0 and node1.state[0][1]==1 and node1.state[0][2]==2 and node1.state[1][0]==3 and node1.state[1][1]==4 and node1.state[1][2]==5 and node1.state[2][0]==6 and node1.state[2][1]==7 and node1.state[2][2]==8  ):
            return True
        else:
            return False



    def heuristic(self,node1):
        hu=0
        for k in range(0,9):
            for i in range(0,3):
                for j in range(0,3):
                    if(self.a[i][j]==k):
                        hu=hu+abs((i-int(k/3)))+abs((j-(k%3)))
        return hu


    def goalstate(self):

        r=np.zeros(shape=(3,3))
        t=r.tolist()
        t[0][0]=0
        t[0][1]=1
        t[0][2]=2
        t[1][0]=3
        t[1][1]=4
        t[1][2]=5
        t[2][0]=6
        t[2][1]=7
        t[2][2]=8


        y=node(t,None,1)
        return y


x=p2()

#dfs.dfs(x,1,2)
#bfs.bfs(x,False)
#uniform_cost.uniform_cost(x)
#a_star.a_star(x)
bidirectional.tree_saerch(x)
