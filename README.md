# Ps1jacker
Ps1jacker is a tool for generating COM Hijacking payload.

## WARNING: This tool is still in heavy development - only one functionality is currently in testing!

### TEST 1:
This will generate a default payload that will open Calculator instead of MSPAINT. Be sure to have calc.SCT file from Examples folder within C:\tools\COM Testing\ on victim machine. Otherwise this method wont work.

`python ./ps1jacker.py -hd`

### TEST 2:
Hijacking MSPAINT.exe by specifing custom parameters.

`python ./ps1jacker.py -p "file://C:\tools\COM Testing\calc.sct" -ch {926749FA-2615-4987-8845-C33E65F2B957} -cf {00000001-0001-0001-0001-0000DEADBEEF}`


