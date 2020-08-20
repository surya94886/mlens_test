spark.sql("""USE videoDB""")

# COMMAND ----------

spark.sql("""DROP TABLE IF EXISTS course_activity""")

# COMMAND ----------

spark.sql("""CREATE TABLE course_activity (courseID INT, consumptionSummary STRING)ROW FORMAT DELIMITEDFIELDS TERMINATED BY '\t'""")

# COMMAND ----------

spark.sql("""ADD FILE consumptionSummary.py""")

# COMMAND ----------

spark.sql("""FROM (  SELECT courseID, videoPos, count(*) as videoPosCount FROM user_course_activity  GROUP BY courseID, videoPos  DISTRIBUTE BY courseID  SORT BY courseID ASC, videoPos ASC) outputINSERT OVERWRITE TABLE course_activitySELECT  TRANSFORM (output.courseID, output.videoPos, output.videoPosCount)  USING 'python consumptionSummary.py'  AS (courseID INT, consumptionSummary STRING)""")

# COMMAND ----------

