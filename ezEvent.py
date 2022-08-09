from sqlalchemy import false
from ezFrame import ezFrame

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

        self.strRepr = "DICK AND BALLS"

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

        if self.eventType == "assign":
            ez1 = self.frameList[0]
            ez2 = self.frameList[1]
            
            # dictionary comprehension to get new variable name/value
            # TODO: this dictionary comprehension is still fucked up somehow, cuz it ain't working...
            newvar = { k : ez2.locs[k] for k in set(ez2.locs.keys()) - set(ez1.locs.keys()) }

            newName = list(newvar.keys())[0]
            newVal = list(newvar.values())[0]
            print("New Variable!")
            print(f"Name: {newName}")
            print(f"Value: {newVal}")

            newID = 0
            oldName = 0

            # check if new variable is pointer to old variable
            for tup in ez2.locaddrs.items():
                if tup[0] == newName:
                    newID = tup[1]
                    print(f"ID: {newID}")

            for tup in ez2.locaddrs.items():
                print(tup)
                if tup[1] == newID and tup[0] != newName:
                    isPointer = True
                    oldName = tup[0]
                    print(f"Pointer to: {oldName}")

            # create string representation from analysis
            self.strRepr = f"New variable '{newName}' was assigned value of '{newVal}'"
            if isPointer:
                self.strRepr += f" (points to '{oldName}')"

        # TODO: implement functionality beyond assignment
        '''
        elif type == "funcdef":
            return None
        elif type == "classdef":
            return None
        else: # "funccall"
            return None
        '''


    def __str__(self):
        return self.strRepr

    def __repr__(self):
        return self.strRepr

    # needed features:
    # constructor, to some limited degree
    # add(): add an ezFrame to the event (or a list of ezFrames)
    # overwrite __str__/__repr__: so that it can report the result of the event
        
