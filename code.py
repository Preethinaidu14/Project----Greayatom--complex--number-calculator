# --------------
import pandas as pd
import numpy as np
import math


#Code starts herec
class complex_numbers:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return '0.0'
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2fi" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    def __add__(self,other):
        x = self.real+ other.real
        y = self.imag + other.imag
        return(complex_numbers(x,y))
    def __sub__(self,other):
        a = self.real - other.real
        b = self.imag - other.imag
        return(complex_numbers(a,b))
    def __mul__(self,other):
        q = ((self.real) * (other.real) - (self.imag) * (other.imag))
        p = ((self.imag) * (other.real) + (self.real) * (other.imag))
        return(complex_numbers(q,p))
    def __truediv__(self,other):
        q = ((self.real) * (other.real) + (self.imag) * (other.imag))/float(((other.real**2)+(other.imag**2)))
        p = ((self.imag) * (other.real) - (self.real) * (other.imag))/float(((other.real**2)+(other.imag**2)))
        return(complex_numbers(q,p))
    def absolute(self):
        r = ((self.real**2)+(self.imag**2))**(1/2)
        return r
    def argument(self):
        s = math.degrees((math.atan(self.imag/self.real)))
        return s
    def conjugate(self):
        real = self.real
        imag = self.imag
        return complex_numbers(real, -imag)

comp_1 = complex_numbers(3,5)
print(comp_1)
comp_2 = complex_numbers(4,4)
print(comp_2)
comp_sum = (comp_1 + comp_2)
#print(comp_sum)
comp_diff = comp_1 - comp_2
#print(comp_diff)
comp_prod = comp_1*comp_2
#print(comp_prod)
comp_quot = (comp_1/comp_2)
print(comp_quot)
comp_abs = comp_1.absolute()
#print(comp_abs)
comp_conj = comp_1.conjugate()
#print(comp_conj)
comp_arg = comp_1.argument()
print(comp_arg)




