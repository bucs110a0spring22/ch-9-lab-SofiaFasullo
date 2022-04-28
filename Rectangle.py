class Rectangle:
  def __init__(self, x, y, h, w):
    if x < 0:
      self.x = 0
    else:
      self.x = x
    if y < 0:
      self.y = 0
    else:
      self.y = y
    if h < 0:
      self.height = 0
    else:
      self.height = h
    if w < 0:
      self.width = 0
    else:
      self.width = w
  

  def __str__(self):
    return "(x : " + str(self.x) + ", y : " + str(self.y) + "), width : " + str(self.width) + ", height : " + str(self.height)