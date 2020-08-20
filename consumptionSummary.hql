--IMPORTANT: This Hive script assumes init.hql has been executed first. 
--This program, using a Python UDF, transforms the userID-courseID-videoPos based
--input data into courseID-consumptionSummary based output data, 
--which is then stored in new table 'course_activity'.

--switch to use videoDB
USE videoDB;

--delete table course_activity - should already be deleted during init.hql, 
--statement here as extra protection.
DROP TABLE IF EXISTS course_activity;

--create table course_activity that will contain the output of this program
CREATE TABLE course_activity (courseID INT, consumptionSummary STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

--add Python UDF 'consumptionSummary.py' that generates a consumption summary for each course
ADD FILE consumptionSummary.py;

--using the output of a select query that returns 
--the number of videoPositions for each courseID and videoPosition pair, and
--through a UDF, generate course activity data and store it in table course_activity  
FROM (
  SELECT courseID, videoPos, count(*) as videoPosCount FROM user_course_activity
  GROUP BY courseID, videoPos
  DISTRIBUTE BY courseID
  SORT BY courseID ASC, videoPos ASC) output
INSERT OVERWRITE TABLE course_activity
SELECT
  TRANSFORM (output.courseID, output.videoPos, output.videoPosCount)
  USING 'python consumptionSummary.py'
  AS (courseID INT, consumptionSummary STRING);

--NOTE: REMOVING THE SELECT STATEMENT BELOW FROM THIS FILE AND ADDING IT AS ANOTHER HIVE CALL INSTEAD: 
--SELECT * FROM course_activity > output.tsv
--REASON:I WAS GETTING UNWANTED 'Deleted /user/hive/warehouse/videodb.db/course_activity' LOG STATEMENT IN THE OUTPUT FILE WHEN MAKING THE FOLLOWING HIVE CALL:
--hive -f consumptionSummary.hql > output.tsv 
--HOWEVER, WE WANT THE OUTPUT FILE TO ONLY CONTAIN THE COURSEID-CONSUMPTIONSUMMARY INFORMATION.

--return the consumption summary resultset [SEE NOTE ABOVE]
--SELECT * FROM course_activity;