
# Creating protected class
class Protected:
    def __init__(self):
        self._protectedVar = 0 

obj = Protected() # Creating a protected object
obj._protectedVar = 57 # Assigning the protected object a value
print(obj._protectedVar)


class Protected: # Creating a private class
    def __init__(self): # Defining a private variable, this one as a string
        self.__PrivateVar = "WHAT UP WORLD?!?"

    def getPrivate(self): 
        print(self.__PrivateVar)

    def setPrivate(self, private):
        self.__PrivateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()

