import pyautogui
import time
import subprocess
import os 
import shell

print("""

     ____  _____ _____ ____   ____  ____   ___ ___    ___  ____   ______ 
    /    |/ ___// ___/|    | /    ||    \\ |   |   |  /  _]|    \\ |      |
   |  o  (   \\_(   \\_  |  | |   __||  _  || _   _ | /  [_ |  _  ||      |
   |     |\\__  |\\__  | |  | |  |  ||  |  ||  \\_/  ||    _]|  |  ||_|  |_|
   |  _  |/  \\ |/  \\ | |  | |  |_ ||  |  ||   |   ||   [_ |  |  |  |  |  
   |  |  |\\    |\\    | |  | |     ||  |  ||   |   ||     ||  |  |  |  |  
   |__|__| \\___| \\___||____||___,_||__|__||___|___||_____||__|__|  |__|  
""")
print("""
                                            __   ___   ___ ___  ____ ____  _        ___  ____  
                                           /  ] /   \\ |   |   ||    \\    || |      /  _]|    \\  
                                          /  / |     || _   _ ||  o  )  | | |     /  [_ |  D  ) 
                                         /  /  |  O  ||  \\_/  ||   _/|  | | |___ |    _]|    /  
                                        /   \\_ |     ||   |   ||  |  |  | |     ||   [_ |    \\  
                                        \\     ||     ||   |   ||  |  |  | |     ||     ||  .  \\ 
                                         \\____| \\___/ |___|___||__| |____||_____||_____||__|\\_| 
      
""")

fileOutputs = {}

# // Empty the file for the first time
with open('log.txt', 'w') as log_file:
    log_file.write("")

def getOuts(filename):

    print()
    print(" "*20,"-"*40+"OPENSHELL"+"-"*40)
    print(" "*37,"-"*20+">> "+filename+" <<"+"-"*20)
    shell.startShell(startCommand((filename)))
    print()


def printOutputs(filename , x , y):
    file = open('./output/Output.ts' , 'w')
    file.write(data[filename])
    file.close()
    time.sleep(2)
    os.system(f'start cmd /K cd output')
    time.sleep(2)
    pyautogui.write('code .')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl' , 'k')
    pyautogui.hotkey('ctrl' , 'w')
    pyautogui.hotkey('ctrl' , 'p')
    time.sleep(1)
    pyautogui.write("output.ts")
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl' , 'a')
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'shift' , 'p')
    time.sleep(1)

    pyautogui.write('codesnap')  
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(x=x , y= y + 120)

    time.sleep(1)

    pyautogui.hotkey('ctrl','c')
    time.sleep(2)

    titles = pyautogui.getAllTitles()
    for title in titles:
        if 'Word' in title:
            docTitle = title
            break
    doc =  pyautogui.getWindowsWithTitle(docTitle)[0] 
    doc.activate()
    time.sleep(2)
    doc.activate()

    pyautogui.hotkey('ctrl','end')
    pyautogui.write(f"{filename.split('.')[0]} Output : ")
    pyautogui.hotkey('enter')

    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl' , 'return')
    time.sleep(2)

    subprocess.call("TASKKILL /F /IM cmd.exe", shell=True)
    subprocess.call("TASKKILL /F /IM Code.exe", shell=True)


files = []
fileType = input("Enter the file extension you want to work with...! (java , py , other(output not supported)): ")
saveImages = input("Save images along with Document pasting ? \n1 for Sure \n2/* for Nah \nType : ")
if(saveImages == 1): saveImages = True
else: saveImages = False
getOutputs = input("Outputs required ? \n1/* for Sure \n2 for Nah \n Default(TRUE) Type : ")
if(getOutputs != 2): getOutputs = True
else: getOutputs = False

directory = os.fsencode("./files")
def startCommand(filename):
    if fileType == "py":
        startcmd = f"python {filename}"
    elif fileType == "java":
        startcmd = f"javac {filename} && java { filename.split(".")[0]}"
    return startcmd

acceptableOuts = ["java" , "py"]
if(fileType in acceptableOuts):
    print(""" Instructions:
          1) to rerun a file type (rerun)
          2) to move to the next file type exit
          3) wait for the output before typing.
""")
    print()

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(f".{fileType}"): 
        files.append(filename)
        if(fileType in acceptableOuts):

            getOuts(filename)

    # ///////////////// READ DATA FROM LOG AND STORE IN VARIABLE
if(fileType in acceptableOuts):
    file = open("log.txt" , "r")
    dataTemp = file.read().split(f"{"--"*20}FILE{"--"*20}")
    data = {k: v for k, v in zip(files, dataTemp)}
    file.close()

# //////////////////////////////////////////////////////////////////////////////////////////////////////// 
# //////////////////////////////////////////////////////////////////////////////////////////////////////// 
# /////////////    MAIN SCRIPT
x = -1
y = -1
print(files , 'files')
def script():
    firstTime = True

    for index ,filename in enumerate(files):
        subprocess.call("TASKKILL /F /IM cmd.exe", shell=True)
        subprocess.call("TASKKILL /F /IM Code.exe", shell=True)

        if filename == "script.py": continue

        os.system(f'start cmd /K "cd files && code {filename}"')
        time.sleep(3)
        pyautogui.hotkey('ctrl','a')
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'shift' , 'p')
        time.sleep(1)
        pyautogui.write('codesnap')  
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.hotkey('ctrl','a')
        time.sleep(1)

        if(firstTime == True):
            pyautogui.alert('To get location of snap button. \nDrive the mouse to the location of the snap button(Rainbow looking). DO NOT CLICK THE BUTTON. And keep the mouse steady on the button for a while.!', button='GOTIT') 
            newX = -2
            newY = -2
            while True:
                X, Y = pyautogui.position()
                if(newX == X and newY == Y):
                    x = newX
                    y = newY
                    break
                newX = X
                newY = Y
                time.sleep(2)

        pyautogui.click(x=x , y= y + 120)
        time.sleep(2)

        pyautogui.hotkey('ctrl','c')
        time.sleep(3)
        if firstTime:
                try:
                    subprocess.call('powershell.exe Unblock-File -Path ./template.docx ; exit', shell=True)
                    time.sleep(1)
                    os.startfile("template.docx")
                except:
                    pyautogui.alert("Template file not found..! will create new file", "souka(autoclose in 2s)" , timeout="2000")
                    f = open("template.docx", "x")
                    time.sleep(1)
                    subprocess.call('powershell.exe Unblock-File -Path ./template.docx  ; exit', shell=True)
                    time.sleep(1)
                    f.close()
                    os.startfile("template.docx")
                    
                time.sleep(2)

        titles = pyautogui.getAllTitles()
        docTitle = ''
        for title in titles:
            if 'Word' in title:
                docTitle = title
                break
        doc =  pyautogui.getWindowsWithTitle(docTitle)[0] 
        doc.activate()

        pyautogui.hotkey('ctrl','end')
        pyautogui.write(f"{filename.split('.')[0]}")
        pyautogui.hotkey('enter')

        pyautogui.hotkey('ctrl','v')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('ctrl' , 'return')
        time.sleep(2)

        vscodeTitle = ''
        if( saveImages == True) :
            for title in titles:
                if 'Visual Studio Code' in title:
                    vscodeTitle = title
                    break
            doc = pyautogui.getWindowsWithTitle(vscodeTitle)[0]
            doc.activate()
            time.sleep(1)
            pyautogui.click(x=x , y= y)
            time.sleep(2)
            pyautogui.write(filename.split('.')[0])

            if firstTime: 
                time.sleep(1)
                pyautogui.alert('Select the directory where you want your files...! 10s windows for the first time..!',timeout="5000") 
                time.sleep(10)
            else: 
                time.sleep(3)

            pyautogui.press('enter')
            time.sleep(2)


        subprocess.call("TASKKILL /F /IM cmd.exe", shell=True)
        subprocess.call("TASKKILL /F /IM Code.exe", shell=True)
        if (fileType in acceptableOuts):
            printOutputs(filename , x , y)
        if firstTime: firstTime = False
        
script()
pyautogui.sleep(5)
subprocess.call("TASKKILL /F /IM cmd.exe", shell=True)
subprocess.call("TASKKILL /F /IM Code.exe", shell=True)