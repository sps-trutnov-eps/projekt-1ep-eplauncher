# Serverový backend aplikace

Složka `api/` obsahuje PHP soubory s jednotlivými skripty, které je možné volat. Každý skript vrací datový objekt ve formátu JSON s klíčem `zprava`.

Složka `sql/` obsahuje SQL soubory, kterými lze vytvořit příslušné tabulky a naplnit je ukázkovými daty.

Soubor `index.html` slouží k ručnímu testování jednotlivých skriptů.

## Seznam skriptů

* `hello.php` (HTTP GET, vrací JSON s textem)

* `users.php` (HTTP GET, vrací JSON s daty)
* `games.php` (HTTP GET, vrací JSON s daty)
* `owned.php` (HTTP GET, vrací JSON s daty)

* `add_user.php` (HTTP POST, vrací JSON s výsledkem - True nebo chybové hlášení ve stringu)
* `buy_game.php` (HTTP POST, vrací JSON s výsledkem - True nebo chybové hlášení ve stringu)
* `check_user.php` (HTTP POST, vrací JSON s výsledkem - True nebo chybové hlášení ve stringu)

## Použití

Skripty  pro účely testování přímo v projektu jsou dostupné na URL http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/ pod svými jmény.

Pro získání JSON dat je třeba použít HTTP request na dané URL (např. http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/users.php).

Ruční testování lze provádět na [HTML stránce](http://senkyr.epsilon.spstrutnov.cz/eplauncher/index.html).
