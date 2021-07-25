class Node:
  def __init__(self, value):
    self.value = value

  def __repr__(self):
    return f'{self.value}'


class UnaryNode:
  def __init__(self, signalNode, valueNode):
    self.signalNode = signalNode
    self.valueNode = valueNode

  def __repr__(self):
    return f'({self.signalNode}, {self.valueNode})'


class BinaryNode:
  def __init__(self, leftNode, operationNode, rightNode):
    self.leftNode = leftNode
    self.operationNode = operationNode
    self.rightNode = rightNode

  def __repr__(self):
    return f'({self.leftNode}, {self.operationNode}, {self.rightNode})'

