from app.shared.error import Error
from app.shared.tokens_definition import TokenType
from app.parser.nodes import *
from app.parser.tree import Tree


CONSTANTS = [TokenType.DECIMAL, TokenType.INTEGER, TokenType.FALSE, TokenType.TRUE]
DATA_TYPE = [TokenType.FLOAT, TokenType.INT, TokenType.BOOL]

class Parser:
  def __init__(self, lexer):
    self.lexer = lexer
    self.tree = Tree()
    self.currentToken = None
    self.tokenLocation = None
    self.nextToken = None
    self.nextTokenLocation = None
    self.getNextToken()
    self.getNextToken()

  def getNextToken(self):
    self.currentToken, self.tokenLocation = self.nextToken, self.nextTokenLocation
    self.nextToken, self.nextTokenLocation = self.lexer.nextToken()

  def checkToken(self, tokens):
    if type(tokens) is list:
      return self.currentToken.key in tokens
    return self.currentToken.key == tokens

  def checkNextToken(self, tokens):
    if type(tokens) is list:
      return self.nextToken.key in tokens
    return self.nextToken.key == tokens

  def consumeToken(self, tokens):
    current = self.currentToken
    if self.checkToken(tokens): self.getNextToken()
    else: self.abort(tokens)
    return current

  def abort(self, expecteds):
    symbol = self.currentToken.value if self.currentToken.key != TokenType.EOF else self.currentToken.key
    raise Error('Parser error', symbol, self.tokenLocation, self.lexer.text, expecteds)

  def registerNode(self, node):
    self.tree.registerNode(node)

  def parse(self):
    while not self.checkToken(TokenType.EOF):
      if (self.line()): continue
      self.abort([TokenType.IDENTIFIER] + CONSTANTS + DATA_TYPE)
    print(self.tree)

  def line(self):
    if self.checkToken(TokenType.END_LINE): 
      return self.endLine()
    elif self.checkToken(TokenType.IDENTIFIER):
      self.registerNode(self.identifierOption())
      return self.endLine()
    elif self.checkToken(CONSTANTS):
      self.registerNode(self.expression())
      return self.endLine()
    elif self.checkToken(DATA_TYPE):
      self.registerNode(self.variableDeclaration())
      return self.endLine()
    return False

  def endLine(self):
    if self.checkToken(TokenType.EOF): return True
    self.consumeToken(TokenType.END_LINE)
    while self.checkToken(TokenType.END_LINE):
      self.consumeToken(TokenType.END_LINE)
    return True

  def identifierOption(self):
    if self.checkNextToken(TokenType.ASSIGNMENT):
      variableNode = VariableNode(self.consumeToken(TokenType.IDENTIFIER))
      return VariableAssignmentNode(variableNode, self.assignment())
    else:
      return self.expression()

  def expression(self):
    return self.binaryOperation(self.andExpression, self.expression, TokenType.OR)

  def andExpression(self):
    return self.binaryOperation(self.notExpression, self.andExpression, TokenType.AND)

  def notExpression(self):
    if self.checkToken(TokenType.NOT):
      return UnaryNode(ValueNode(self.consumeToken(TokenType.NOT)), self.notExpression())
    return self.boolOperators()

  def boolOperators(self):
    tokens = [TokenType.EQUAL, TokenType.DIFFERENT, TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL]
    return self.binaryOperation(self.mathExpression, self.boolOperators, tokens)

  def mathExpression(self):
    return self.binaryOperation(self.term, self.mathExpression, [TokenType.ADD, TokenType.SUBTRACT])

  def term(self):
    return self.binaryOperation(self.factor, self.term, [TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.REST])

  def factor(self):
    return self.binaryOperation(self.unary, self.factor, TokenType.ELEVATE)

  def binaryOperation(self, nextFunction, currentFunction, tokens):
    left = nextFunction()
    if self.checkToken(tokens):
      operation = self.consumeToken(tokens)
      return BinaryNode(left, ValueNode(operation), currentFunction())
    return left

  def unary(self):
    if self.checkToken([TokenType.ADD, TokenType.SUBTRACT]):
      signal = self.consumeToken([TokenType.ADD, TokenType.SUBTRACT])
      return UnaryNode(ValueNode(signal), self.unary())
    return self.value()

  def value(self):
    if self.checkToken(CONSTANTS):
      return self.constans()
    elif self.checkToken(TokenType.IDENTIFIER): 
      return self.variables()
    elif self.checkToken(TokenType.LEFT_PAREN):
      self.consumeToken(TokenType.LEFT_PAREN)
      binaryOperation = self.expression()
      self.consumeToken(TokenType.RIGHT_PAREN)
      return binaryOperation
    self.abort(CONSTANTS + [TokenType.IDENTIFIER])

  def constans(self):
    node = self.consumeToken(CONSTANTS)
    return ValueNode(node)

  def variables(self):
    node = self.consumeToken(TokenType.IDENTIFIER)
    return VariableNode(node)

  def variableDeclaration(self):
    type = self.dataType()
    return VariableDeclarationNode(type, self.declarationList())

  def dataType(self):
    return self.consumeToken(DATA_TYPE)

  def declarationList(self):
    node = VariableNode(self.consumeToken(TokenType.IDENTIFIER))
    if self.checkToken(TokenType.ASSIGNMENT): 
      node = VariableAssignmentNode(node, self.assignment())
    if self.checkToken(TokenType.COMMA):
      self.consumeToken(TokenType.COMMA)
      return [node] + self.declarationList()
    return [node]

  def assignment(self):
    self.consumeToken(TokenType.ASSIGNMENT)
    return self.expression()
