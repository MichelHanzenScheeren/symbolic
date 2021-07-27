class VariableNode:
  def __init__(self, value):
    self.value = value
  def __repr__(self):
    return f'{self.value}'

class ValueNode:
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

class VariableDeclarationNode:
  def __init__(self, dataType, variablesList):
    self.dataType = dataType
    self.variablesList = variablesList
  def __repr__(self):
    # text = self.variablesList[0]
    # for i in range(1, len(self.variablesList)):
    #   text += f', { self.variablesList[i].__repr__()}'
    return f'({self.dataType}, {self.variablesList})'

class VariableAssignmentNode:
  def __init__(self, variableNode, valueNode):
    self.variableNode = variableNode
    self.valueNode = valueNode
  def __repr__(self):
    return f'({self.variableNode}, {self.valueNode})'
