# Basic sys.argv -> OOP

# argv is a util of the sys lib
import sys


# Create a class object too keep code clean
class ShowArgv():
    # initiate the object
    # so that it's functions share the properties
    def __init__(self):
        pass

    # create a function to enumerate the arguments
    def get_args(self, args_):
        for i, ar_ in enumerate(args_):
            print(f"[{str(i)}]:[{str(ar_)}]")
        print(f"[number of args]:[{str(len(sys.argv))}]")


# To use an Object Callback (function)
if __name__=="__main__":
    # - You must first Initialize the Object
    SA = ShowArgv()
    if sys.argv:
        # run the callback
        SA.get_args(sys.argv)


