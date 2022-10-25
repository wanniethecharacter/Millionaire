set TARGET=Convert-Path .\millionaire.exe
set SHORTCUT=[Environment]::GetFolderPath('Desktop') + '\Millionaire.lnk'
set PWS=powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile
set WORKINGFOLDER=Convert-Path ..\millionaire
%PWS% -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut(%SHORTCUT%); $S.WorkingDirectory = %WORKINGFOLDER%; $S.TargetPath = %TARGET%; $S.Save()"