import debugging
import simplest
import sys
from pprint import pprint as pp

def mytrace(frame, event, arg):
    print(f"FRAME {frame.f_code}")
    print(f"EVENT {event}")
    print(f"ARGS {arg}")
    print(f"    inside function \" {frame.f_code.co_name} \" on line {frame.f_lineno}")
    print(f"    called by {frame.f_back.f_code.co_name}")
    print(f"    locals: {frame.f_locals}")
    #pp(f"    globals: {frame.f_globals}")
    print()
    return mytrace

sys.settrace(mytrace)

# debugging.run()
simplest.run()

# im thinking we're gunna need to write a "diff" style function
# because looking at a single frame object can't tell us much
# unless, of course, we can compare locals between frames, etc.