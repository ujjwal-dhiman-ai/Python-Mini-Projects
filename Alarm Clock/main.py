from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set: (HH:MM:SS)\n")
hms = alarm_time.split(':')

a_hour = hms[0]
a_min = hms[1]
a_sec = hms[2]
print('Setting alarm for', alarm_time, '...Done')
# print(a_hour,a_min,a_sec)
print("Press CTRL + C to stop alarm.")
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S").split(':')

    c_hour = current_time[0]
    c_min = current_time[1]
    c_sec = current_time[2]
    # print(c_hour, c_min,c_sec)
    if a_hour == c_hour:
        if a_min == c_min:
            if a_sec == c_sec:
                print("Wake Up!!")
                playsound('sound.mp3')
                break
