import requests

url = 'https://www.whenisthenextmcufilm.com/api'
response = requests.get(url)

if response.ok:
    as_json = response.json()
    print('= When is the next MCU film? =')
    print(f"{as_json['title']} releases in {as_json['days_until']} days!")
    print(f"{as_json['following_production']['title']=}")
else:
    print('Щось пішло не так...')
    print(f'{response.status_code=}')

