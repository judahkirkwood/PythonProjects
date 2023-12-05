

import dunder


def print_dunder2():
    name = (__name__)
    return name

if __name__ == "__main__":
    #The following is calling code from within this script
    print("I am running code from {}".format(print_dunder2()))

    #The following is calling code from the imported app.py
    print("I am running code from {}".format(dunder.print_dunder()))

    
