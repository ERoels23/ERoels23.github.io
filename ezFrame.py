from copy import deepcopy
import ast
import ujson

class ezFrame:
    address = None
    line = None
    eType = None
    caller = None
    current = None
    file = None
    locs = []
    locaddrs = []
    args = []

    # what does my frame need?
        # Address on Stack
            # string? really only need it for comps
        # Line No.
        # Event Type (line, return, call, etc.)
            # enum?
        # Caller Function
        # Current Function
        # Local Variables
        # Local Arguments (?)
    
    # maybe?
        # Filename
            # PythonTutor, for example, does not support >1 file at a time
                # as far as I'm aware... hmmm...

    def __init__(self, frame, event, arg):
        # requires a live frame object in order to instantiate
        self.line = frame.f_lineno
        self.caller = frame.f_back
        self.eType = event
        self.current = frame.f_code.co_name
        
        self.address = hex(id(frame))

        # attempting to skirt the deepcopy TypeError
        self.locs = ujson.dumps(frame.f_locals)
        self.locs = ujson.loads(self.locs)
        # seems like that's working... for now

        # we also need to record the addresses of each variable, to find pointers
        self.locaddrs = { {k, id(k)} for k in self.locs.keys }
        
        self.args = arg
        self.file = frame.f_code.co_filename


    def ezPrint(self):
        ret = "PROGRAM SNAPSHOT:\n"
        ret += f"ADDRESS: {self.address}\n"
        ret += f"LINE NO: {self.line}\n"
        ret += f"TYPE   : {self.eType}\n"
        ret += f"CURFUNC: {self.current}\n"
        ret += f"PARENT : {self.caller}\n"
        ret += f"ARGS   : {self.args}\n"
        ret += f"FILE   : {self.file}\n"
        ret += f"LOCALS : {str(self.locs)}\n"
        print(ret)

    # next up!
    '''
    we'll write a function that compares two adjacent stack frames
    it will attempt to deduce what happened between the reporting of those 2 frames
    
    '''
        