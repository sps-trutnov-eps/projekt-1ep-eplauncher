# Ukazka dosazeni achievementu v minihre
# (c) Jakub Senkyr, 2024

import demo_main

jmeno_hry = 'Pokusná minihra'
jmeno_odznacku = 'Pokusný achievement'

def zverejneni_jmena():
    return jmeno_hry

def dosazeni_achievementu():
    print('\t\tNyní dosáhneme achievementu...')
    demo_main.unlock(jmeno_odznacku)
    print('\t\t...a hotovo!')

def main():
    print('\tJsme v minihře...')
    dosazeni_achievementu()
    print('\tMinihra končí.')

if __name__ == "__main__":
    main()
