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

## SQL schema

Backend udržuje data ve třech tabulkách s následujícími sloupci:

* `1ep_eplauncher_users` přehled registrovaných hráčů
  - `id` jednoznačný identifikátor hráče, autoinkrementované celé číslo
  - `username` uživatelské jméno po přihlašování, unikátní text
  - `password` hash hesla získaný pomocí Bcrypt, text
  - `money` měna pro odemykání her, celé číslo
* `1ep_eplauncher_games` přehled her v nabídce
  - `id` jednoznačný identifikátor hry, autoinkrementované celé číslo
  - `name` jméno hry pro zobrazení, unikátní text
  - `price` cena hry potřebná pro její odemčení, celé číslo
  - `unlock_key` tajná fráze pro odemčení hry, text
  - `checksum` kontrolní součet zdrojového souboru hry, text
* `1ep_eplauncher_owned` přehled transakcí nákupů
  - `id` jednoznačný identifikátor transakce, autoinkrementované celé číslo
  - `user_id` kdo transakci provedl, číslo korespondující s `id` v tabulce uživatelů
  - `game_id` kterou hru si odemkl, číslo korespondující s `id` v tabulce her
  - `from_when` kdy k transakci došlo, timestamp okamžiku zanesení záznamu do tabulky
