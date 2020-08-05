
''' JavaScript Object Notation

##https://www.youtube.com/watch?v=9N6a-VLBa2I // https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-JSON
import json

with open('states.json') as f:
  data = json.load(f)
  print(data)

for state in data['states']:
  print(state)
  print(state['name'])
  print(state['name'],state['abbreviation'])

'''




