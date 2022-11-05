class Rectangle:

    def __init__(self, length, width, height):
        if int(length) < 0 or int(width) < 0 or int(height) < 0:
            raise ValueError() 
        self.length = length
        self.width = width
        self.height = height

    def calculate_volume(self):
        return self.length * self.width * self.height
        