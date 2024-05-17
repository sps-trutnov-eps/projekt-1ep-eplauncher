-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Počítač: localhost
-- Vytvořeno: Pát 17. kvě 2024, 16:14
-- Verze serveru: 10.1.48-MariaDB-0+deb9u2
-- Verze PHP: 7.3.33-1+0~20211119.91+debian9~1.gbp618351

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databáze: `ucit_senkyr`
--

-- --------------------------------------------------------

--
-- Struktura tabulky `1ep_eplauncher_games`
--

CREATE TABLE `1ep_eplauncher_games` (
  `id` int(11) NOT NULL,
  `name` varchar(120) COLLATE utf8_czech_ci NOT NULL,
  `unlock_key` varchar(255) COLLATE utf8_czech_ci NOT NULL,
  `price` int(11) NOT NULL,
  `checksum` varchar(64) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Vypisuji data pro tabulku `1ep_eplauncher_games`
--

--
-- Indexy pro exportované tabulky
--

--
-- Indexy pro tabulku `1ep_eplauncher_games`
--
ALTER TABLE `1ep_eplauncher_games`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- AUTO_INCREMENT pro tabulky
--

--
-- AUTO_INCREMENT pro tabulku `1ep_eplauncher_games`
--
ALTER TABLE `1ep_eplauncher_games`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
