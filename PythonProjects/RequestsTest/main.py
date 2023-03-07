import requests

token = '2f1497b0dc664f98f6018854c86e71ea'

reg_trainer_response = requests.post('https://pokemonbattle.me:9104/trainers/reg',
                        headers = {'Content-Type' : 'application/json'},
                        json = {"trainer_token" : token, "email": "mr.guchenko@mail.ru", "password": "Iloveqa1"})
print(reg_trainer_response.text)

confirm_response = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email',
                        headers = {'Content-Type' : 'application/json'},
                        json = {"trainer_token" : token})
print(confirm_response.text)

add_pokemons_response = requests.post('https://pokemonbattle.me:9104/pokemons', 
                        headers = {'Content-Type' : 'application/json',
                        'trainer_token' : token},
                        json = {"name": "Бульбазавр",
                                "photo": "https://dolnikov.ru/pokemons/albums/010.png"})
print(add_pokemons_response.text)

change_name_pokemon = requests.put('https://pokemonbattle.me:9104/pokemons',
                         headers = {'Content-Type' : 'application/json',
                        'trainer_token' : token},
                        json = {"pokemon_id": 6020,
                                "name": "Пикачу",
                                "photo": "https://dolnikov.ru/pokemons/albums/010.png"})
print(change_name_pokemon.text)

add_a_pokemon_to_a_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball',
                         headers = {'Content-Type' : 'application/json',
                        'trainer_token' : token},
                        json = {"pokemon_id": 6020,})
print(add_a_pokemon_to_a_pokeball.text)