class Token:
  def __init__(self, key, value, showValue=True):
    self.key = key
    self.value = value
    self.showValue = showValue

  def __repr__(self):
    repr = f'<{self.key}:{self.value}>' if self.showValue else f'<{self.key}>'
    return repr.replace('\n', '\\n').replace('\t', '\\t').replace('\r', '\\r').replace('TokenType.', '')
