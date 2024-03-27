import requests
import random

def show_list(list, title):
    if list:
        print(f'{title.capitalize()}: ')
        for item in list:
            print(f' — {item}')

def get_random_character():
    page = random.randint(1, 7438)
    pageSize = 1

    url = f'https://api.disneyapi.dev/character?pageSize={pageSize}&page={page}'

    response = requests.get(url)
    if response.ok:
        return response.json()['data']
    else:
        print('Щось пішло не так...')
        print(f'{response.status_code=}')


characters = [get_random_character() for _ in range(5)]

for character in characters:
    print('\n\n', character['name'], '\n')
    show_list(character['films'], 'films')
    show_list(character['shortFilms'], 'short films')
    show_list(character['tvShows'], 'tv shows')
    show_list(character['videoGames'], 'video games')

