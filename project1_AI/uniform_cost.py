from node import node
import queue

def uniform_cost(problem1):
    observe_node=0
    expand_node=0
    max_memory=0


    t=0



    visited =[]
    a = problem1.initialstate()
    q=queue.PriorityQueue()
    q.put((0,t,a))
    t=+1
    while(True):
        if(q.empty()):
            print("javab nadarad")
            return
        else:
            if (max_memory < q.qsize()):
                max_memory = q.qsize()


            cost,w,node1=q.get()
            expand_node+=1

            if(node1.state not in visited):
                visited.append(node1.state)
                if(problem1.goal(node1)==True):
                    print("javab darad")
                    showpath(node1)
                    print("cost",cost)
                    print("max_memory", max_memory)
                    print("observe_node", observe_node)
                    print("expand_node", expand_node)
                    return
                for s1 in problem1.actions(node1):
                    c = problem1.result(node1, s1)
                    if(c.state not in visited):
                        observe_node+=1
                        tc=cost+c.cost

                        q.put((tc,t,c))
                        t+=1






def showpath(c):
    if(c.parrent==None):
        print(c.state)
    else:
        showpath(c.parrent)
        print(c.state)
