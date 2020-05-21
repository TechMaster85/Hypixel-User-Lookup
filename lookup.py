import datetime as dt
import pyautogui as pag
import requests

try:
    f = open("apikey.txt", "r")

except FileNotFoundError:
    api_key = pag.prompt(text="Enter your Hypixel API key. You can get it from typing [/api new] in Hypixel chat.",
                         title="API Key")
    pag.alert(text="We will now test your connection.")
    data = requests.get(f"https://api.hypixel.net/player?key={api_key}&name=TechMaster85").json()

    if data['success']:
        f = open("apikey.txt", "w+")
        f.write(api_key)
        f.close()
        f = open("apikey.txt", "r")
        pag.alert(text="It worked! Let's go! Your API key is now saved to apikey.txt.")

    else:
        pag.alert(text="That didn't work. Check your Internet connection and check your key for errors.")

api_key = f.read()

player_name = pag.prompt(text="Enter the name of the player you want to look up.", title="Player Entry")
data = requests.get(f"https://api.hypixel.net/player?key={api_key}&name={player_name}").json()

pag.alert(text="Request received. Check the command line for output.\n")

if data['player']:
    print(data)
    print()

    print(f"{player_name}'s most recent login was at "
          f"{dt.datetime.fromtimestamp(data['player']['lastLogin'] / 1000)} in your timezone.")

    print(f"The last time {player_name} logged out was at "
          f"{dt.datetime.fromtimestamp(data['player']['lastLogout'] / 1000)}.")

    print("\nIf you weren't logged on at these times, change your Minecraft password IMMEDIATELY.")
    print("Thanks for using this program! Have a great day! Press enter to exit.")
    input()

elif not data['success']:
    print("Your data can't be found. Delete apikey.txt and restart the program.")

else:
    print("The name you entered is not valid. Please restart and try again.")
