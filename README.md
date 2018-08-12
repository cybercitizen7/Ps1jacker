# Ps1jacker
Ps1jacker is a tool for generating COM Hijacking payload.
COM Hijacking is a method of getting Remote Code Execution by using legitimiate Windows process'. For example, when you start MSPAINT.exe it will trigger several registry keys / directories in your registry. These are specified by CLSID (ClassID). Some of these CLSID do not even exist on your machine, which opens up an opportunity for attacker. The attacker will find that unique non-existing CLSID and hijack it, by adding it to Registry and trigger his/her own script once that CLSID is called by MSPAINT.exe. 

## WARNING: This tool is still in heavy development - only one functionality is currently in testing!

### TEST 1:
This will generate a default payload that will open Calculator instead of MSPAINT. Be sure to have calc.SCT file from Examples folder within C:\tools\COM Testing\ on victim machine. Otherwise this method wont work.

`python ./ps1jacker.py -hd`

### TEST 2:
Hijacking MSPAINT.exe by specifing custom parameters.

`python ./ps1jacker.py -p "file://C:\tools\COM Testing\calc.sct" -ch {926749FA-2615-4987-8845-C33E65F2B957} -cf {00000001-0001-0001-0001-0000DEADBEEF}`


