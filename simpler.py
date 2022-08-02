def run():
    class Staff601:
        course = '6.01'
        building = 34
        room = 501

        def salutation(self):
            return self.role + ' ' + self.name

    pat = Staff601()
    print(pat.course)

    pat.name = 'Pat'
    pat.age = 60
    pat.role = 'Professor'

    print(pat.building)
    pat.building = 32
    print(pat.building)

    print(pat.salutation())
    print(Staff601.salutation(pat))

'''
nice clean example of swapping between multiple frames within 1 quick program
it becomes obvious that the Class gets its own stack frame where it holds static vars,
and another separate frame is made when class functions are called.
whenever that class definition needs to be referenced, like when calling salutation,
it swaps back into that frame to quickly run the code it needs there.

in order to catch print statements, we'll have to be monitoring console output as well
I was anticipating that anyway, PyTutor uses it of course

when args refer to a specific object, we're most likely looking at a return from a method call
EX: when salutation is called, Professor Pat is the arg, passed in as 'self', 
and returned as string


- calling a function within a function
'''