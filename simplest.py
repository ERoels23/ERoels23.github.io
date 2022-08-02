from re import A


def run():
    class myObj:
        myVar = 0
        def __init__(self):
            myVar = 17
            return self
        def speak(self):
            print(self.myVar)
    myInstance = myObj()
    myInstance.speak()
          
# check for-loops and other structures    
# this simple program right here produced a total of 5 file-local frames
'''
1. call   (line 1), parent function calls the run() function within this file
2. line   (line 2), x gets instantiated, not in locals for this frame yet
3. line   (line 3), 1 gets appended to x, x = [] now reported in locals
4. line   (line 4), prints out x (weird that this is a line, not a call to a function)
5. return (line 4), returns from the run() function back to caller file
'''

