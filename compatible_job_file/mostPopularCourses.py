spark.sql("""USE videoDB""")

# COMMAND ----------

spark.sql("""SELECT courseID, COUNT(DISTINCT userID) AS uniqueUserCount FROM user_course_activity GROUP BY courseID SORT BY uniqueUserCount DESC LIMIT ${hiveconf:fwefwefwe}""")

# COMMAND ----------

