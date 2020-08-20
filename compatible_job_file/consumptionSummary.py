#!/usr/bin/python
import sys

#Consumption Summary Function
#This function takes an input resultset that is ordered by courseID and videoPos, 
#and returns video consumption output in format: 
#courseID	[videoPos1:#1, videoPos2:#2, ..]


lastCourseID = None
summaryStr = ""

for line in sys.stdin:
   #strip the dataset into individual lines
   line = line.strip()

   #split the line into attributes separated by tabs
   courseID, videoPos, videoPosCount = line.split('\t')

   #if this is the first line we are executing, or 
   #if it is the same course as in the previous line
   if lastCourseID is None or lastCourseID == courseID:
      if lastCourseID == courseID:
         #if it is the same course as in the previous line, we add a comma
         summaryStr = summaryStr + ", "
   else:
      #we are done with the last course; return the courseID and its consumption summary
      summaryStr =  "[" + summaryStr + "]"
      print '\t'.join([lastCourseID, summaryStr])
      #reset summary string      
      summaryStr = ""
      
   #compose a subsection of the consumption summary string for each video position and 
   #the number of times that video position was encountered in the input
   summaryStr = summaryStr + str(videoPos) + ":" + str(videoPosCount)
   #now, remember the current course ID as our last course ID
   lastCourseID = courseID

#return the last course summary information 
#that did not get a chance to be returned in the loop above
if lastCourseID is not None:
   summaryStr =  "[" + summaryStr + "]"
   print '\t'.join([lastCourseID, summaryStr])    

