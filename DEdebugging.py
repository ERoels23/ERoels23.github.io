import debugging
import simplest
import sys
from ezFrame import ezFrame
import inspect as ins
from pprint import pprint as pp

allFrames = []
ezFrames = []

def diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1)) 

def mytrace(frame, event, arg):
    allFrames.append(frame)
    ez = ezFrame(frame, event, arg)
    ezFrames.append(ez)
    print("\nNEW FRAME COMIN IN HOT")
    print(f"FRAME {frame.f_code}")
    print(f"EVENT {event}")
    print(f"ARGS {arg}")
    print(f"    inside function \" {frame.f_code.co_name} \" on line {frame.f_lineno}")
    print(f"    called by {frame.f_back.f_code.co_name}")
    print(f"    locals: {frame.f_locals}")
    #pp(f"    globals: {frame.f_globals}")
    print("TESTINGGGGGGGGGGGGGGG")
    print(f"frame.f_back: {frame.f_back}")
    print(f"frame.f_code: {frame.f_code}")

    code = frame.f_code
    print(f"f_code.consts: {code.co_consts}")
    print(f"f_code.name: {code.co_name}")
    print(f"f_code.names: {code.co_names}")
    print(f"f_code.stacksize: {code.co_stacksize}")
    print(f"f_code.varnames: {code.co_varnames}")
    # f_code.co_{insert here}
        # argcount, code, cellvars, consts,
        # filename, firstlineno, flags, lnotab,
        # freevars, posonlyargcount, kwonlyargcount,
        # name, names, nlocals, stacksize, varnames

    print(f"frame.f_lineno: {frame.f_lineno}")
    print(f"frame.f_locals: {frame.f_locals}")

    return mytrace

sys.settrace(mytrace)

# debugging.run()
simplest.run()

newLocals = []
''' 
for i in range(len(allFrames)):
    if i != 0:
        # print("\nFRAME INFO:")
        # print(ins.getframeinfo(allFrames[i]))
        l1 = list(allFrames[i].f_locals.items())
        print(l1)
        l2 = list(allFrames[i-1].f_locals.items())
        print(l2)
        if l1 != l2:
            newLocals.append(diff(l1, l2))
'''
# for some reason this is just giving me the same locals dict every time...
# it's always saving just the one frame? Idk...
# I think it's because the frame object is a little wonky sometimes

# print(newLocals)
# print(allFrames[0].f_locals.items())
# print(type(allFrames[0]))

# im thinking we're gunna need to write a "diff" style function
# because looking at a single frame object can't tell us much
# unless, of course, we can compare locals between frames, etc.

# but perhaps we should start out by defining our own custom frame object
# because the one we're dealing with is kinda ass (or im just a dumby)

for f in ezFrames:
    f.ezprint()