# Keel-Keylogger-
App with GUI and backend all with python using various libraries.

Keyloggers or keystroke loggers are software programs or hardware devices that track the activities (keys pressed) of a keyboard. 
Keyloggers are a form of spyware where users are unaware their actions are being tracked. (I have not implemented this in this version of the app)

More detailed descriptions are in the raw code as comments. 

Keel.py is the main function (GUI). 
  tkinter was used here to create the GUI with Start and Stop recording buttons, a force upload button to upload the data to your email, and a delete button to delete 
  the log from the folder. 
  
main.py
  the pynput library was used to create a functon and file that will record all the inputs of the keyboard. It will ensure that special characters are deleted and 
  converted into actual readlable format. (It would save the keystrokes ie. Key.space, Key.enter)
  
sender.py
  using smtplib, and ssl, an email sender was created. It retrieves the log data from the text and sends the log to an email that was inputted in the code
  
Keel.exe
  through terminal and using pyinstaller, turned the py code into a executable and a shortcut with a custom Keel logo icon file.


TO RUN THE CODE
_________________________________________________________________________________________________________________________________________________________________________

***Make sure to have all the codes downloaded in the same folder "Keylogger" like a .exe file. 

***Place all the files into a mother Keylogger folder with everything in the rep. 
