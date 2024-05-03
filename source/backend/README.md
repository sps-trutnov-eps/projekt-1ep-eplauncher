# Serverový backend aplikace

Složka `api/` obsahuje PHP soubory s jednotlivými skripty, které je možné volat. Každý skript vrací datový objekt ve formátu JSON s klíčem `zprava`.

Složka `sql/` obsahuje SQL soubory, kterými lze vytvořit příslušné tabulky a naplnit je ukázkovými daty.

Soubor `index.html` slouží k ručnímu testování jednotlivých skriptů.

## Seznam skriptů

* `hello.php`
* `users.php`
* `games.php`
* `owned.php`

## Použití

Složka se skripty je pro účely testování dostupná na [školním serveru](http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/).

Pro získání JSON dat je třeba použít HTTP request, např. http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/users.php
