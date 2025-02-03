class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y



class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius,radius)
       
    def area (self):
       return 3.14 * super().area()
    

cal = circle(3)
print(cal.area())

i=0
for i in range(10):
    i = i + 1
    print (i)
