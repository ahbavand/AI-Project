

visit=[]
o_node=0
e_node=0



def dfs(problem1,version,depth):
     graphsearch_without_depth(problem1)
    #treesearch_incremental_search(problem1)
  #  graphsearch_without_depth(problem1)
   #  treesearch_by_depth(problem1,depth)
#    graphsearch_by_depth(problem1,5)
  #  graphsearch_incremental_search(problem1)







def treesearch_by_depth(problem1,dl):

    observe_node=0
    expand_node=0
    max_memory=0
    global e_node
    global o_node

    a = problem1.initialstate()
    stak=[]
    stak.append(a)
    while (True):
        if(len(stak)==0):
            print("javab nadarad")
            return False
        else:
            if (max_memory < len(stak)):
                max_memory =len(stak)

            b=stak.pop()

            if(b.get_depth()<dl):
                expand_node += 1

                for s1 in problem1.actions(b):
                    c = problem1.result(b, s1)
                    stak.append(c)
                    observe_node += 1

                    if (problem1.goal(c) == True):
                        print("javab darad")
                        showpath(c)
                        print("max_memory", max_memory)
                        print("observe_node", observe_node)
                        print("expand_node", expand_node)
                        e_node=e_node+expand_node
                        o_node=o_node+observe_node
                        return True






def treesearch_by_depth1(problem1,dl):

    observe_node=0
    expand_node=0
    max_memory=0
    global e_node
    global o_node

    a = problem1.initialstate()
    stak=[]
    stak.append(a)
    while (True):
        if(len(stak)==0):
            print("javab nadarad")
            return False
        else:
            if (max_memory < len(stak)):
                max_memory =len(stak)

            b=stak.pop()

            if(b.get_depth()<dl):
                expand_node += 1
                e_node+=1

                for s1 in problem1.actions(b):
                    c = problem1.result(b, s1)
                    stak.append(c)
                    observe_node += 1
                    o_node+=1

                    if (problem1.goal(c) == True):
                        print("javab darad")
                        showpath(c)
                        print("max_memory", max_memory)
                        print("observe_node", o_node)
                        print("expand_node", e_node)
                        print()
                        return True



def treesearch_without_depth(problem1):

    a = problem1.initialstate()
    stak=[]
    stak.append(a)
    while (True):
        if(len(stak)==0):
            print("javab nadarad")
            return
        else:
            b=stak.pop()
            for s1 in problem1.actions(b):
                c = problem1.result(b, s1)
                stak.append(c)

                if (problem1.goal(c) == True):
                    print("javab darad")
                    showpath(c)

                    return




def treesearch_incremental_search(problem1):
    for i in range(0,100000):
        if(treesearch_by_depth1(problem1,i)==True):
            break








def graphsearch_without_depth(problem1):
    observe_node=0
    expand_node=0
    max_memory=0



    a = problem1.initialstate()
    stak=[]
    stak.append(a)
    while (True):
        if(len(stak)==0):
            print("javab nadarad")
            return
        else:
            if (max_memory < len(stak)):
                max_memory = len(stak)

            b=stak.pop()
            expand_node+=1
            for s1 in problem1.actions(b):
                c = problem1.result(b, s1)
                if (visited(c) == False):
                    observe_node+=1
                    stak.append(c)
                    visit.append(c.state)
                    if (problem1.goal(c) == True):
                        showpath(c)
                        print("javab darad")
                        print("max_memory", max_memory)
                        print("observe_node", observe_node)
                        print("expand_node", expand_node)
                        return



def visited(c):
    if c.state in visit:
        return True
    else:
        return False






def showpath(c):
    li=[]
    while(True):
        if (c.parrent == None):
            print(c.state)
            while(len(li)!=0):
                q=li.pop()
                print(q.state)
            break

        else:
            li.append(c)
            c=c.parrent


"""

def graphsearch_incremental_search(problem1):
    for i in range(5,8):

        if(graphsearch_by_depth(problem1,i)==True):
            break



def graphsearch_by_depth(problem1,dl):
    a = problem1.initialstate()
    stak=[]
    stak.append(a)
    while (True):
        if(len(stak)==0):
            print("javab nadarad")
            return False
        else:
            b=stak.pop()
            print(len(stak),"yes")
            if(b.get_depth()<dl):
                for s1 in problem1.actions(b):
                    c = problem1.result(b, s1)
                    if (visited(c) == False):
                        stak.append(c)
                        visit.append(c.state)
                        if (problem1.goal(c) == True):
                            print("javab darad")
                            showpath(c)
                            return True


"""

