from enum import Enum


### ENUMS TO TOKENS, VERY USEFUL IN PARSER ###
class TokenType(Enum):
  # OPERATORS
  ADD, SUBTRACT = 'ADD', 'SUBTRACT'
  MULTIPLY, DIVIDE, REST = 'MULTIPLY', 'DIVIDE', 'REST'
  ELEVATE, ROOT = 'ELEVATE', 'ROOT'
  LEFT_PAREN, RIGHT_PAREN = 'LEFT_PAREN', 'RIGHT_PAREN'
  OR, AND = 'OR', 'AND',
  EQUAL, DIFFERENT, NOT = 'EQUAL', 'DIFFERENT', 'NOT'
  GREATER_EQUAL, GREATER = 'GREATER_EQUAL', 'GREATER'
  LESS_EQUAL, LESS = 'LESS_EQUAL', 'LESS'
  # VALUES
  FLOAT, INT, FALSE, TRUE = 'FLOAT', 'INT', 'FALSE', 'TRUE'
  IDENTIFIER = 'IDENTIFIER'
  # END OF INPUT
  EOF = 'EOF'


### SYMBOLS OR PATTERNS RELATIONS ###
SKIP = [' ', '\r', '\t', '\n']
OPERATORS = {
  TokenType.ADD: '+',
  TokenType.SUBTRACT: '-',
  TokenType.MULTIPLY: '*',
  TokenType.DIVIDE: '/',
  TokenType.REST: '%',
  TokenType.ELEVATE: '^',
  TokenType.ROOT: '~',
  TokenType.LEFT_PAREN: '(',
  TokenType.RIGHT_PAREN: ')',
  TokenType.OR: '||',
  TokenType.AND: '&&',
  TokenType.EQUAL: '==',
  TokenType.DIFFERENT: '!=',
  TokenType.NOT: '!',
  TokenType.GREATER_EQUAL: '>=',
  TokenType.GREATER: '>',
  TokenType.LESS_EQUAL: '<=',
  TokenType.LESS: '<',
}
NUMBERS_PATTERN = r'[0-9]|[.]'
NUMBERS = {
  TokenType.FLOAT: r'(([0-9])+[.]([0-9])*)|(([0-9])*[.]([0-9])+)',
  TokenType.INT: r'([0-9])+',
}

WORDS_PATTERN = r'[A-Z]|[a-z]|[_]|[0-9]'
WORDS = {
  TokenType.TRUE: 'True',
  TokenType.FALSE: 'False',
  TokenType.IDENTIFIER: r'([A-Z]|[a-z]|[_])([A-z]|[a-z]|[0-9]|[_])*',
}


### UTILITIES TO IDENTIFY TOKEN PROPERTIES ###
# This implies to show their value or their key in error messages
class Utils:
  @staticmethod
  def isComplexToken(key): 
    return OPERATORS.get(key) is None and key not in [TokenType.TRUE, TokenType.FALSE]

  @staticmethod
  def getTokenSymbol(key):
    symbol = OPERATORS.get(key)
    return symbol or key
