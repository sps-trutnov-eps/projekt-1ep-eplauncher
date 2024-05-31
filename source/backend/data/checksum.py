# Skript pro pocitani kontrolniho souctu (hlavniho) souboru minihry
# (c) Jakub Senkyr, 2024

import hashlib
import os

# zde je treba nastavit spravnou cestu k souboru minihry
soubor_minihry = '../../minihry/Flappy bird/Flappy_Bird_py.py'

with open(soubor_minihry, "rb") as file:
    file_content = file.read()
    
hash_object = hashlib.sha256()
hash_object.update(file_content)
checksum = hash_object.hexdigest()
print('  Kontrolní součet:' + '\n    ' + checksum)
