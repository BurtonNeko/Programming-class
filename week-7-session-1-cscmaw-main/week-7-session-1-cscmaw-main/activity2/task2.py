# Create an updated version of the Rectangle class from activity1/task2 with the following methods:
# (1) area method to return the area of a rectangle
# (2) perimeter method to return the perimeter of a rectangle
class Rectangle:
    def __init__(self, wid, high):
        self.height = high
        self.width = wid

    def set_height(self, high):
        self.height = high

    def set_width(self,wid):
        self.width = wid

    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width
    
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return self.hight * 2 + self.width * 2

rectangle1 = Rectangle(5, 8)
print(rectangle1.height)
print(rectangle1.width)

rectangle1.set_height(10)
print(rectangle1.height)





# Once completed, create 2 instances of Rectangles with:
# (1) first rectangle with width = 4 and height = 40
# (2) second rectangle with width = 3.5 and height=35.9
# After that, print the area and perimeter of both rectangle instances.




# Did you have setters with validation? Can the value of width and height be negative?
# If you have not, update the setters with validation for the width and height.
