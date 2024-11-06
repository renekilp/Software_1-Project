# Software 1 Course Project
![alt text](image.png)

This is the repository for the flight game project for the Software 1 course at Metropolia University of Applied Sciences' Information and Communication Technology program, created as the final project for the course. The purpose of the project was to develop a simple flight game using the Python programming language and incorporating a database.

###    Project Developers:
- Eemil Nurmi
- Rene Kilpeläinen
- Onni Kivinen
- Patrik Skogberg
## Instructions for Running the Game

- This section provides instructions for running the game from scratch. 
- If you already have the flight_game database, proceed to: (3. Required Libraries) 
- (Note!) The user and password must be 'root', and the port: 3306.
  
### 1. Downloading the MariaDB MSI package https://mariadb.org/download/
  - Run the installer with default settings.
  - Use 'root' for both 'User' and 'Password'. 
  - Set 'Port' to: 3306.

### 2. Creating the Flight Game Database in MariaDB
   1. Download the flight_game.sql file, which can be found in the "Database" folder of this repository.
   2. Open the MySQL Client (MariaDB) and enter the password 'root'.
   3. Create the database: ``` create database flight_game;```
   4. Use the database: ```use flight_game;```
   5. Run the command:  ```source C:/Users/käyttäjä/Downloads/lentopeli.sql;``` <-- (adjust the path to where you downloaded the flight_game.sql file.)

### 3. Required Libraries:
- Enter the following commands in your IDE's terminal:
- ```pip install mysql-connector```
- ```pip install colorama```
- ```pip install art```
- ```pip install geopy```
- Or download the above libraries manually from your IDE's extensions section.
 
 (If you already have a database named flight_game, go to the "Database" folder and run the Python files: ```highscore_into_database.py``` and ```KYSYMYSTAULUNLUONTI.py```.) They will add the necessary tables to the existing flight_game database for our game.)


### 4. Running the Game:
- Run the "main.py" file, which is located in the "main.game" folder.
- Enjoy the game!


## Tietokanta
#### (Kuva) Relational model of the database 
![alt text](flight_game_relation_model.png)

#### Tables: questions- and high_score added to the original database.

## Database SQL Code
##### SQL code for the database without data.

```sql
-- --------------------------------------------------------
-- Verkkotietokone:              127.0.0.1
-- Palvelinversio:               11.4.0-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Versio:              12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for taulu flight_game.airport
CREATE TABLE IF NOT EXISTS `airport` (
  `id` int(11) NOT NULL,
  `ident` varchar(40) NOT NULL,
  `type` varchar(40) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `latitude_deg` double DEFAULT NULL,
  `longitude_deg` double DEFAULT NULL,
  `elevation_ft` int(11) DEFAULT NULL,
  `continent` varchar(40) DEFAULT NULL,
  `iso_country` varchar(40) DEFAULT NULL,
  `iso_region` varchar(40) DEFAULT NULL,
  `municipality` varchar(40) DEFAULT NULL,
  `scheduled_service` varchar(40) DEFAULT NULL,
  `gps_code` varchar(40) DEFAULT NULL,
  `iata_code` varchar(40) DEFAULT NULL,
  `local_code` varchar(40) DEFAULT NULL,
  `home_link` varchar(40) DEFAULT NULL,
  `wikipedia_link` varchar(40) DEFAULT NULL,
  `keywords` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ident`),
  KEY `iso_country` (`iso_country`),
  CONSTRAINT `airport_ibfk_1` FOREIGN KEY (`iso_country`) REFERENCES `country` (`iso_country`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.country
CREATE TABLE IF NOT EXISTS `country` (
  `iso_country` varchar(40) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `continent` varchar(40) DEFAULT NULL,
  `wikipedia_link` varchar(40) DEFAULT NULL,
  `keywords` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`iso_country`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.game
CREATE TABLE IF NOT EXISTS `game` (
  `id` varchar(40) NOT NULL,
  `co2_consumed` int(8) DEFAULT NULL,
  `co2_budget` int(8) DEFAULT NULL,
  `location` varchar(10) DEFAULT NULL,
  `screen_name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `location` (`location`),
  CONSTRAINT `game_ibfk_1` FOREIGN KEY (`location`) REFERENCES `airport` (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.goal
CREATE TABLE IF NOT EXISTS `goal` (
  `id` int(11) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `icon` varchar(8) DEFAULT NULL,
  `target` varchar(40) DEFAULT NULL,
  `target_minvalue` decimal(8,2) DEFAULT NULL,
  `target_maxvalue` decimal(8,2) DEFAULT NULL,
  `target_text` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.goal_reached
CREATE TABLE IF NOT EXISTS `goal_reached` (
  `game_id` varchar(40) NOT NULL,
  `goal_id` int(11) NOT NULL,
  PRIMARY KEY (`game_id`,`goal_id`),
  KEY `goalid` (`goal_id`),
  CONSTRAINT `goal_reached_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  CONSTRAINT `goal_reached_ibfk_2` FOREIGN KEY (`goal_id`) REFERENCES `goal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.high_score
CREATE TABLE IF NOT EXISTS `high_score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `player_name` varchar(255) DEFAULT NULL,
  `player_score` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.questions
CREATE TABLE IF NOT EXISTS `questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text DEFAULT NULL,
  `correct_answer` text DEFAULT NULL,
  `wrong_answer_1` text DEFAULT NULL,
  `wrong_answer_2` text DEFAULT NULL,
  `wrong_answer_3` text DEFAULT NULL,
  `wrong_answer_4` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Tietojen vientiä ei oltu valittu.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
```
