class Location:
  def __init__(self, position=0, line=1, column=1):
    self.position = position
    self.line = line
    self.column = column

  def advance(self, character, quantity):
    if quantity == 0: return
    self.position += quantity
    self.column += quantity
    if character == '\n':
      self.line += 1
      self.column = 1

  def __repr__(self):
    return f'line {self.line}, column {self.column}'
  
  def copy(self):
    return Location(self.position, self.line, self.column)
