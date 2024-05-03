-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Počítač: localhost
-- Vytvořeno: Pát 03. kvě 2024, 12:51
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
-- Struktura tabulky `1ep_eplauncher_users`
--

CREATE TABLE `1ep_eplauncher_users` (
  `id` int(11) NOT NULL,
  `username` varchar(60) COLLATE utf8_czech_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_czech_ci NOT NULL,
  `money` int(11) NOT NULL DEFAULT '50'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Vypisuji data pro tabulku `1ep_eplauncher_users`
--

INSERT INTO `1ep_eplauncher_users` (`id`, `username`, `password`, `money`) VALUES
(1, 'user1', '$2a$12$mMYc1OA2Q.RnU0awGOQN4.Ew26//dvaJ96Q6VxqugLB0pdJnFuOBO', 50),
(2, 'user2', '$2a$12$mMYc1OA2Q.RnU0awGOQN4.Ew26//dvaJ96Q6VxqugLB0pdJnFuOBO', 50);

--
-- Indexy pro exportované tabulky
--

--
-- Indexy pro tabulku `1ep_eplauncher_users`
--
ALTER TABLE `1ep_eplauncher_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT pro tabulky
--

--
-- AUTO_INCREMENT pro tabulku `1ep_eplauncher_users`
--
ALTER TABLE `1ep_eplauncher_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
