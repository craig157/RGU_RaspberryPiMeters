#Main for Component 2
import json
import time
from GetTempAndHumidity import ObtainAndDisplayData_func as data
from GetTempAndHumidity import createData_func as createData

startTime = time.time()
interval = 30

#Takes 30 seconds to run the Message Display, so interval is 30 seconds less than required
while True:
    data() #display data on the sensehat
    createData() #create Json string of data
    time.sleep(interval - ((time.time() - startTime) % interval))
                     