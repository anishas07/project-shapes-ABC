from abc import ABC, abstractmethod
class shapes(ABC) :
    def area(self):
            pass
    
class triangle(shapes):
    
    def area(self):
            print("The area of a triangle is, 1/2*4*4" )
class circle(shapes):

    def area(self):
            print("The area of a circle is, 4*5")
      
class square(shapes):

    def area(self):
            print("The area of a square is,5*5" )

#code
R = triangle()
R.area()

K = circle()
K.area()

S = square()
S.area()