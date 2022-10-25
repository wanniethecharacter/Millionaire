set TARGET=Convert-Path .\millionaire.exe
set SHORTCUT=[Environment]::GetFolderPath('Desktop') + '\Millionaire.lnk'
set PWS=powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile

%PWS% -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut(%SHORTCUT%); $S.TargetPath = %TARGET%; $S.Save()"