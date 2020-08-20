--This Hive program creates a new table 'user_course_activity' within a new database 
--'videoDB' and loads data from input file ${hiveconf:INPUT_FILE} located in HDFS
--location ${hiveconf:HDFS_LOC} into this new table. 

--delete existing database videoDB along with cascade deleting all the tables in it,
--we want to start fresh
DROP DATABASE IF EXISTS videoDB CASCADE;

--create database videoDB 
CREATE DATABASE videoDB;

--switch to use this new database
USE videoDB;

--upload input file into HDFS - we want to start with a fresh copy of the input file every time
dfs -put ${hiveconf:INPUT_FILE} ${hiveconf:HDFS_LOC};

--delete table user_course_activity - should already be deleted during drop database, 
--statement here as extra protection.
DROP TABLE IF EXISTS user_course_activity;

--create table user_course_activity
CREATE TABLE user_course_activity (userID INT, courseID INT, videoPos INT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

--load input data from the input file in HDFS into table user_course_activity
LOAD DATA INPATH '${hiveconf:HDFS_LOC}/${hiveconf:INPUT_FILE}' OVERWRITE INTO TABLE user_course_activity;