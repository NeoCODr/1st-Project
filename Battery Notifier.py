from plyer import notification
import time
import batteryinfo as bi
from playsound3 import playsound

print("Your Application Has Started...")

prev_percent = None
notified = False

while True:
    Batter = bi.Battery()
    Battery = round(Batter.percent.value)
    Battery2 = round(Batter.percent.value, 2)
    State = Batter.state

    if prev_percent != None:
        Discharge = round(Battery2 - prev_percent, 2)
        print(Discharge)
    prev_percent = Battery2

    if Battery >= 99 and State.lower() == "charging" and notified == False:
        notified = True
        

        notification.notify(
            title='Overcharging Alert',
            message='Your Device Has Charged, Please Disconnect The Power Plug',
            timeout=9,
        )
        playsound("C:/Users/ankit/OneDrive/Desktop/python/SCRAP YARD/beep.mp3")

    if Battery < 99 and State.lower() != "charging":
        notified = False

    time.sleep(60)
