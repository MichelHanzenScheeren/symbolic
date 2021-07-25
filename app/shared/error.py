# from app.shared.show_error import showError
from app.shared.tokens_definition import TokenType, Utils
from app.lexer.token import Token

class Error(Exception):
  def __init__(self, errorType, symbol, location, text, expecteds=None):
    message = f'{errorType}: '
    if symbol == TokenType.EOF: message += f'Unexpected end of input in {location}.'
    else: message += f'Invalid symbol "{symbol}" in {location}.'
    if expecteds != None: message += f'\n  Was expecting: {self.expectedsText(expecteds)}'
    message += f'\n  {self.showError(text, location.position, location.column, symbol)}'
    super().__init__(message.replace('TokenType.', ''))

  def expectedsText(self, expecteds):
    if not type(expecteds) is list: expecteds = [expecteds]
    for i, value in enumerate(expecteds):
      if i == 0: expectedsText =  f'"{self.getTokenText(value)}"'
      elif i == len(expecteds) - 1: expectedsText += f' or "{self.getTokenText(value)}"'
      else: expectedsText += f', "{self.getTokenText(value)}"'
    return f'{expectedsText or ""}.'

  def getTokenText(self, key):
    if Utils.isComplexToken(key): return key
    return Utils.getTokenSymbol(key)

  def showError(self, text, position, columnStart, symbol):
    columnEnd = columnStart + (1 if symbol == TokenType.EOF else len(symbol))
    idx_start = max(text.rfind('\n', 0, position), 0)
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0: idx_end = len(text)
    line = text[idx_start:idx_end].replace('\t', '') + '\n '
    indicators = ' ' * columnStart + '^' * (columnEnd - columnStart)
    return line + indicators
