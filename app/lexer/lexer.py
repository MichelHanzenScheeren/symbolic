import re as regex
from app.lexer.location import Location
from app.lexer.token import Token
from app.shared.tokens_definition import *
from app.shared.error import Error


class Lexer:
  def __init__(self, text='', origin='unknown'):
    self.text = text
    self.origin = origin
    self.location = Location()
    self.currentChar = self.peekAhead(quantity=0) # Initialization with first char

  def consumeChar(self, quantity=1):
    self.location.advance(self.currentChar, quantity)
    self.currentChar = self.text[self.location.position] if self.location.position < len(self.text) else None
    return self.text[self.location.position - quantity]

  def peekAhead(self, quantity=1):
    next = self.location.position + quantity
    return self.text[next] if next < len(self.text) else None

  def abort(self):
    symbol = TokenType.EOF if self.currentChar is None else self.currentChar
    raise Error('Lexer error', symbol, self.location.copy(), self.text)

  def nextToken(self):
    while self.is_skip(): self.consumeChar()
    if self.currentChar is None:
      return (Token(TokenType.EOF, 'EOF', False), self.location.copy())
    if self.match(NUMBERS_PATTERN, self.currentChar): 
      return self.regexClassification(NUMBERS_PATTERN, NUMBERS, self.match)
    if self.match(WORDS_PATTERN, self.currentChar):
      return self.regexClassification(WORDS_PATTERN, WORDS, self.matchOrCompare)
    return self.staticTokens()

  def is_skip(self):
    for value in SKIP:
      if self.currentChar == value: return True
    return False

  def match(self, pattern, character):
    return bool(regex.match(pattern, character))

  def regexClassification(self, pattern, iterator, validateFunction):
    location = self.location.copy()
    term = self.advanceWhileMatch(pattern)
    for key, value in iterator.items():
      if validateFunction(value, term):
        return (Token(key, term, Utils.isComplexToken(key)), location)
    self.abort()

  def advanceWhileMatch(self, pattern, term = ''):
    while self.currentChar != None and self.match(pattern, self.currentChar):
      term += self.consumeChar()
    return term

  def matchOrCompare(self, value, term):
    if value.find('*') != -1 or value.find('[') != -1:
      return self.match(value, term)
    return value == term

  def staticTokens(self):
    result = self.staticClassification(OPERATORS)
    if result is not None: return result
    self.abort()

  def staticClassification(self, iterator):
    location = self.location.copy()
    for key, value in iterator.items():
      term = self.getCharacters(len(value))
      if value == term:
        self.consumeChar(len(term))
        return (Token(key, term, Utils.isComplexToken(key)), location)
    return None

  def getCharacters(self, quantity):
    characters, currentChar, index = '', self.currentChar, 0
    while currentChar != None and quantity - len(characters) > 0:
      characters += currentChar
      index += 1 
      currentChar = self.peekAhead(index)
    return characters
