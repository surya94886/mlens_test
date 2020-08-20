spark.sql("""USE videoDB""")

# COMMAND ----------

hiveconf:fwefwefwe = dbutils.widgets.fetch('hiveconf:fwefwefwe')
spark.sql("""SELECT courseID, COUNT(DISTINCT userID) AS uniqueUserCount FROM user_course_activity GROUP BY courseID SORT BY uniqueUserCount DESC LIMIT ${hiveconf:fwefwefwe}""".format(hiveconf:fwefwefwe=hiveconf:fwefwefwe))

# COMMAND ----------

