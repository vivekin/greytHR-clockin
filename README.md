# greytHR-clockin

(netsh wlan show interfaces) -match '^ *SSID*' | ForEach-Object { ($_ -split ': ')[1] }
Get-NetConnectionProfile | Select-Object Name


(netsh wlan show interfaces) -match '^ *SSID*' | ForEach-Object { ($_ -split ': ')[1] }
xyz

Get-NetConnectionProfile | Select-Object Name
Name
----
xyz


set-location 'C:\Users\xyz\Documents\greythr_auto'
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install selenium
pip install python-dateutil
python .\greythr_clock.py 'xyz' 'xyz@xyzxyz'


set-location 'C:\Users\xyz\Documents\greythr_auto'
.\venv\Scripts\Activate.ps1
python .\greythr_clock.py 'xyz' 'xyz@xyzxyz'
