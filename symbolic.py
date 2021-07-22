from sys import argv

def run():
  print('Symbolic v1.0 - a python based interpreter')
  if len(argv) == 1 or argv[1] == '-t':
    print('Line-by-line input mode')
    terminal()
  else:
    print('Invalid entry. Was expecting:')
    print('\t-t\t\tTerminal input mode')
    print('\t-f\t\tFile input mode')


def terminal():
  try:
    while True:
      text = input('~> ')
      print(f'text: {text}')
  except KeyboardInterrupt:
    print('\nsee you later! :)', end='')
  except:
    print('Something wrong has happened!')

# Symbolic starts
run()