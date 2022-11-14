/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - scholarship
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`scholarship` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `scholarship`;

/*Table structure for table `application` */

DROP TABLE IF EXISTS `application`;

CREATE TABLE `application` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sch_id` int(11) DEFAULT NULL,
  `st_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `application` */

insert  into `application`(`id`,`sch_id`,`st_id`,`date`,`status`) values 
(16,3,24,'2022-10-13','eeee'),
(17,3,20,'2022-10-13','pending');

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `course` varchar(100) DEFAULT NULL,
  `fee` bigint(20) DEFAULT NULL,
  `duration` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`cid`,`course`,`fee`,`duration`) values 
(6,'computer',20000,'3year'),
(7,'biology',4500,'2year');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`uid`,`feedback`,`date`) values 
(10,24,'hggfyfg','2022-10-13'),
(11,20,'user','2022-10-13'),
(12,24,'jijjj','2022-10-13');

/*Table structure for table `govt_scholarship` */

DROP TABLE IF EXISTS `govt_scholarship`;

CREATE TABLE `govt_scholarship` (
  `gid` int(11) NOT NULL AUTO_INCREMENT,
  `scholarship` varchar(100) DEFAULT NULL,
  `amount` bigint(20) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`gid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `govt_scholarship` */

insert  into `govt_scholarship`(`gid`,`scholarship`,`amount`,`details`,`date`) values 
(3,'egrand',750,'for all student','2022-10-12'),
(5,'dff',678,'fgxcvcxvb','2022-10-13');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(18,'admin','admin','admin'),
(19,'akhila','akhila','staff'),
(20,'nnn','nnn','student'),
(21,'stu','stu','pending'),
(22,'eee','eee','pending'),
(23,'ppp','ppp','student'),
(24,'aaa','eee','student');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`id`,`sid`,`cid`,`status`) values 
(14,20,6,'pending'),
(16,23,6,'rejected'),
(17,24,7,'confirm'),
(18,24,6,'confirm');

/*Table structure for table `scholarship` */

DROP TABLE IF EXISTS `scholarship`;

CREATE TABLE `scholarship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scholarship` varchar(30) DEFAULT NULL,
  `amount` bigint(20) DEFAULT NULL,
  `details` varchar(30) DEFAULT NULL,
  `date` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `scholarship` */

insert  into `scholarship`(`id`,`scholarship`,`amount`,`details`,`date`) values 
(3,'scholarship',800,'for malayalam student','2022-10-13');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `sf_id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `fname` varchar(29) DEFAULT NULL,
  `lname` varchar(30) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sf_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`sf_id`,`lid`,`fname`,`lname`,`gender`,`place`,`post`,`pin`,`phone`,`email`) values 
(3,19,'akhila','akathan','female','pantharangadi','pantharangadi',676306,6765676767,'aaa@gmail.com');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`id`,`lid`,`cid`,`fname`,`lname`,`gender`,`place`,`post`,`pin`,`phone`,`email`) values 
(1,20,6,'aroo','njan','male','goa','goa',787878,9867453412,'fgtrfyte@gmail.com'),
(2,21,6,'anu','ammu','female','pantharangadi','calicut',676767,8798789845,'fgtrfyte@gmail.com'),
(3,22,6,'eee','eee','female','eeee','eeee',678987,9876787678,'nnn@gmail.com'),
(4,23,6,'ppp','ppp','female','ppp','ppp',787878,9878787867,'fgtrfyte@gmail.com'),
(11,24,6,'aswin','k','male','kannur','kkk',679856,9876543212,'aswinkannur@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
