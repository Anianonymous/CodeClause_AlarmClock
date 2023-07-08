from tkinter import *
import time
from playsound import playsound


def check_alarm():
    alarm_hour = int(entry_hour.get())
    alarm_minute = int(entry_minute.get())

    current_time = time.strftime("%H:%M")
    if alarm_hour == int(time.strftime("%H")) and alarm_minute == int(time.strftime("%M")):
        print("Playing")
        playsound("C:\\Users\\hegde\\Downloads\\Alarm.mp3")


root = Tk()
root.geometry('300x500')
root.resizable(False, False)
root.title("Alarm Clock")
root.configure(bg="blue")
# Create labels
Label(root,text="Alarm Clock",font ='a 20 bold',bg='blue',fg='yellow').place(x=70)
label_hour = Label(root, text="Hour:",font='a 10 bold')
label_hour.place(x=130,y=60)
entry_hour = Entry()
entry_hour.place(x=85,y=90)

label_minute = Label(root, text="Minute:",font='a 10 bold')
label_minute.place(x=120,y=130)
entry_minute = Entry(root)
entry_minute.place(x=85,y=160)

# Create a button to set the alarm
button_set = Button(root, text="Set Alarm", command=check_alarm,fg='white',bg='green')
button_set.place(x=115,y=190)

root.mainloop()
