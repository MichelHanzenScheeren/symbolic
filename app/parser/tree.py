class Tree:
  def __init__(self):
    self.nodes = []

  def __repr__(self):
    text = ''
    for index, node in enumerate(self.nodes):
      text += f'\nNode {index + 1}: {node}'
    return text

  def registerNode(self, node):
    self.nodes.append(node)
