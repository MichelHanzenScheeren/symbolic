class Tree:
  def __init__(self):
    self.nodes = []

  def __repr__(self):
    text = ''
    for index, node in enumerate(self.nodes):
      text += f'Node {index + 1}: {node}'
      if index != len(self.nodes) - 1:  text += '\n'
    return text

  def registerNode(self, node):
    self.nodes.append(node)
