# Skript pro pocitani kontrolniho souctu (hlavniho) souboru minihry
# (c) Jakub Senkyr, 2024

import hashlib

# zde je treba nastavit spravnou cestu k souboru minihry
soubor_minihry = '../minihry/moje_minihra.py'

with open(soubor_minihry, "rb") as file:
    file_content = file.read()
    
hash_object = hashlib.sha256()
hash_object.update(file_content)
checksum = hash_object.hexdigest()
print('  Kontrolní součet:' + '\n    ' + checksum)
