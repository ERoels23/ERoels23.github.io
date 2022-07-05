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
it becomes obvious that the Class gets its own stack frame where it holds static vars
and function stubs (see how 'salution' is recorded).
whenever that class definition needs to be referenced, like when calling salutation,
it swaps back into that frame to quickly run the code it needs there.

in order to catch print statements, we'll have to be monitoring console output as well
I was anticipating that anyway, PyTutor uses it of course
'''