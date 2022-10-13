import random
temperature=random.randint(0,200)
humidity=random.randint(0,100)
print(temperature,humidity)
if(temperature>=100):
    print("Temperature detected is high",temperature)
    if(humidity>80):
      print("Humidity is high",humidity)
      print("Hazardous")
      print("Buzzer On")
    else:
      print("Humidity is low",humidity)
      print("Buzzer Off")
else:
    print("Temperature is in limit",temperature)
    print("Good Environment condition detected")
    
