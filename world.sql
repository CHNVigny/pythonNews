CREATE TABLE `newsdata`.`world`( 
   `Title` TEXT , 
   `Description` TEXT , 
   `Date` TEXT , 
   `Source` TEXT , 
   `ImgUrl` TEXT , 
   `Url` TEXT , 
   `ID` BIGINT(20) NOT NULL AUTO_INCREMENT , 
   PRIMARY KEY (`ID`)
 )
DELETE FROM china;
DELETE FROM finance;
DELETE FROM js;
DELETE FROM social;
DELETE FROM sports;
DELETE FROM tech;
DELETE FROM test;
DELETE FROM world;