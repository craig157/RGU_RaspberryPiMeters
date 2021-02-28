from datetime import datetime
from sense_hat import SenseHat
from SetBackground import BackColour_func as backColour
import json

#Get details from sensors
def ObtainAndDisplayData_func():
    sense = SenseHat()
    sense.clear()
    temp = sense.get_temperature() # Get Temperature from Sensor and round to 1 Decimal.
    formatTemp = round(temp,1)
    humidity = sense.get_humidity() # Get Humidity from Sensor and round to 1 Decimal. 
    formatHumidity = round(humidity,1)
    now = datetime.now() # Get Date Time Now then Split into Seperate Date and Time for Displaying
    dateOnly = now.strftime("%d/%m/%Y")
    timeOnly = now.strftime("%H:%M:%S")
    print('Temperature: ' + str(formatTemp) + '°C | Humidity: ' + str(formatHumidity) + '% | Date: ' + str(dateOnly) + ' | Time: ' + str(timeOnly)) # Test Print of what should appear on display
    backgroundColour = backColour(temp)
    fontColour = (255,255,255)
    sense.show_message('Temperature: ' + str(formatTemp) + 'C | Humidity: ' + str(formatHumidity) + '% | Date: ' + str(dateOnly) + ' | Time: ' + str(timeOnly), text_colour=fontColour, back_colour=backgroundColour) 
    sense.clear() # Clear display when finished
    
def createData_func():
    sense = SenseHat()
    sense.clear()
    temp = sense.get_temperature() # Get Temperature from Sensor and round to 1 Decimal.
    formatTemp = round(temp,1)
    humidity = sense.get_humidity() # Get Humidity from Sensor and round to 1 Decimal. 
    formatHumidity = round(humidity,1)
    x = {
        "assetId": 'RP001',
        "temperature": formatTemp,
        "humidity": formatHumidity
        }
    y = json.dumps(x)
    print(y)
    
def getTemp_func():
    sense = SenseHat()
    sense.clear()
    temp = sense.get_temperature() # Get Temperature from Sensor and round to 1 Decimal.
    formatTemp = round(temp,1)
    return formatTemp
    
def getHumidity_func():
    sense = SenseHat()
    sense.clear()
    humidity = sense.get_humidity() # Get Humidity from Sensor and round to 1 Decimal. 
    formatHumidity = round(humidity,1)
    return formatHumidity
    

