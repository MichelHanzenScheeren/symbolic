from app.parser.parser import Parser
from app.shared.tokens_definition import TokenType
from app.lexer.lexer import Lexer
from sys import argv
from os.path import basename


def run():
  print('Symbolic v1.0 - a python based interpreter')
  if len(argv) == 1 or argv[1] == '-t' or argv[1] == 'terminal':
    print('Line-by-line input mode\n')
    fromTerminal()
  elif argv[1] == '-f' or argv[1] == 'file':
    print('File input mode\n')
    fromFile(argv)
  else:
    print('Invalid entry. Was expecting:')
    print('\t-t\t\tTerminal input mode')


def fromTerminal():
  try:
    while True:
      text = input('~> ') + '\n'
      execute(text, 'terminal')
  except KeyboardInterrupt:
    print('\nsee you later! :)')
  except Exception as error:
    print(error)


def fromFile(argv):
  try:
    if len(argv) < 3: 
      return print('You need to inform a relative file path.')
    with open(argv[2], "r") as myFile: 
      text, origin = myFile.read(), basename(myFile.name)
    execute(text, origin)
  except:
    print('Could not open the specified file')


def execute(text, origin):
  try:
    lexer = Lexer(text, origin)
    parser = Parser(lexer)
    parser.parse()
  except Exception as error:
    print(error)
  # while True:
  #   symbol, location = lexer.nextToken()
  #   print(symbol)
  #   if symbol.key == TokenType.EOF: break 
  

run() # Symbolic starts
