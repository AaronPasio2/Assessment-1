glossary = {
  'Float': 'A number, positive or negative, containing one or more decimals.',
  'Integer': 'A a whole number, positive or negative, without decimals, of unlimited length.',
  'String': 'A sequence of characters that is used as data.',
  'Variable': 'Name that represents a value stored in the computer memory.',
  'Function': 'Piece of prewritten code that performs an operation.',
  'While Loop': 'A Condition-Controlled Loop.',
  'For Loop': 'A Count-Controlled Loop.',
  'Comments': 'Notes of explanation within a program.',
  'List': 'An object that contains multiple data items.',
  'Dictionary': 'Object that stores a collection of data.',
  }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")