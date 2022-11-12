import numpy as np
import math
import random
import time

#def updatestate():
    #return true if the number is collapsed
    #return False

def split(a,b):
    """Return the split complex number j."""
    return nonentangled(a,b)  
    
def jroot(a):
    #make a number become a split complex number
    return nonentangled(0,math.sqrt(a))

globalpointers = [] 

class nonentangled:
    """A SplitComplexNumber object class. Has a real and imaginary part."""
    def __init__(self, real = .5, imag = .5):
        """Set the real and imaginary parts of the complex number."""
        self.real = real
        self.imag = imag
        #self.update()
        
    #def update():
        #"""Update the state of the complex number."""
        #updatestate()

    def collapse(self, index):
        """Return the collapse form of the complex numbers."""
        if index == 1:
            return float(self.real + self.imag)
        elif index == -1:
            return float(self.real - self.imag)
        else:
            print("Error: Can only collapse to 1 or -1.")

    
    def conjugate(self):
        """Return the conjugate of the complex number."""
        return nonentangled(self.real, -self.imag)
    
    def __str__(self):
        """Return a string representation of the complex number."""
        if self.real == 0:
            if self.imag == 0:
                return "(0)"
            else:
                if self.imag == 1:
                    return "(j)"
                elif self.imag == -1:
                    return "(-j)" 
                else:
                    return "(" + str(self.imag) + "j)"
        else:
            if self.imag < 0:
                if self.imag == -1:
                    return "(" + str(self.real) + "-j" + ")"
                else:
                    return "(" + str(self.real) + str(self.imag) + "j" + ")"
            elif self.imag > 0:
                if self.imag == 1:
                    return "(" + str(self.real) + "+j" + ")"
                else:
                    return "(" + str(self.real) + "+" + str(self.imag) + "j" + ")"
            else:
                return "(" + str(self.real) + ")"

    def __abs__(self):
        """Return the abosolute value of the complex number."""
        return (self.real**2 - self.imag**2)**0.5

    def __eq__(self, other):
        """Return True if the complex numbers are equal."""
        return self.real == other.real and self.imag == other.imag
    
    def __add__(self, other):
        """Return the sum of the complex numbers."""
        return nonentangled(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        """Return the difference of the complex numbers."""
        return nonentangled(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        """Return the product of the complex numbers."""
        real = self.real * other.real + self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return nonentangled(real, imag)
    
    def __truediv__(self, other):
        """Return the quotient of the complex numbers."""
        if other.real == other.imag:
            return self.collapse(1) / other.collapse(1)
        elif other.real == -other.imag:
            return self.collapse(-1) / other.collapse(-1)
        else:
            real = (self.real*other.real - self.imag*other.imag)/(other.real**2 - other.imag**2)
            imag = (other.real*self.imag - self.real*other.imag)/(other.real**2 - other.imag**2)
            return nonentangled(real, imag)

    def real(self):
        """Return the real part of the complex number."""
        return self.real
    
    def imag(self):
        """Return the imaginary part of the complex number."""
        return float(self.imag)

    def list(self):
        """Return the complex number as a list."""
        return np.array([self.real, self.imag])
    
    def rcollapse(self):
        """Return a random collapse of the split complex number."""
        return float(self.collapse(random.choice([1, -1])))


#nth power (continuous over R)
#euler analogue (continuous over R)
#real numbers to an nth power transformed int split complex numbers
#printing the correct split complex form in arrays (not the pointer)
#how to find the norm of it
#entanglement
#non entangled split complex number
#interactions with complex numbers
