# RGU_RaspberryPiMeters
Project for obtaining sensor reads from Raspberry Pi

Main Script:
  =Displays data on SenseHAT
  =Creates data in a JSON String
  
PublishAws.py:
  =Using the functions created in the other files, will publish the data to Dynamo DB 
  
Test_Subscribe.py (in AWS Folder):
  =This can be ran to obtain the data being sent to Dynamo DB in parralel to the database updating (for testing)
  
Analytics Dashboard (Qlikview)
  =Requires Qlikview12 
