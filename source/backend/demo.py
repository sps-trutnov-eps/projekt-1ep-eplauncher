# Ukazka pouziti serveroveho API primo z Pythonu
# (c) Jakub Senkyr, 2024

import requests
import json

print('Tento skript demonstruje komunikaci s databází na serveru pomocí HTTP')
input('<Enter> pro pokračování...')
print()

# 1) hello (prijata data jako JSON objekt)
url = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/hello.php'
response = requests.get(url)
print('Toto jsou surová data vrácená z URL', url)
print(response.text)
print()

print('Toto jsou data extrahovaná z formátu JSON')
print(json.loads(response.text)['message'])
input('<Enter> pro pokračování...')
print()

# 2) users (prijata data jako JSON pole objektu)
url = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/users.php'
response = requests.get('http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/users.php')
print('Toto jsou surová data vrácená z URL', url)
print(response.text)
print()

print('Toto jsou data extrahovaná z formátu JSON')
users = json.loads(response.text)
for user in users:
    print(user)
input('<Enter> pro pokračování...')
print()

# 3) check_user (prijata data jako JSON objekt s True nebo chybou ve stringu)
username = input('Zadej jméno uživatele: ')
password = input('Zadej heslo uživatele: ')
user = {'username': username, 'password': password}
url = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/check_user.php'
response = requests.post(url, json = user)
print('Toto jsou surová data vrácená z URL', url)
print(response.text)
print()

print('Toto jsou data extrahovaná z formátu JSON')
print(json.loads(response.text)['vysledek'])
input('<Enter> pro pokračování...')
print()

print('A to je vše, lidičky!')
