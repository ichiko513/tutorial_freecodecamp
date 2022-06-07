
class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        pass
    def __str__(self) -> str:
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)
    # def __repr__(self) -> str:
    #     pass
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        pic = '';
        for h in range(self.height):
            pic += ''.join([ '*' for w in range(self.width) ]) + '\n'
        return pic
    def get_amount_inside(self, rect):
        return ( self.width // rect.width ) * (self.height // rect.height)

class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side,side)
    def __str__(self) -> str:
        return 'Square(side={})'.format(self.width)
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
    def set_width(self, width):
        self.set_side(width)
    def set_height(self, height):
        self.set_side(height)

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

