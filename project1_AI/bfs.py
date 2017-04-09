from queue import Queue

visit=[]

def bfs(problem1,a):
    if(a==True):
        graphsearch(problem1)
    else:
        treesearch(problem1)

#def graphsearch(problem1):
#    a=problem1.initialstate()

def treesearch(problem1):
    observe_node=0
    expand_node=0
    max_memory=0
    a = problem1.initialstate()
    q=Queue()
    q.put(a)

    while (True):
         if (q.empty()):
            print("javab nadarad")
            return
         else:
             if(max_memory<q.qsize()):
                 max_memory=q.qsize()
             b=q.get()
             expand_node+=1

             for s1 in problem1.actions(b):
                 c=problem1.result(b,s1)
                 q.put(c)
                 observe_node+=1
                 if(problem1.goal(c)==True):
                     showpath(c)
                     print("javab darad")
                     print("max_memory",max_memory)
                     print("observe_node",observe_node)
                     print("expand_node",expand_node)
                     return



def graphsearch(problem1):

    observe_node=0
    expand_node=0
    max_memory=0


    a = problem1.initialstate()
    q=Queue()
    q.put(a)
    while (True):
         if (q.empty()):
            print("javab nadarad")
            return
         else:
             if(max_memory<q.qsize()):
                 max_memory=q.qsize()


             b=q.get()
             expand_node+=1
             for s1 in problem1.actions(b):
                 c=problem1.result(b,s1)
                 if(visited(c)==False):
                    observe_node+=1
                    visit.append(c.state)
                    q.put(c)
                    print(c)

                    if(problem1.goal(c)==True):
                        showpath(c)
                        print("javab darad")
                        print("max_memory", max_memory)
                        print("observe_node", observe_node)
                        print("expand_node", expand_node)

                        return




def visited(c):
    print(visit)
    if c.state in visit:
        return True
    else:
        return False



def showpath(c):
    if(c.parrent==None):
        print(c.state)
    else:
        showpath(c.parrent)
        print(c.state)


