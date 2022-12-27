class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    aux_str = "Rectangle(width=" + str(self.width) + ", height=" + str(
      self.height) + ")"
    return aux_str

  def set_width(self, width1):
    self.width = width1

  def set_height(self, height1):
    self.height = height1

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = (2 * self.width + 2 * self.height)
    return perimeter

  def get_diagonal(self):
    perimeter = ((self.width**2 + self.height**2)**.5)
    return perimeter

  def get_picture(self):
    aux_picture = ""
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    for i in range(self.height):
      for j in range(self.width):
        aux_picture += "*"
      aux_picture += "\n"
    return aux_picture

  def get_amount_inside(self, inside):
    aux_R = self.get_area()
    aux_S = inside.get_area()
    aux_T = aux_R // aux_S
    return aux_T


class Square(Rectangle):

  def __init__(self, side):
    self.side = side
    Rectangle.__init__(self, side, side)

  def __str__(self):
    aux_str = "Square(side=" + str(self.side) + ")"
    return aux_str

  def set_side(self, side):
    self.side = side
    Rectangle.set_width(self, self.side)
    Rectangle.set_height(self, self.side)

  def set_width(self, side):
    self.side = side
    Rectangle.set_width(self, self.side)
    Rectangle.set_height(self, self.side)

  def set_height(self, side):
    self.side = side
    Rectangle.set_width(self, self.side)
    Rectangle.set_height(self, self.side)
