class ezFrame:
    address = ""
    line = -1
    eType = ""
    caller = ""
    current = ""
    locals = []
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

    def __init__(self, f):
        # requires a live frame object in order to instantiate
        return None
