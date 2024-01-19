import customtkinter 
import requests
import psutil
import subprocess
import pyautogui
import time



app = customtkinter.CTk()
app.geometry("1000x900")
app.title("Bloxed Info")

customtkinter.set_appearance_mode("Dark")

def main_menu():
    pass

line = customtkinter.CTkLabel(app, text=" ------------------------------------------",font=('VERDANA', 50))  # display image with a CTkLabel
line.pack()
info_head_1 = customtkinter.CTkLabel(app, text="BLOXED",font=('VERDANA', 50))  # display image with a CTkLabel
info_head_1.pack()
info_head_2 = customtkinter.CTkLabel(app, text=" UPDATES AND INFO",font=('VERDANA', 50))  # display image with a CTkLabel
info_head_2.pack()
line = customtkinter.CTkLabel(app, text=" ------------------------------------------",font=('VERDANA', 50))  # display image with a CTkLabel
line.pack()
info_1 = customtkinter.CTkLabel(app, text="🫡 - This is the first version of the app",font=('monospaced', 50))  # display image with a CTkLabel
info_1.pack(pady=10,padx=10)
info_2= customtkinter.CTkLabel(app, text="🪲 - There might be a lot of bugs",font=('monospaced', 50))  # display image with a CTkLabel
info_2.pack(pady=10,padx=10)
info_3= customtkinter.CTkLabel(app, text="📜Scripter: @daniel_generic on instagram",font=('monospaced', 50))  # display image with a CTkLabel
info_3.pack(pady=10,padx=10)
info_4= customtkinter.CTkLabel(app, text="🆓 - This is the free BETA! version",font=('monospaced', 50))  # display image with a CTkLabel
info_4.pack(pady=10,padx=10)


def delete_all_widgets():
    for widget in app.winfo_children():
        widget.destroy() # Destroy all child widgets within the app

    """ """
    # =========================== #
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
    fps_unlock_label2 = customtkinter.CTkLabel(app, text="---",font=('VERDANA', 40))  # display image with a CTkLabel
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
                Fps = "450"
                fps_unlock_label2.configure(text= "Setting fps")
                time.sleep(1)
                open(FileLocation, "w").write("{\"DFIntTaskSchedulerTargetFps\": " + Fps + "}")
                print("Created ClientAppSettings:", FileLocation)
                fps_unlock_label2.configure(text= "Workin On It!")
                time.sleep(1)
                fps_unlock_label2.configure(text= "(●'◡'●) done")
            else:
                print(f"You do not have the current Roblox WindowPlayer version installed {RobloxVersion}")
                fps_unlock_label2.configure(text= "Download Roblox ⚠️")
        else:
            print("Failed to fetch the current WindowPlayer Roblox version")
            fps_unlock_label2.configure(text= "Failed :()")
        finish()

    fps_unlock_button = customtkinter.CTkButton(app, text="Unlock Fps", command=unlock_fps,width=400,height=100,font=('monospaced', 50))
    fps_unlock_button.place(x=25,y=300)

    def lag_reduction_strategy():
        reduce_lag_label2.configure(text= "Starting 🫡")
        try:
            reduce_lag_label2.configure(text= "Roblox Not Open ⚠️")
            for process in psutil.process_iter(['pid', 'name']):
                if 'RobloxPlayerBeta.exe' in process.info['name']:
                    roblox_pid = process.info['pid']
                    subprocess.run(["wmic", "process", "where", f"processid={roblox_pid}", "setpriority", "64"])
                    reduce_lag_label2.configure(text= "Done ☆*: .｡. o(≧▽≦)o .｡.:*☆")
                    time.sleep(60)
                    subprocess.run(["wmic", "process", "where", f"processid={roblox_pid}", "setpriority", "32"])
                    reduce_lag_label2.configure(text= "Done (^///^)")
        except Exception as e:
            pass 


    reduce_lag_button = customtkinter.CTkButton(app, text="Boost Gameplay", command=lag_reduction_strategy,width=400,height=100,font=('monospaced', 50))
    reduce_lag_button.place(x=25,y=450)
    reduce_lag_label = customtkinter.CTkLabel(app, text="state : ",font=('VERDANA', 40))  # display image with a CTkLabel
    reduce_lag_label.place(x=450,y=450)
    reduce_lag_label2 = customtkinter.CTkLabel(app, text="---",font=('VERDANA', 40))  # display image with a CTkLabel
    reduce_lag_label2.place(x=450,y=500)

    coming_soon = customtkinter.CTkLabel(app, text="MORE COMING SOON",font=('VERDANA', 60))  # display image with a CTkLabel
    coming_soon.place(x=225,y=600)
     # =========================== #
    
    

info_button = customtkinter.CTkButton(app, text="Start!",command=delete_all_widgets,width=500,height=100,font=('monospaced', 50))
info_button.pack(pady=120,padx=10)


app.mainloop() 