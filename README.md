# Resume Analyzer
An automated resume reviewer to analyze a federal sector resume and provide basic feedback (length, sentiment, spelling). Currently, the only supported extension for the reviewer is Word documents (.docx). The most functionality from the program can be achieved on a Windows system.

## Instructions
**READ ALL INSTRUCTIONS BEFORE BEGINNING INSTALLATION. THE INSTRUCTIONS BELOW OUTLINE THE ONLY THINGS YOU WILL NEED FOR THE REVIEWER.**

### Installation
1. Make sure you have installed the latest version of Python: https://www.python.org/downloads/release/python-380/  
    a. __Windows__: scroll down to 'Files'. Then, download and run the 'Windows x86-64 executable installer'. You should install using the recommended packages.  
    b. __macOS__: scroll down to 'Files'. Then, download and run the 'macOS 64-bit installer'  
    c. **ALL OPERATING SYSTEMS**: If you are prompted in the installer, **make sure you check 'Add Python to PATH' and 'Allow Python to bypass the maximum PATH        character limit'**
2. Download the files from this repository by clicking the green `Clone or Download` button in the top right of this page and select          `Download ZIP`.
3. Unzip the folder  
    a. __Windows__: Right click the zipped resume reviewer folder and select 'Extract All'. This will create an unzipped folder for you to        access.  
    b. __macOS__: Open the zipped resume reviewer folder, macOS will automatically create an unzipped folder. Open the unzipped folder.  
    c. **ALL OPERATING SYSTEMS**: Move the unzipped resume reviewer folder into a place where you will remember it.
4. Add any resumes to be reviewed into the `resumes` folder. The program will only detect resumes if they are inside this folder.
5. Run the reviewer  
    a. __Windows__: Double click the `reviewer.bat` file to run the resume reviewer. Windows may prevent you from running it, click 'More Info' then 'Run Anyway' to bypass the message. When you want to run the reviewer, this is the only file you will have to run.  
    b. __macOS__: Hold the 'control' key and click the `reviewer.command` file, then click 'Open' in the menu and 'Open' in the pop-up window to run the resume reviewer. The program will ask for your password (*your password will not show up when you type it in; this is normal. Just type in your password and hit 'Enter'*). When you want to run the reviewer, this is the only file you will have to run.
    
### Usage
__Windows__: Move any resumes to be reviewed into the 'resumes' folder. Double click the `reviewer.bat` file to run the reviewer. There should not be a Windows prevention window this time.
__macOS__: Move any resumes to be reviewed into the 'resumes' folder. Double click the `reviewer.command` file to run the reviewer. There should not be a macOS pop-up window this time.

## OS Support
The library that allows the page count functions to work are not supported on macOS or Linux.
If your program is not working on macOS or Linux, try using a Windows machine as the program has the most support for Windows or consider running a Windows virtual machine or dual-booting using [Bootcamp](https://support.apple.com/boot-camp).

## Development
Add any new dependencies into `requirements.txt`. They will be automatically detected by `setup.py`.  
Page count functions are dependent on macOS support for the `pywin32` library.
