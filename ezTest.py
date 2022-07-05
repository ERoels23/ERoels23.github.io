import simplest
import sys
from ezFrame import ezFrame

ezFrames = []

def mytrace(frame, event, arg):
    ezFrames.append(ezFrame(frame, event, arg))
    return mytrace

sys.settrace(mytrace)
simplest.run()
sys.settrace(None)

for f in ezFrames:
    f.ezprint()

# pytest framework 
#     can illustrate state changes
# deepdiff and other tools can help with rich differences between objects

# differentiate between looping structures and actual function calls
# address may change if you go into a control structure

# from the spreadsheet, let's see which of these events we can extract
# then do that lmao