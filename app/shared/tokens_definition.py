from enum import Enum


### ENUMS TO TOKENS, VERY USEFUL IN PARSER ###
class TokenType(Enum):
  # OPERATORS
  ADD, SUBTRACT = 'ADD', 'SUBTRACT'
  MULTIPLY, DIVIDE, REST = 'MULTIPLY', 'DIVIDE', 'REST'
  ELEVATE, ROOT = 'ELEVATE', 'ROOT'
  LEFT_PAREN, RIGHT_PAREN = 'LEFT_PAREN', 'RIGHT_PAREN'
  # VALUES
  FLOAT, INT = 'FLOAT', 'INT'
  # END OF INPUT
  EOF = 'EOF'


### SIMBOLS OR PATTERNS RELATIONS ###
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
  TokenType.RIGHT_PAREN: ')'
}
NUMBERS_PATTERN = r'[0-9]|[.]'
NUMBERS = {
  TokenType.FLOAT: r'(([0-9])+[.]([0-9])*)|(([0-9])*[.]([0-9])+)',
  TokenType.INT: r'([0-9])+',
}


### UTILITIES TO IDENTIFICATE TOKEN PROPERTIES ###
# This implies to show their value or their key in error messages
def isSimpleToken(key): 
  return OPERATORS.get(key) != None
