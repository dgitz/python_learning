# Notes
def sayHello(name): # Define a function, with the argument 'name'
    >>> print('Hello, ' + name)
sayHello('Al') # Call the function, by passing 'Al' 

# Call Stack
- When your program calls a function, Python creates a 'frame object' on the top of the 'call stack'
- When a function call returns, Pyhton removes a 'frame object' from the top of the 'call stack' and moves the execution to theline number stores in it.
- Frame objects are always added/removed from the top of the stack and not from any other place.

 # Scope
 - Parameters/Variables that are assigned in a called function are in a function's 'local scope'.
 - Parameters/Variables that are assigned outside all functions are said to exist in the 'global scope'.