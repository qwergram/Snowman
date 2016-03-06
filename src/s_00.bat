@echo off
D:\src\app\Python.exe D:\src\util.py
echo CLOVER V20
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\MICROSOFT\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\MICROSOFT\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowAllTrustedApps" /d "1"
D:\src\app\Python.exe "D:\src\s_01.py"
D:\src\app\Python.exe "D:\src\s_02.py"
D:\src\app\Python.exe "D:\src\s_03.py"
D:\src\app\Python.exe "D:\src\s_04.py"
D:\src\app\Python.exe "D:\src\s_05.py"
D:\src\app\Python.exe "D:\src\s_06.py"
powershell -ExecutionPolicy Bypass "D:\App\Add-AppDevPackage.ps1" -action install -bypass true -section all
D:\src\app\Python.exe "D:\src\s_07.py"
D:\src\app\Python.exe "D:\src\s_08.py"
D:\src\app\Python.exe "D:\src\s_09.py"
D:\src\app\Python.exe "D:\src\s_10.py"
pause
