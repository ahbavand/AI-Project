from queue import Queue


def tree_saerch(problem1):




    observe_node=0
    expand_node=0
    max_memory=0


    visit1=[]
    visit2=[]
    q1=Queue()
    q2=Queue()

    a = problem1.initialstate()
    b=problem1.goalstate()
    q1.put(a)
    q2.put(b)
    visit1.append(a.state)
    visit2.append(b.state)
    while (True):
         if (q1.empty() or q2.empty()):
            print("javab nadarad")
            return

         else:

              if (max_memory < q1.qsize() + q2.qsize()):
                 max_memory = q1.qsize() + q2.qsize()

              b1=q1.get()
              b2=q2.get()
              expand_node=expand_node+2


              for s1 in problem1.actions(b1):
                   c1=problem1.result(b1,s1)
                   q1.put(c1)
                   observe_node+=1
                   if(c1.state not in visit1):
                       visit1.append(c1.state)


                   if(c1.state in visit2):
                       print("javab darad")
                       print("max_memory", max_memory)
                       print("observe_node", observe_node)
                       print("expand_node", expand_node)

                       showpath1(c1)
                       while(True):
                           c2=q2.get()
                           if(c2.state==c1.state):
                               showpath2(c2)
                               return

                       return

         for s2 in problem1.actions(b2):
             c2 = problem1.result(b2, s2)
             q2.put(c2)
             observe_node+=1
             if (c2.state not in visit2):
                 visit2.append(c2.state)

             if (c2.state in visit1):
                 print("javab darad")
                 print("max_memory", max_memory)
                 print("observe_node", observe_node)
                 print("expand_node", expand_node)


                 while (True):
                     c1 = q1.get()
                     if (c1.state == c2.state):
                         showpath2(c1)
                         return

                 showpath2(c2)

                 return












def showpath1(c1):
    if(c1.parrent==None):
        print(c1.state)
    else:
        showpath1(c1.parrent)
        print(c1.state)



def showpath2(c2):
    if(c2.parrent==None):
        print(c2.state)
    else:
        print(c2.state)
        showpath2(c2.parrent)



