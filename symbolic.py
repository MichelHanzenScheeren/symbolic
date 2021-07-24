from app.parser.parser import Parser
from app.shared.tokens_definition import TokenType
from app.lexer.lexer import Lexer
from sys import argv


def run():
  print('Symbolic v1.0 - a python based interpreter')
  if len(argv) == 1 or argv[1] == '-t':
    print('Line-by-line input mode')
    terminal()
  else:
    print('Invalid entry. Was expecting:')
    print('\t-t\t\tTerminal input mode')


def terminal():
  try:
    while True:
      text = input('~> ')
      lexer = Lexer(text, 'terminal')
      parser = Parser(lexer)
      parser.parse()
  except KeyboardInterrupt:
    print('\nsee you later! :)', end='')
  except Exception as error:
    print(error)


run() # Symbolic starts
