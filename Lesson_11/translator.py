import requests
import urllib.parse
from colorama import Fore, Back, Style

while True:
    languages = [
        "pirate",
        "morse",
        "minion",
        "yoda",
        "klingon",
        "vulcan",
        "mandalorian"
    ]
    for i in range(0, len(languages)):
        print(f"{i}. {languages[i]}")

    language = languages[int(input(f"{Fore.YELLOW}Please choose language for translation (number): {Style.RESET_ALL}"))]
    sentence = input(f"{Fore.YELLOW}Please enter sentence for translation: {Style.RESET_ALL}")

    resp = requests.api.get(f"http://api.funtranslations.com/translate/{language}?text={urllib.parse.quote(sentence)}")
    if not resp.ok:
        print('Something goes wrong')
        print(resp)
        exit()
    print(f"Translation to {language} language:")
    print(Fore.YELLOW)
    print(resp.json()['contents']['translated'])
    print(Style.RESET_ALL)

    answer = input(f"{Fore.YELLOW}Do you want repeat? (y/n): {Style.RESET_ALL}")
    if answer == "n" or answer == "N":
        break