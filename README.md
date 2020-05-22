# Hypixel User Lookup
Ever logged onto Hypixel and realized you were permenantly banned for no reason? Your Minecraft account may have been compromised. Use this program to check for unusual account activity.
# Installation
Just go to the 'release' tab and download the .exe file. Mac and Linux builds will come (hopefully) soon. 
# Goals
- Make an easy-to-use program for any Minecraft player without the intimidation or potential complexity of a command line
# Q&A
- Windows Smartscreen questions whether this file is safe.
  - Trust me, it is safe. Upload this to virustotal.com and the only AV that detects it is SecureAge APEX (which I can almost guarantee you've never heard of).
- How the heck am I supposed to get an API key if I'm banned?
  - Someone else can log onto the server, generate the key, and send it to you.
- Why do we need our own keys?
  - From what I read, Hypixel allows API requests every 0.5 seconds on the same key. If this program becomes frequently used and the same key was used over and over, the program will break.
- Why are you trying to help evade bans?
  - If you were violating the Hypixel rules, that's your fault. If you violated the rules but never did, you can use this to find out if your account was hacked. After getting information, you can follow the official appeal and account recovery process.
- Where is this data coming from?
  - The search is from api.hypixel.net. The huge JSON string output is the raw data.
- What tools did you use to write this?
  - I use PyCharm Professional 2020.1.
- That's a lot of files for a simple program.
  - The actual program I wrote is lookup.py. Everything else (dist, venv) was automatically generated. Let me know if some of these files aren't supposed to be here.
# Ways to Help:
Here are some things I want to get done:
- Make the source code easier to read, PEP 8 compliant, and overall more organized.
- Add proper functions (although I'd rather not create separate Python scripts).
- Find out a way to recieve output in a GUI window while making things not too complicated.
- Make fuctional Mac and Linux (preferably AppImage) binaries.
- If you're really ambitious, make a full-on GUI that isn't just PyAutoGUI prompts and alerts.