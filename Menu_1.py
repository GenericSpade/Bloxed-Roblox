import customtkinter 
import requests
import pyautogui
import time


app = customtkinter.CTk()
app.geometry("1000x900")
app.title("Beta Menu 1")


customtkinter.set_appearance_mode("Dark")


line = customtkinter.CTkLabel(app, text=" ------------------------------------------",font=('VERDANA', 50))  # display image with a CTkLabel
line.pack()
info_head_1 = customtkinter.CTkLabel(app, text="BLOXED",font=('VERDANA', 50))  # display image with a CTkLabel
info_head_1.pack()
info_head_2 = customtkinter.CTkLabel(app, text=" BETA MENU",font=('VERDANA', 50))  # display image with a CTkLabel
info_head_2.pack()
line = customtkinter.CTkLabel(app, text=" ------------------------------------------",font=('VERDANA', 50))  # display image with a CTkLabel
line.pack()
fps_unlock_label = customtkinter.CTkLabel(app, text="state : ",font=('VERDANA', 40))  # display image with a CTkLabel
fps_unlock_label.place(x=450,y=300)
fps_unlock_label2 = customtkinter.CTkLabel(app, text="",font=('VERDANA', 40))  # display image with a CTkLabel
fps_unlock_label2.place(x=450,y=350)

def unlock_fps():
    fps_unlock_label2.configure(text= "༼ つ ◕_◕ ༽つ starting")

    def finish():
        from time import sleep
        sleep(1)
        pass
        

    try:
        from requests import get as HttpGet
        fps_unlock_label2.configure(text= "Trying")
    except:
        print("Failed to import requests module\nPlease install the \"requests\" module:\n\n---\n\npython -m install requests")
        finish()
        fps_unlock_label2.configure(text= "Failed")

    print("Fetching Roblox WindowPlayer version: https://clientsettings.roblox.com/v2/client-version/WindowsPlayer")
    VersionRequest = HttpGet("https://clientsettings.roblox.com/v2/client-version/WindowsPlayer")
    fps_unlock_label2.configure(text= "Fetching!")

    if VersionRequest:
        fps_unlock_label2.configure(text= "Starting")
        import os
        from os.path import exists as isfile
        from json import loads
        from getpass import getuser

        fps_unlock_label2.configure(text= "Workin on it!")

        RobloxVersion = loads(VersionRequest.text)["clientVersionUpload"]
        FileLocation = f"C:/Users/{getuser()}/AppData/Local/Roblox/Versions/{RobloxVersion}"
    
        if isfile(FileLocation):
            print("Roblox WindowPlayer version:", RobloxVersion)
            FileLocation += "/ClientSettings"
            fps_unlock_label2.configure(text= "Almost there")

            if not isfile(FileLocation):
                os.makedirs(FileLocation)
                print("Created ClientSettings folder", FileLocation)

            FileLocation += "/ClientAppSettings.json"
            Fps = "200"
            fps_unlock_label2.configure(text= "Setting fps")
            time.sleep(1)
            open(FileLocation, "w").write("{\"DFIntTaskSchedulerTargetFps\": " + Fps + "}")
            print("Created ClientAppSettings:", FileLocation)
            fps_unlock_label2.configure(text= "Workin On It!")
            time.sleep(1)
            fps_unlock_label2.configure(text= "(●'◡'●) done")
        else:
            print(f"You do not have the current Roblox WindowPlayer version installed {RobloxVersion}")
            fps_unlock_label2.configure(text= "You need to download roblox")
    else:
        print("Failed to fetch the current WindowPlayer Roblox version")
        fps_unlock_label2.configure(text= "Failed :()")
    finish()

fps_unlock_button = customtkinter.CTkButton(app, text="Unlock Fps", command=unlock_fps,width=400,height=100,font=('monospaced', 50))
fps_unlock_button.place(x=25,y=300)




app.mainloop()