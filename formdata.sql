CREATE DATABASE IF NOT EXISTS `flasklogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE IF NOT EXISTS `accounts` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
      `username` varchar(50) NOT NULL,
      `password` varchar(255) NOT NULL,
      `email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

USE `flasklogin`;
CREATE TABLE IF NOT EXISTS `formdata2` (
`firstname` varchar(100) NOT NULL,
`lastname` varchar(100) NOT NULL,
`address` varchar(500) NOT NULL,
`city` varchar(100) NOT NULL,
`zipcode` varchar(40) NOT NULL,
`country` varchar(80) NOT NULL,
`email` varchar(100) NOT NULL,
`phone` varchar(20) NOT NULL,
`highschool` varchar(500) NOT NULL,
`inter` varchar(500) NOT NULL,
`undergrad` varchar(500) NOT NULL,
`grad` varchar(500) NOT NULL,
`others`  varchar(1000) NOT NULL,
`experience`  varchar(2000) NOT NULL,
`skills`  varchar(2000) NOT NULL,
`interest`  varchar(2000) NOT NULL,
`summary`  varchar(2000) NOT NULL,
 PRIMARY KEY (`email`)
 )ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

USE `flasklogin`;
CREATE TABLE IF NOT EXISTS `feedback1` (
`comment` varchar(1000) NOT NULL,
PRIMARY KEY (`comment`)
) DEFAULT CHARSET=utf8;



