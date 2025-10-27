import math

# Define a class Coordinate with fields x and y. The value to these fields
# are passed to the __init__ method when an instance of Coordinate is created.
# Define a setter method for x and for y, which only accept numbers.
# Then, define a method called distance. The distance method should take
# another instance of Coordinate as an argument and returns the distance between 
# the two coordinates. The formula to find the distance between the two coordinates,
# distance = √((x2 – x1)² + (y2 – y1)²). You can use math.sqrt() function for the square root
class Coordinate:
    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)
        
    def set_x(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError('x must be a number.')
        self.x = x
        
    def set_y(self, y):
        if not isinstance(y, (int, float)):
            raise TypeError('y must be a number.')
        self.y = y

    def distance(self, other):
        if not isinstance(other,(Coordinate)):
            raise TypeError('Augument must be an instance of Coordinate.')
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx**2 + dy**2)







# Once completed, create two instances of Coordinates:
# coordinate1 with x = 3, y = 4
# coordinate2 with x = 9, y = 12
# and print the distance between coordinate1 and coordinate2
# with the distance method in both coordinates. Are they the same?








# Once you have completed with the distance method, update the class definition with
# another method called slope to calculate the slope between the two coordinates.
# The formula for slop is (y2 - y1) /( x2 - x1). Then, print the slopes between the two coordinates
# you have created previously.
