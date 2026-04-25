class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height



rect = Rectangle(5, 3)
print("Area =", rect.get_area())