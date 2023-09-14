import json

data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)

# Acessando outros valores no dicionário 'info'
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print("Phone:", info["phone"]["number"])

# Acessando e modificando outros valores no dicionário 'info'
info["address"] = "123 Main Street"
info["phone"]["extension"] = "1234"

# Exibindo todos os valores no dicionário 'info'
for key, value in info.items():
    print(key + ":", value)
