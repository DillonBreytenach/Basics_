# Basic sys.argv

import sys

# Create callback to iterate through the arguments,
# given when running the program
def get_args(args_):
    for i, ar_ in enumerate(args_):
        print(f"[{str(i)}]:[{str(ar_)}]")
    print(f"[number of args]:[{str(i)}]")


# check if python3 has received any arguments
if sys.argv:
    get_args(sys.argv)

# In the case that you run the code.. 
# it will be True, since the file name is argv[0]
