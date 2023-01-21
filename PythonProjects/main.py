import requests
import json

token = '90ce7f904e57a48f4e638d1389bd5bfe'

response = requests.post('https://pokemonbattle.me:5000/trainers/reg', json = {
    "trainer_token": token,
    "email": "nast.zimina.1997@gmail.com",
    "password": "Ziminanast1997"
}, headers = {'Content-Type': 'application/json'})

print(response.text)

response_confirm = requests.post('https://pokemonbattle.me:5000/trainers/confirm_email', json = {
    "trainer_token": token
}, headers = {'Content-Type': 'application/json'})

print(response_confirm.text)

print(response_confirm.status_code)

if response_confirm.status_code == 200:
    print('ok')
else:
    print('not ok')



response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 
'trainer_token': token},
json = {
    "name": "Делавер",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
}) 

pokemon_id = response.json()['id']


response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 
'trainer_token': token}, json = {
    "pokemon_id": pokemon_id,
    "name": "Пикачу",
    "photo": ""
} )

print (response_change.text)


response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type' : 'application/json', 
'trainer_token': token},
json = {
    "pokemon_id": pokemon_id
})

print(response.text)