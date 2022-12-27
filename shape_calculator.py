class Rectangle:
  
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    aux_str = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    #aux_str = str(Rectangle(width=self.width, height=self.height))
    return aux_str

  def set_width(self,width1):
    self.width = width1
    
  def set_height(self,height1):
    self.height = height1
    
  def get_area(self):
    area = self.width * self.height
    return area
    
  def get_perimeter(self):
    perimeter = (2 * self.width + 2 * self.height)
    return perimeter
    
  def get_diagonal(self):
    perimeter = ((self.width ** 2 + self.height ** 2) ** .5)
    return perimeter
    
  def get_picture(self):
    aux_picture = ""
    if self.height or self.width > 50:
      return "Too big for picture."
    for i in range(self.height):
      for j in range(self.width):
        aux_picture += "*"
      aux_picture += "\n"
    return aux_picture
    
  def get_amount_inside(self):
    print("")
    
    
  
  
  
  
  
class Square:
  def __init__(Rectangle,side):
    Rectangle.self.width = side
    Rectangle.self.width = side
    print("")

  def set_side(self,side1):
    Rectangle.self.width = side1
    Rectangle.self.width = side1