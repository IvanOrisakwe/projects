-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 02, 2025 at 09:50 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `testikanta`
--

-- --------------------------------------------------------

--
-- Table structure for table `kayttajat`
--

CREATE TABLE `kayttajat` (
  `id` int(11) NOT NULL,
  `nimi` varchar(100) DEFAULT NULL,
  `ika` int(11) DEFAULT NULL,
  `sukupuoli` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `kayttajat`
--

INSERT INTO `kayttajat` (`id`, `nimi`, `ika`, `sukupuoli`) VALUES
(1, 'Aino Heikkinen', 25, 'Other'),
(2, 'Onni Virtanen', 51, 'Female'),
(3, 'Emma Salminen', 64, 'Female'),
(4, 'Sofia Heikkinen', 51, 'Other'),
(5, 'Noel Lehtinen', 35, 'Other'),
(6, 'Leo Koskinen', 27, 'Male'),
(7, 'Ella Virtanen', 53, 'Other'),
(8, 'Ella Heikkinen', 38, 'Other'),
(9, 'Veeti Hämäläinen', 60, 'Other'),
(10, 'Leo Korhonen', 24, 'Other'),
(11, 'Veeti Salminen', 56, 'Other'),
(12, 'Ella Lehtinen', 49, 'Other'),
(13, 'Ella Heinonen', 38, 'Male'),
(14, 'Oskari Järvinen', 61, 'Male'),
(15, 'Eeli Hämäläinen', 30, 'Female'),
(16, 'Noel Korhonen', 39, 'Other'),
(17, 'Eeli Nieminen', 54, 'Female'),
(18, 'Oskari Virtanen', 27, 'Other'),
(19, 'Vilma Mäkinen', 36, 'Other'),
(20, 'Veeti Mäkelä', 50, 'Female');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kayttajat`
--
ALTER TABLE `kayttajat`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kayttajat`
--
ALTER TABLE `kayttajat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
