spark.sql("""USE videoDB""")

# COMMAND ----------

hiveconf = dbutils.widgets.fetch('hiveconf')
spark.sql("""SELECT courseID, COUNT(DISTINCT userID) AS uniqueUserCount FROM user_course_activity GROUP BY courseID SORT BY uniqueUserCount DESC LIMIT ${hiveconf}""".format(hiveconf=hiveconf))

# COMMAND ----------

