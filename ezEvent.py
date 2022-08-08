from sqlalchemy import false
import ezFrame

class ezEvent:
    frameList = []          #to hold our series of ezFrames
    eventType = "Default"   #assignment, class def, etc.
    types = ["assign","funcdef","classdef","funccall"]
    strRepr = ""
    '''
    assign: (poss: pointer)
    funcdef: (poss: class method)
    classdef: 
    funccall: (poss: instantiate, method, )  
    '''

    # assignment
    # definition (class or function, but might look similar)
    # function call
    # 

    def __init__(self, type):
        '''
        only requires type of object before definition, adding frames comes later
        '''
        if type in self.types:
            self.eventType = type
        else:
            raise TypeError("valid event types: assign, funcdef, classdef, funccall")

    def add(self, f):
        '''
        only expected to be called once, it does calc once added, so use wisely!
        '''
        isPointer = False

        # generic setup, collect ezFrames/Events in one place
        if isinstance(f, ezFrame) or isinstance(f, ezEvent):
            # might append ezEvent to an ezEvent 
            # (ex: func def within class def, constructor call within assignment, etc.)
            self.frameList.append(f)
        elif isinstance(f, list):
            self.frameList += f
        else:
            raise TypeError("ezEvent 'add()' requires ezFrame or list of ezFrames")

        if type == "assign":
            ez1 = self.frameList[0]
            ez2 = self.frameList[1]
            
            # dictionary comprehension to get new variable name/value
            newvar = { k : ez2.locs[k] for k in set(ez2.locs) - set(ez1.locs) }
            newName = newvar.keys[0]
            newVal = newvar.values[0]

            newID = 0
            oldName = 0

            # check if new variable is pointer to old variable
            for key, value in ez2.locaddrs:
                if key == newName:
                    newid = value

            for key, value in ez2.locaddrs:
                if value == newid and key != newName:
                    isPointer = True
                    oldName = key

            # create string representation from analysis
            self.strRepr = f"New variable {newName} was assigned value of {newVal}"
            if isPointer:
                self.strRepr += f" (pointer to {oldName})"

        # TODO: implement functionality beyond assignment
        elif type == "funcdef":
            return None
        elif type == "classdef":
            return None
        else: # "funccall"
            return None


    def __str__(self):
        return "pass the boof"

            
    # needed features:
    # constructor, to some limited degree
    # add(): add an ezFrame to the event (or a list of ezFrames)
    # overwrite __str__/__repr__: so that it can report the result of the event
        
