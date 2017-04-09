import abc
class problem:

    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def initialstate(self):
        #return initial state
        return


    @abc.abstractmethod
    def actions(self,node1):
        #return all actions
        return

    @abc.abstractmethod
    def result(self,node1,action):
        #return  state that earns from this state by this action
        return


    @abc.abstractmethod
    def goal(self,node1):
        #return  state that earns from this state by this action
        return




    @abc.abstractmethod
    def heuristic(self,node1):
        #return  state that earns from this state by this action
        return



    @abc.abstractmethod
    def goalstate(self):
        #return  state that earns from this state by this action
        return














