--IMPORTANT: This Hive script assumes init.hql has been executed first. 
--This program returns the N most popular course IDs based on unique user count.
--N is provided as part of the hiveconf parameter N.

--switch to use videoDB
USE videoDB;

SELECT courseID, COUNT(DISTINCT userID) AS uniqueUserCount FROM user_course_activity GROUP BY courseID SORT BY uniqueUserCount DESC LIMIT ${hiveconf:N};