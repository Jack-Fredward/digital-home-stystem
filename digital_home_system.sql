-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: digital_home_database
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

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
-- Table structure for table `Actuators`
--

DROP TABLE IF EXISTS `Actuators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Actuators` (
  `A_ID` int(11) NOT NULL AUTO_INCREMENT,
  `D_ID` int(11) DEFAULT NULL,
  `State` int(11) NOT NULL,
  `LUT` datetime DEFAULT NULL,
  `A_Name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`A_ID`),
  KEY `Actuators_FK` (`D_ID`),
  CONSTRAINT `Actuators_FK` FOREIGN KEY (`D_ID`) REFERENCES `Devices` (`D_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actuators`
--

LOCK TABLES `Actuators` WRITE;
/*!40000 ALTER TABLE `Actuators` DISABLE KEYS */;
INSERT INTO `Actuators` VALUES (49,82,0,'2020-10-07 15:27:35','Oven Actuator'),(50,84,0,'2020-10-07 15:27:35','Burner1 Actuator'),(51,84,0,'2020-10-07 15:27:35','Burner2 Actuator'),(52,84,0,'2020-10-07 15:27:35','Burner3 Actuator'),(53,84,0,'2020-10-07 15:27:35','Burner4 Actuator');
/*!40000 ALTER TABLE `Actuators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BrightnessSensor`
--

DROP TABLE IF EXISTS `BrightnessSensor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BrightnessSensor` (
  `BS_ID` int(11) NOT NULL AUTO_INCREMENT,
  `D_ID` int(11) DEFAULT NULL,
  `BS_Name` varchar(100) DEFAULT NULL,
  `BrightnessPct` float DEFAULT NULL,
  PRIMARY KEY (`BS_ID`),
  KEY `BrightnessSensor_FK` (`D_ID`),
  CONSTRAINT `BrightnessSensor_FK` FOREIGN KEY (`D_ID`) REFERENCES `Devices` (`D_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BrightnessSensor`
--

LOCK TABLES `BrightnessSensor` WRITE;
/*!40000 ALTER TABLE `BrightnessSensor` DISABLE KEYS */;
/*!40000 ALTER TABLE `BrightnessSensor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Devices`
--

DROP TABLE IF EXISTS `Devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Devices` (
  `D_ID` int(11) NOT NULL AUTO_INCREMENT,
  `D_Name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`D_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Devices`
--

LOCK TABLES `Devices` WRITE;
/*!40000 ALTER TABLE `Devices` DISABLE KEYS */;
INSERT INTO `Devices` VALUES (82,'Oven'),(83,'Fridge'),(84,'Stove');
/*!40000 ALTER TABLE `Devices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LiquidFlowSensors`
--

DROP TABLE IF EXISTS `LiquidFlowSensors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LiquidFlowSensors` (
  `LFS_ID` int(11) NOT NULL AUTO_INCREMENT,
  `D_ID` int(11) DEFAULT NULL,
  `LFS_Name` varchar(100) DEFAULT NULL,
  `FlowRatePct` float DEFAULT NULL,
  PRIMARY KEY (`LFS_ID`),
  KEY `LiquidFlowSensors_FK` (`D_ID`),
  CONSTRAINT `LiquidFlowSensors_FK` FOREIGN KEY (`D_ID`) REFERENCES `Devices` (`D_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LiquidFlowSensors`
--

LOCK TABLES `LiquidFlowSensors` WRITE;
/*!40000 ALTER TABLE `LiquidFlowSensors` DISABLE KEYS */;
/*!40000 ALTER TABLE `LiquidFlowSensors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MotionSensors`
--

DROP TABLE IF EXISTS `MotionSensors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MotionSensors` (
  `MS_ID` int(11) NOT NULL AUTO_INCREMENT,
  `D_ID` int(11) DEFAULT NULL,
  `MS_Name` varchar(100) DEFAULT NULL,
  `Is_Motion` int(11) DEFAULT NULL,
  PRIMARY KEY (`MS_ID`),
  KEY `MotionSensors_FK` (`D_ID`),
  CONSTRAINT `MotionSensors_FK` FOREIGN KEY (`D_ID`) REFERENCES `Devices` (`D_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MotionSensors`
--

LOCK TABLES `MotionSensors` WRITE;
/*!40000 ALTER TABLE `MotionSensors` DISABLE KEYS */;
/*!40000 ALTER TABLE `MotionSensors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OpenCloseSensors`
--

DROP TABLE IF EXISTS `OpenCloseSensors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OpenCloseSensors` (
  `OCS_ID` int(11) NOT NULL AUTO_INCREMENT,
  `D_ID` int(11) DEFAULT NULL,
  `OCS_Name` varchar(100) DEFAULT NULL,
  `State` int(11) DEFAULT NULL,
  PRIMARY KEY (`OCS_ID`),
  KEY `OpenCloseSensors_FK` (`D_ID`),
  CONSTRAINT `OpenCloseSensors_FK` FOREIGN KEY (`D_ID`) REFERENCES `Devices` (`D_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COMMENT='For things that have two states a 1 state and a 0 state(on/off, open/close, etc)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OpenCloseSensors`
--

LOCK TABLES `OpenCloseSensors` WRITE;
/*!40000 ALTER TABLE `OpenCloseSensors` DISABLE KEYS */;
INSERT INTO `OpenCloseSensors` VALUES (5,83,'Fridge Door OCS',0);
/*!40000 ALTER TABLE `OpenCloseSensors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TempSensors`
--

DROP TABLE IF EXISTS `TempSensors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TempSensors` (
  `TS_ID` int(11) NOT NULL AUTO_INCREMENT,
  `D_ID` int(11) DEFAULT NULL,
  `TS_Name` varchar(100) DEFAULT NULL,
  `Temp` float DEFAULT NULL,
  PRIMARY KEY (`TS_ID`),
  KEY `TempSensors_FK` (`D_ID`),
  CONSTRAINT `TempSensors_FK` FOREIGN KEY (`D_ID`) REFERENCES `Devices` (`D_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TempSensors`
--

LOCK TABLES `TempSensors` WRITE;
/*!40000 ALTER TABLE `TempSensors` DISABLE KEYS */;
INSERT INTO `TempSensors` VALUES (11,82,'OTS1',0),(12,83,'FTS1',0),(13,84,'STS1',0),(14,84,'STS2',0),(15,84,'STS3',0),(16,84,'STS4',0);
/*!40000 ALTER TABLE `TempSensors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `U_ID` int(11) NOT NULL AUTO_INCREMENT,
  `F_Name` varchar(100) DEFAULT NULL,
  `L_Name` varchar(100) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Is_Disabled` int(11) NOT NULL,
  `Is_SU` int(11) NOT NULL,
  PRIMARY KEY (`U_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'Steve','Wright',76,1,0),(2,'Mini','Wright',72,0,0),(3,'Stanely','Wright',47,0,1),(4,'Vinni','Wright',42,0,0),(5,'Michelle','Wright',18,0,0),(6,'Robert','Wright',16,0,0);
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-07 15:39:01
