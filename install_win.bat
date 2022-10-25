pip install pyinstaller
pip install pillow
pip install pipreqs
pipreqs .
pip install -r requirements.txt
pyinstaller --paths "./millionaire" --distpath "./bin" --noconfirm --onefile --console --icon "./loim.png" --name=millionaire "./millionaire/runner.py"
set TARGET=Convert-Path .\bin\millionaire.exe
set SHORTCUT='.\Millionaire.lnk'
set WORKINGFOLDER=Convert-Path .\millionaire
set PWS=powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile
%PWS% -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut(%SHORTCUT%); $S.WorkingDirectory = %WORKINGFOLDER%; $S.TargetPath = %TARGET%; $S.Save()"