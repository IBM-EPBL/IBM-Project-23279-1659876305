from gpiozero import LED,Button,TrafficLights,Buzzer
from time import sleep
buzzer=Buzzer(15)
button = Button(21)    
lights = TrafficLights(25, 8, 7)    
led=LED(16)
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    button.wait_for_press()   
    buzzer.on()   
    light.green.on()    
    sleep(1)    
    lights.yellow.on()    
    sleep(1)    
    lights.red.on()    
    sleep(1)    
    lights.off()   
    buzzer.off()  