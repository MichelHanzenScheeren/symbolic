from app.shared.error import Error
from app.shared.tokens_definition import TokenType, Utils


class Parser:
  def __init__(self, lexer):
    self.lexer = lexer
    self.currentToken = None
    self.tokenLocation = None
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
    raise Error('Parser error', self.currentToken.value, self.tokenLocation, self.lexer.text, expecteds)

  def parse(self):
    self.main()

  def main(self):
    print('PROGRAM INIT')
    while not self.checkToken(TokenType.EOF):
      print(f'CONSUMED {self.consumeToken(self.currentToken.key)}')
    print('PROGRAM END')
