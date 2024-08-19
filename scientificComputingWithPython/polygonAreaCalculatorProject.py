class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_dimension):
        self.width = new_dimension
         
    def set_height(self, new_dimension):
        self.height = new_dimension
         
    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter =  2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for col in range(self.height):
            picture += f'{"":*^{self.width}}\n'
        return picture
            
    def get_amount_inside(self, other):
        amount_inside = (self.height // other.height) * (self.width // other.width)
        return amount_inside

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, new_dimension):
        self.side = new_dimension
        self.width = new_dimension
        self.height = new_dimension

    def set_width(self, new_dimension):
        self.side = new_dimension
        self.width = new_dimension
        self.height = new_dimension

    def set_height(self, new_dimension):
        self.side = new_dimension
        self.width = new_dimension
        self.height = new_dimension
        
    def __str__(self):
        return f'Square(side={self.side})'





rect = Rectangle(10, 5)
print(rect)
print(f'{rect.get_area() = }')
rect.set_height(3)
print(f'{rect.get_perimeter() = }')
print(f'{rect = !s}')
print(f'{rect.get_picture()}')