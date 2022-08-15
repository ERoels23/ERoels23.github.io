import debugging
import simplest
import simpler
import sys
from ezFrame import ezFrame
from ezEvent import ezEvent
import inspect as ins
from pprint import pprint as pp

ezFrames = []

# may also need to change to Mac syntax if on Mac
currFile = "c:\\Users\\Eric\\Desktop\\NOTIONS\\ERoels23.github.io\\simplest.py"

# tracing function
def mytrace(frame, event, arg):
    # currently excludes calls to built-in functions. 
    if (frame.f_code.co_filename == currFile or frame.f_back.f_code.co_filename == currFile):
        ez = ezFrame(frame, event, arg)
        ezFrames.append(ez)

    return mytrace

# ensure that custom trace function is being used
sys.settrace(mytrace)

# run the sample python program, tracing as we go
simplest.run()

# pop out the first and last, because it's just call/return for run() in the target file, not useful
""" 
ezFrames.pop(0)
ezFrames.pop(-1) 
"""
# ugh okay actually these are kinda useful, because we occassionally need the previous or next frame
# in order to fully define an assignment or function call

for f in ezFrames:
    f.ezPrint()

# event creation and frame allocation is currently done manually
# each frame must be given an event type (ie. "assign", "funccall", "funcdef", "classdef")
event1 = ezEvent("assign")
event2 = ezEvent("assign")
event3 = ezEvent("assign")
event4 = ezEvent("assign")
event1.add([ezFrames[1], ezFrames[2]])
event2.add([ezFrames[2], ezFrames[3]])
event3.add([ezFrames[3], ezFrames[4]])
event4.add([ezFrames[4], ezFrames[5]])

# uses the __repr__ of ezEvent to print Event descriptions
print("\nRESULTS: ")
print(str(event1))
print(str(event2))
print(str(event3))
print(str(event4))

print("\nTRACE RESULTS:")
print("Successfully Traced.")
print(f"{len(ezFrames)} frames found.")