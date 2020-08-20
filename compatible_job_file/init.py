spark.sql("""DROP DATABASE IF EXISTS videoDB CASCADE""")

# COMMAND ----------

spark.sql("""CREATE DATABASE videoDB""")

# COMMAND ----------

spark.sql("""USE videoDB""")

# COMMAND ----------

spark.sql("""dfs -put ${hiveconf:INPUT_FILE} ${hiveconf:HDFS_LOC}""")

# COMMAND ----------

spark.sql("""DROP TABLE IF EXISTS user_course_activity""")

# COMMAND ----------

spark.sql("""CREATE TABLE user_course_activity (userID INT, courseID INT, videoPos INT)ROW FORMAT DELIMITEDFIELDS TERMINATED BY '\t'STORED AS TEXTFILE""")

# COMMAND ----------

spark.sql("""LOAD DATA INPATH '${hiveconf:HDFS_LOC}/${hiveconf:INPUT_FILE}' OVERWRITE INTO TABLE user_course_activity""")

# COMMAND ----------

