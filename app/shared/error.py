# from app.shared.show_error import showError
from app.shared.tokens_definition import TokenType, Utils
from app.lexer.token import Token

class Error(Exception):
  def __init__(self, errorType, symbol, location, text, expected=None):
    message = f'{errorType}: '
    if symbol == TokenType.EOF: message += 'Unexpected end of input'
    else: message += f'Invalid symbol "{symbol}"'
    message += f' in {location}.'
    if expected != None: message += f'\n  Was expecting: {expected}'
    columnEnd = location.column + (1 if symbol == TokenType.EOF else len(symbol))
    message += f'\n  {self.showError(text, location.position, location.column, columnEnd)}'
    super().__init__(message.replace('TokenType.', ''))

  def showError(self, text, position, columnStart, columnEnd):
    idx_start = max(text.rfind('\n', 0, position), 0)
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0: idx_end = len(text)
    line = text[idx_start:idx_end].replace('\t', '') + '\n '
    indicators = ' ' * columnStart + '^' * (columnEnd - columnStart)
    return line + indicators
