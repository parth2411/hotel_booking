-- MySQL dump 10.13  Distrib 5.7.19, for Win64 (x86_64)
--
-- Host: localhost    Database: booking
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(30) DEFAULT NULL,
  `lname` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `mobno` varchar(20) DEFAULT NULL,
  `city` varchar(40) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'hjdfg','sdvb','dfgh','dfgh','fghjk','vbn','fgh'),(2,'','','','','','',''),(3,'','','','','','',''),(4,'','','','','','',''),(5,'','','','','','',''),(6,'raj','kumar','admin@gmail.com','1234567895','Vadgaov,pune','admin','admin123'),(7,'rahul','mahale','rahulmah@gmail.com','1234567890','nahre','rahul','rahul111');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotel_id` int(11) DEFAULT NULL,
  `comment` varchar(70) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,1,'Good rooms',8),(2,3,'asdasdad',6),(3,3,'asdasdad',6),(4,1,'dsfsdf',6),(5,1,'addfffwewe',8),(6,1,'addfffwewe',8),(7,1,'fsdfsdfsf',7),(8,3,'sdfsdfsdfsdf',10),(9,3,'sdfsdfsdfsdf',9),(10,2,'asdfghjkl;',5),(11,3,'jhgsadhgasgdajsd',4),(12,3,'werwerwer',9),(13,3,'ewerwer',7),(14,1,'dasdsad',8),(15,1,'wrwerwerwer',9),(16,3,'sdfsdfsdfw',8),(17,3,'fsdfsf',6),(18,3,'sdfsdfsdf',8),(19,3,'sdsdfsdf',5),(20,3,'fgdfgdfg',7),(21,3,'',0),(22,3,'ertertert',5),(23,3,'sdfsdfsdf',0),(24,3,'dfgdfgdfg',6),(25,3,'',0),(26,3,'',0),(27,3,'rtertert',2),(28,3,'rtertert',2),(29,3,'gdgdfgdfg',8),(30,3,'dgdfgdfg',8),(31,1,'dfgdgdfgdfg',7),(32,3,'fgdfgdfgdfgdfg',8);
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotels`
--

DROP TABLE IF EXISTS `hotels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hotels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `available_rooms` int(20) DEFAULT NULL,
  `booked_rooms` int(11) DEFAULT NULL,
  `rate` float(10,2) DEFAULT NULL,
  `location` varchar(30) DEFAULT NULL,
  `rating` float(2,1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotels`
--

LOCK TABLES `hotels` WRITE;
/*!40000 ALTER TABLE `hotels` DISABLE KEYS */;
INSERT INTO `hotels` VALUES (1,'The Pride Hotel',6,10,1200.00,'pune',7.6),(2,'Hotel Sagar Plaza',0,7,2200.00,'pune',5.0),(3,'A Taj Hotel',16,13,5200.00,'pune',5.4),(4,'JW Marriott',1,2,10000.00,'Mumbai',NULL),(5,'Taj Mahal Palace',0,2,11000.00,'Mumbai',NULL);
/*!40000 ALTER TABLE `hotels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room_booking`
--

DROP TABLE IF EXISTS `room_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `room_booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cust_id` int(11) DEFAULT NULL,
  `fname` varchar(30) DEFAULT NULL,
  `lname` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `mobno` varchar(20) DEFAULT NULL,
  `checkIn` varchar(30) DEFAULT NULL,
  `checkOut` varchar(30) DEFAULT NULL,
  `hotel_id` int(20) DEFAULT NULL,
  `hotel_name` varchar(40) DEFAULT NULL,
  `hotel_city` varchar(40) DEFAULT NULL,
  `rooms` int(11) DEFAULT NULL,
  `room_type` varchar(30) DEFAULT NULL,
  `rate` float(10,2) DEFAULT NULL,
  `total` float(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_booking`
--

LOCK TABLES `room_booking` WRITE;
/*!40000 ALTER TABLE `room_booking` DISABLE KEYS */;
INSERT INTO `room_booking` VALUES (8,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Thu Sep 28 2017','Mon Sep 25 2017',NULL,'The Pride Hotel','pune',1,NULL,1200.00,2400.00),(9,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Sat Sep 30 2017','Sun Oct 1 2017',NULL,'A Taj Hotel','pune',1,NULL,5200.00,10400.00),(10,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Mon Oct 2 2017','Tue Oct 3 2017',NULL,'JW Marriott','Mumbai',2,NULL,10000.00,60000.00),(11,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Sat Sep 30 2017','Sun Oct 1 2017',NULL,'A Taj Hotel','pune',1,NULL,5200.00,5200.00),(12,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Sun Oct 1 2017','Tue Oct 3 2017',NULL,'A Taj Hotel','pune',1,NULL,5200.00,10400.00),(13,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Wed Oct 4 2017','Thu Oct 5 2017',NULL,'A Taj Hotel','pune',1,NULL,5200.00,5200.00),(14,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Sun Oct 1 2017','Mon Oct 2 2017',NULL,'Taj Mahal Palace','Mumbai',1,NULL,11000.00,11001.00),(15,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Tue Oct 3 2017','Wed Oct 4 2017',NULL,'The Pride Hotel','pune',1,NULL,1200.00,1201.00),(16,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Sat Sep 30 2017','Sun Oct 1 2017',NULL,'Hotel Sagar Plaza','pune',1,NULL,2200.00,2310.00),(17,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Tue Oct 3 2017','Wed Oct 4 2017',NULL,'Hotel Sagar Plaza','pune',1,NULL,2200.00,2310.00),(18,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Tue Oct 3 2017','Wed Oct 4 2017',NULL,'A Taj Hotel','pune',1,NULL,5200.00,7800.00),(19,7,'rahul','mahale','rahulmah@gmail.com','1234567890','Tue Oct 3 2017','Wed Oct 4 2017',NULL,'A Taj Hotel','pune',1,'Double Room',5200.00,6760.00),(45,6,'raj','kumar','admin@gmail.com','1234567895','Tue Oct 3 2017','Tue Oct 3 2017',1,'The Pride Hotel','pune',1,'Single Room',1200.00,1201.00),(46,6,'raj','kumar','admin@gmail.com','1234567895','Tue Oct 3 2017','Tue Oct 3 2017',3,'A Taj Hotel','pune',1,'Single Room',5200.00,5201.00);
/*!40000 ALTER TABLE `room_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `session` (
  `id` int(11) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `hotel_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
INSERT INTO `session` VALUES (111,'admin','admin123',3);
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-03 20:41:22
