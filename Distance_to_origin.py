import math 
class point:
    def __init__ (self,x=0,y=0):
        self.x= x
        self.y= y
    
    def distance_to_origin(self):
         return math.sqrt((self.x**2)+ (self.y**2))
    def reflect(self,axis ):
        if axis=='x':
            self.y= -self.y
        else:
            self.x=-self.x

pt= point(4)
pt.reflect('x') 
print((pt.x, pt.y))
print(pt.distance_to_origin())
