# Serverový backend aplikace

## Obsah složky `backend`

Složka `api/` obsahuje PHP skripty, které je možné volat přes HTTP. Každý skript vrací datový objekt ve formátu [JSON](https://www.json.org/json-en.html).

Složka `sql/` obsahuje SQL skripty, kterými lze na databázovém serveru vytvořit příslušné tabulky.

Složka `demo/` obsahuje ukázky kódu v Pythonu, kterými se dá komunikovat s backendem.

Složka `data/` obsahuje CSV soubor s dostupnými hrami. Do databáze se data musejí přesunout ručně.

Soubor `index.html` slouží k ručnímu testování jednotlivých skriptů (nelze spouštět lokálně, viz dále).

## Použití backendu

Skripty pro provoz projektu jsou dostupné na URL http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/ pod svými jmény, viz dále.

Pro získání JSON dat je třeba použít HTTP request na dané URL (např. http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/users.php).

Ruční testování ve webovém prohlížeči lze provádět na hostované stránce [`index.html`](http://senkyr.epsilon.spstrutnov.cz/eplauncher/index.html).

## Seznam skriptů

* pro requesty typu HTTP GET, vrací JSON objekt s textovou zprávou
  - `hello.php` zpráva je obsažena pod klíčem `message`

* pro requesty typu HTTP GET, vrací JSON s polem objektů
  - `users.php` objekty reprezentují uživatele
  - `games.php` objekty reprezentují hry
  - `owned.php` objekty reprezentují transakce o nákupech her
  - `achievements.php` objekty reprezentují achievementy ve hrách
  - `achieved.php` objekty reprezentují odemčení achievementů hráči

* pro requesty typu HTTP POST, vrací JSON objekt s klíčem `vysledek`
  - `add_user.php` přidání uživatele, je třeba odeslat JSON objekt s klíči `username`, `password`
  - `check_user.php` ověření uživatele, je třeba odeslat JSON objekt s klíči `username`, `password`
  - `buy_game.php` nákup hry, je třeba odeslat JSON objekt s klíči `username`, `password`, `game_id`
  - `get_money.php` odemčení achievementu, je třeba odeslat JSON objekt s klíči `username`, `game_name`, `checksum`, `achievement`

## SQL schéma

Backend udržuje data v pěti tabulkách s následujícími sloupci:

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
* `1ep_eplauncher_achievements` přehled achievementů v jednotlivých hrách
  - `id` jednoznačný identifikátor achievementu, autoinkrementované celé číslo
  - `game_id` hra, do které achievement patří, číslo korespondující s `id` v tabulce her
  - `name` název achievementu, v každé hře smí být pouze jeden achievement s daným názvem
  - `amount` částka, která se odemčením achievementu připíše hráči na účet
* `1ep_eplauncher_achieved` přehled odemčení achievementů jednotlivými hráči
  - `id` jednoznačný identifikátor odemčení, autoinkrementované celé číslo
  - `user_id` kdo odemčení provedl, číslo korespondující s `id` v tabulce uživatelů
  - `achievement_id` který achievement byl odemčen, číslo korespondující s `id` v tabulce achievementů
  - `achieved_at` kdy k odemčení došlo, timestamp okamžiku zanesení záznamu do tabulky
