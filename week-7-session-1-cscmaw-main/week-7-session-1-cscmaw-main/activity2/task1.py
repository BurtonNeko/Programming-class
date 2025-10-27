# Define a Circle class with a single field named radius. The value for radius is passed
# when an instance of Circle is created. In this class, define the following methods:
# (1) get_radius to return the radius of the circle
# (2) perimeter to return the perimeter of the circle, perimeter = 2 * Pi * radius (you can set Pi = 3.142)
# (3) area to return the area of a circle, area = Pi * radius * radius
class Circle:
    PI = 3.14
    
    def __init__(self, radius):
        self.set_eadius(radius)
        
    def get_raduis(self):
        return self.radius
    
    def set_radius(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative.')
        self.radius = radius
        
    def peremeter(self):
        return 2 * Circle.PI * self.radius
    
    def area(self):
        return Circle.PI * self.radius * self.radius




# Once completed, create two instances of Circle with different radius, eg 4.5, 10.8
# and print the radius, perimeter, and area for both instances




# Did you create a setter for radius? Can the radius be a negative number?
# If you have not, create a setter for radius with validation.
