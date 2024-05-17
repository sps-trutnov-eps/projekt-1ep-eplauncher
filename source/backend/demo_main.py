# Ukazka overeni dosazeni achievementu v minihre v hlavnim kodu
# (c) Jakub Senkyr, 2024

import requests
import inspect
import hashlib
import json
import os

import demo_minihra

jmeno_hrace = 'senkyr'

def unlock(how_many):
    print('Nahlášeno dosažení achievementu, probíhá kontrola...')
    
    # z prijateho volani ziskame informace o volajicim
    stack = inspect.stack()    
    soubor_minihry = stack[1].filename
    modul_minihry = inspect.getmodule(stack[1][0])
    print('  Volající soubor:' + '\n    ' + os.path.basename(soubor_minihry))
    print('  Volající modul:' + '\n    ' + modul_minihry.__name__)
    
    # zjistime si jmeno minihry
    jmeno_hry = modul_minihry.zverejneni_jmena()

    # spocitame si checksum souboru s minihrou
    with open(soubor_minihry, "rb") as file:
        file_content = file.read()
    
    hash_object = hashlib.sha256()
    hash_object.update(file_content)
    checksum = hash_object.hexdigest()
    print('  Kontrolní součet:' + '\n    ' + checksum)
    
    # sestavime data a odesleme je k overeni na server
    data = {'checksum': checksum, 'game_name': jmeno_hry, 'username': jmeno_hrace}
    url = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/get_money.php'
    
    print('  Data se odesílají na server k ověření...')
    response = requests.post(url, json = data)
    vysledek = json.loads(response.text)['vysledek']
    
    # zde zjistime, jestli bylo hlaseni o achievementu legitimni
    if vysledek == True:
        print('    Potvrzení proběhlo úspěšně :-)')
    else:
        print('    Potvrzení selhalo :-(')
    
    print('Kontrola skončila.')

def main():
    print('Jsme v hlavním programu...')
    print('Nyní spustíme minihru...')
    demo_minihra.main()
    print('Hlavní program končí.')

if __name__ == "__main__":
    main()
