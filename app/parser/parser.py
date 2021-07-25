from app.shared.error import Error
from app.shared.tokens_definition import TokenType
from app.parser.nodes import *
from app.parser.tree import Tree


class Parser:
  def __init__(self, lexer):
    self.lexer = lexer
    self.currentToken = None
    self.tokenLocation = None
    self.tree = Tree()
    self.nextToken()

  def nextToken(self):
    self.currentToken, self.tokenLocation = self.lexer.nextToken()

  def checkToken(self, tokens):
    if type(tokens) is list:
      return self.currentToken.key in tokens
    return self.currentToken.key == tokens

  def consumeToken(self, tokens):
    current = self.currentToken
    if self.checkToken(tokens): self.nextToken()
    else: self.abort(tokens)
    return current

  def abort(self, expecteds):
    symbol = self.currentToken.value if self.currentToken.key != TokenType.EOF else self.currentToken.key
    raise Error('Parser error', symbol, self.tokenLocation, self.lexer.text, expecteds)

  def parse(self):
    print('PROGRAM INIT')
    while not self.checkToken(TokenType.EOF):
      self.statement()
    print('PROGRAM END')
    print(self.tree)

  def statement(self):
    print('START STATEMENT')
    self.tree.registerNode(self.expression())
    print('END STATEMENT')

  def expression(self):
    left = self.term()
    if self.checkToken([TokenType.ADD, TokenType.SUBTRACT]):
      operation = self.consumeToken([TokenType.ADD, TokenType.SUBTRACT])
      return BinaryNode(left, Node(operation), self.expression())
    return left

  def term(self):
    left = self.factor()
    if self.checkToken([TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.REST]):
      operation = self.consumeToken([TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.REST])
      return BinaryNode(left, Node(operation), self.term())
    return left

  def factor(self):
    left = self.unary()
    if self.checkToken([TokenType.ELEVATE]):
      operation = self.consumeToken([TokenType.ELEVATE])
      return BinaryNode(left, Node(operation), self.factor())
    return left

  def unary(self):
    if self.checkToken([TokenType.ADD, TokenType.SUBTRACT]):
      signal = self.consumeToken([TokenType.ADD, TokenType.SUBTRACT])
      return UnaryNode(Node(signal), self.unary())
    else:
      return self.value()

  def value(self):
    if self.checkToken([TokenType.FLOAT, TokenType.INT]):
      return Node(self.consumeToken([TokenType.FLOAT, TokenType.INT]))
    elif self.checkToken(TokenType.LEFT_PAREN):
      self.consumeToken(TokenType.LEFT_PAREN)
      binaryOperation = self.expression()
      self.consumeToken(TokenType.RIGHT_PAREN)
      return binaryOperation
    self.abort([TokenType.FLOAT, TokenType.INT, TokenType.LEFT_PAREN])
