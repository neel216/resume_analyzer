for /d %%d in (C:\Users\%USERNAME%\AppData\Local\Programs\Python\*) do (set profile=%%d& goto break)
:break
%profile%\Scripts pip install -r requirements.txt
%profile%\python.exe setup.py
%profile%\python.exe reviewer.py