import numpy as np
from problem import problem
import bfs
import dfs
import uniform_cost
from  node import node
import a_star


class p1(problem):
    def __init__(self):
        self.a = np.zeros(shape=(20, 20))
        self.goal_state = 17
        self.a[0][1]=71
        self.a[1][0]=71
        self.a[0][3]=151
        self.a[3][0]=151

        self.a[1][2]=75
        self.a[2][1]=75

        self.a[2][3]=140
        self.a[3][2]=140

        self.a[2][4]=118
        self.a[4][2]=118

        self.a[3][12]=80
        self.a[12][3]=80

        self.a[3][11]=99
        self.a[11][3]=99

        self.a[4][5]=111
        self.a[5][4]=111

        self.a[5][6]=70
        self.a[6][5]=70

        self.a[6][7]=75
        self.a[7][6]=75

        self.a[7][8]=120
        self.a[8][7]=120

        self.a[8][9]=138
        self.a[9][8]=138

        self.a[8][12]=146
        self.a[12][8]=146

        self.a[9][12]=97
        self.a[12][9]=97

        self.a[9][10]=101
        self.a[10][9]=101

        self.a[10][11]=211
        self.a[11][10]=211

        self.a[10][14]=85
        self.a[14][10]=85

        self.a[10][13]=90
        self.a[13][10]=90

        self.a[14][15]=98
        self.a[15][14]=98

        self.a[14][17]=142
        self.a[17][14]=142

        self.a[15][16]=86
        self.a[16][15]=86

        self.a[17][18]=92
        self.a[18][17]=92

        self.a[18][19]=87
        self.a[19][18]=87


        self.point=[]
        self.point.append([131,571])
        self.point.append([108,531])
        self.point.append([91,142])
        self.point.append([207,457])
        self.point.append([94,410])
        self.point.append([165,379])
        self.point.append([168,339])
        self.point.append([165,299])
        self.point.append([253,288])
        self.point.append([320,368])
        self.point.append([400,327])
        self.point.append([305,449])
        self.point.append([233,410])
        self.point.append([375,270])
        self.point.append([456,350])
        self.point.append([534,350])
        self.point.append([562,293])
        self.point.append([509,444])
        self.point.append([473,506])
        self.point.append([406,537])





    def initialstate(self):
        y=node(2,None,0)
        return y


    def actions(self,node1):
        lis_soh_ser=[]
        for co in range(0,20):
            if(self.a[node1.state][co]>0):
                lis_soh_ser.append(co)
        return lis_soh_ser

    def result(self,node1,action):
        y=node(action,node1,self.a[node1.state][action])
        return y



    def goal(self,node1):
        if(node1.state==self.goal_state):
            return True
        else:
            return False




    def heuristic(self,node1):
        return ((self.point[node1.state][0]-self.point[17][0])**2+(self.point[node1.state][1]-self.point[17][1])**2)**(0.5)





x=p1()
#bfs.bfs(x,False)
#dfs.dfs(x,1,8)
uniform_cost.uniform_cost(x)
#a_star.a_star(x)

