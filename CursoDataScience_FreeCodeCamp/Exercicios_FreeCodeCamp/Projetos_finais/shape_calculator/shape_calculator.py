class Rectangle:
    def __init__(self, width, height):
        self.set_width = width
        self.set_height = height
        self.get_area = width * height

    def get_perimeter(self):
        return (2 * self.set_width) + (2 * self.set_height)

    def get_diagonal(self):
        return (self.set_width ** 2 + self.set_height ** 2) ** 0.5

    def get_picture(self):
        if self.set_width > 50 or self.set_height > 50:
            return "Too big for picture."

        picture = ""
        for i in range(self.set_height):
            picture += "*" * self.set_width + "\n"
        return picture

class Square(Rectangle):
    def __init__(self, side):
        # Chama o construtor da classe pai (Rectangle) passando o mesmo valor para largura e altura.
        super().__init__(side, side)
