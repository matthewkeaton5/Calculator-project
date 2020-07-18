#helper functions to be used in class calculator
def add(int1,int2):
    return int1 + int2
def sub(int1,int2):
    return int1 - int2
def mult(int1,int2):
    return int1 * int2
def div(int1,int2):
    return int1 / int2
def square(int1):
    return int1**2
def root(int1):
    return int1**(1/2)

class Calculator:

    solution = 0
    #initialize class
    def __init__(self):
        pass
    #functions to produce answers when imported
    def add(self,int1,int2):
        self.solution = add(int1,int2)
        return self.solution

    def sub(self,int1,int2):
        self.solution = sub(int1,int2)
        return self.solution

    def mult(self,int1,int2):
        self.solution = mult(int1,int2)
        return self.solution

    def div(self,int1,int2):
        self.solution = div(int1,int2)
        return self.solution

    def square(self,int1):
        self.solution = square(int1)
        return self.solution

    def root(self,int1):
        self.solution = root(int1)
        return self.solution
