import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL do serviço de API
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    # Parâmetros da requisição
    parms = dict()
    parms['address'] = address
    parms['key'] = '42'  # Adicionar a chave aqui
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # Obtendo o place_id do primeiro resultado
    place_id = js['results'][0]['place_id']
    print('Place id', place_id)

    #print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
