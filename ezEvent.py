from ezFrame import ezFrame

class ezEvent:
    types = ["assign","funcdef","classdef","funccall"]

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
        self.frameList = []
        self.strRepr = ""
        self.eventType = type

        if type in self.types:
            self.eventType = type
        else:
            raise TypeError("valid event types: assign, funcdef, classdef, funccall")

        self.strRepr = "Default String"

    def add(self, f):
        '''
        only expected to be called once, it does calc once added, so use wisely!
        '''
        isPointer = False

        # generic setup, collect ezFrames/Events in one place
        try:
            if isinstance(f, ezFrame) or isinstance(f, ezEvent):
                # might append ezEvent to an ezEvent 
                # (ex: func def within class def, constructor call within assignment, etc.)
                self.frameList.append(f)
            elif isinstance(f, list):
                self.frameList += f
        except:
            raise TypeError("ezEvent 'add()' requires ezFrame or list of ezFrames")


        if self.eventType == "assign":
            ez1 = self.frameList[0]
            ez2 = self.frameList[1]
            
            # dictionary comprehension to get new variable name/value
            newvar = { k : ez2.locs[k] for k in set(ez2.locs) - set(ez1.locs) }

            newName = list(newvar.keys())[0]
            newVal = list(newvar.values())[0]

            newID = 0
            oldName = 0

            # check if new variable is pointer to old variable
            for tup in ez2.locaddrs.items():
                if tup[0] == newName:
                    newID = tup[1]

            for tup in ez2.locaddrs.items():
                if tup[1] == newID and tup[0] != newName:
                    isPointer = True
                    oldName = tup[0]

            # create string representation from analysis
            self.strRepr = f"New variable '{newName}' was assigned value of '{newVal}'"
            if isPointer:
                self.strRepr += f" (points to '{oldName}')"
        
        elif type == "funcdef":
            # new stack pointer, call type, curfunc for name
            # need: function name, argument names, return value name (if applicable)
            ez1 = self.frameList[0]
            ez2 = self.frameList[1]

            # format: line with almost no info, 
            # then line no. skips >1, another line with funcName as a local variable

            # obtain name of new function, it's recorded as a new local variable
            newFunc = { k : ez2.locs[k] for k in set(ez2.locs) - set(ez1.locs) }
            funcName = list(newFunc.keys())[0]

            self.strRepr = f"New custom function '{funcName}()' defined"

        elif type == "funccall":
            # this is where it starts to get pretty tricky
            # 
            return None
        
        '''
        else: # "classdef"
            return None
        '''


    def __str__(self):
        return self.strRepr

    def __repr__(self):
        return self.strRepr
