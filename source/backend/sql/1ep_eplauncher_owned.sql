-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Počítač: localhost
-- Vytvořeno: Pát 03. kvě 2024, 12:03
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
-- Struktura tabulky `1ep_eplauncher_owned`
--

CREATE TABLE `1ep_eplauncher_owned` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  `from_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Vypisuji data pro tabulku `1ep_eplauncher_owned`
--

INSERT INTO `1ep_eplauncher_owned` (`id`, `user_id`, `game_id`, `from_date`) VALUES
(1, 1, 1, '2024-05-03 09:08:13'),
(2, 2, 2, '2024-05-03 09:08:13'),
(3, 1, 2, '2024-05-03 09:08:20');

--
-- Indexy pro exportované tabulky
--

--
-- Indexy pro tabulku `1ep_eplauncher_owned`
--
ALTER TABLE `1ep_eplauncher_owned`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pro tabulky
--

--
-- AUTO_INCREMENT pro tabulku `1ep_eplauncher_owned`
--
ALTER TABLE `1ep_eplauncher_owned`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
