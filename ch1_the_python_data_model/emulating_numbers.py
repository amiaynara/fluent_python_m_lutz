import math

class Vector():
  
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    '''Note that repr is string representation that should be\
    unambiguous. If possible should be code to recreate the object.
    repr is fallback for str'''
    return f'Vector({self.x!r}, {self.y!r})'  # the data type should not be lost
  # Note: if you have to implement one, implement __repr__

  def __str__(self):
    '''This is called by str() built-in and implicitly used when
    print() function is used'''
    return f'Vector({self.x}, {self.y})'

  def __abs__(self):
    return math.hypot(x, y)


# Note: Python has a bool type. But it aso uses objects in Boolean context (as conditions in if or while)
# Object are also used as operands to logical operators and, or, not.
# By default the users' objects are treated as truthy, unless __bool__ has been implemented. 
# If x.__bool__() is called when we do bool(x), if __bool__ is not implemented x.__len__() is called. 
  def __bool__(self):
    return bool(abs(self))
# A faster implementation of __bool_)
  def __bool__(self):
    return bool(self.x or self.y) # it avoids the whole trip abs -> __abs__ -> squares -> square roots

  def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)

  def __mul__(self, scaler):
    return Vector(self.x * scalar, self.y * scalar) # ???

def main():
  vector = Vector(1, 3)
  print(vector)
if __name__ == '__main__':
  main()
