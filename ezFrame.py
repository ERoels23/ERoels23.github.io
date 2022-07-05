from copy import deepcopy

class ezFrame:
    address = None
    line = None
    eType = None
    caller = None
    current = None
    file = None
    locs = []
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
        # not sure yet how to isolate the address...
        self.address = hex(id(frame))
        print(frame.f_locals)
        self.locs = deepcopy(frame.f_locals)
        self.args = arg
        self.file = frame.f_code.co_filename

    def ezprint(self):
        if (self.file == "/Users/Eric/NOTIONS/ERoels23.github.io/simplest.py"):
            print("ezFrame Print:")
            print(f"ADDRESS: {self.address}")
            print(f"LINE NO: {self.line}")
            print(f"TYPE   : {self.eType}")
            print(f"CURFUNC: {self.current}")
            print(f"PARENT : {self.caller}")
            print(f"ARGS   : {self.args}")
            print(f"FILE   : {self.file}")
            print(f"LOCALS :")
            print(self.locs)

    def __repr__(self):
        # new toString() method here!
        None