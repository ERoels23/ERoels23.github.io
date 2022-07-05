import debugging
import simplest
import sys
from ezFrame import ezFrame
import inspect as ins
from pprint import pprint as pp

ezFrames = []

def mytrace(frame, event, arg):
    # this filename might be restricting too much, hard to see calls to built-in funcs
    if frame.f_code.co_filename == "c:\\Users\\Eric\\Desktop\\NOTIONS\\ERoels23.github.io\\simplest.py":
        print("Found a frame!")
        ez = ezFrame(frame, event, arg)
        ezFrames.append(ez)


    '''
        print("\nNEW FRAME COMIN IN HOT")
        print(f"FRAME {frame.f_code}")
        print(f"EVENT {event}")
        print(f"ARGS {arg}")
        print(f"    inside function \" {frame.f_code.co_name} \" on line {frame.f_lineno}")
        print(f"    called by {frame.f_back.f_code.co_name}")
        print(f"    locals: {frame.f_locals}")
        #pp(f"    globals: {frame.f_globals}")
        print("TEe.names: {code.co_names}")
        print(f"f_code.stacksize: {code.co_stacksize}")
        print(f"f_code.varnames: {code.co_varnames}")
        # f_code.co_{insert here}
            # argcount, code, cellvars, consts,
            # filename, firstlineno, flags, lnotab,
            # freevars, posonlyargcount, kwonlyargcount,
            # name, names, nlocals, stacksize, varnames

        print(f"frame.f_back: {frame.f_back}")
        print(f"frame.f_code: {frame.f_code}")

        code = frame.f_code
        print(f"f_code.consts: {code.co_consts}")
        print(f"f_code.name: {code.co_name}")
        print(f"f_cod
        print(f"frame.f_lineno: {frame.f_lineno}")
        print(f"frame.f_locals: {frame.f_locals}")
    '''
    return mytrace

sys.settrace(mytrace)

simplest.run()

for f in ezFrames:
    f.ezPrint()

