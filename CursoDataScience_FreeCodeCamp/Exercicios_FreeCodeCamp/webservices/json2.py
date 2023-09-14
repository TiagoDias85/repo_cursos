import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
  { "id" : "029",
    "x" : "37",
    "name" : "Trent"
  }
]'''

info = json.loads(data)
print("Contagem de Agentes:", len(info))

for item in info:
    for key, value in item.items():
        print(key + ":", value)
