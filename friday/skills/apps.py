import subprocess as sp

def open_application(command):
    try:
        if "notepad" in command:
            sp.Popen("notepad.exe")
            return "Opening Notepad."
        elif "calculator" in command:
            sp.Popen("calc.exe")
            return "Opening Calculator."
        elif "paint" in command:
            sp.Popen("mspaint.exe")
            return "Opening Paint."
        elif "cmd" in command:
            sp.Popen(r"C:\WINDOWS\system32\cmd.exe")
            return "Opening Command Prompt."
        elif "vs code" in command:
            sp.Popen(r"C:\Users\VENKATESH\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd")
            return "Opening Visual Studio Code."
        elif "brave" in command:
            sp.Popen(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
            return "Opening Brave Browser."
    except Exception as e:
        print(e)


def close_application(command):
    try:
        if "notepad" in command:
            sp.run(["taskkill", "/f", "/im", "notepad.exe"])
            return "Closing Notepad."

        elif "calculator" in command:
            sp.run(["taskkill", "/f", "/im", "calc.exe"])
            return "Closing Calculator."
        elif "paint" in command:
            sp.run(["taskkill", "/f", "/im", "mspaint.exe"])
            return "Closing Paint."
        elif "cmd" in command:
            sp.run(["taskkill", "/f", "/im", r"C:\WINDOWS\system32\cmd.exe"])
            return "Closing Command Prompt."
        elif "vs code" in command:
            sp.run(["taskkill", "/f", "/im", "code.exe"])
            return "Closing Visual Studio Code."
        elif "brave" in command:
            sp.run(["taskkill", "/f", "/im", "brave.exe"])
            return "Closing Brave Browser."    
        else:
            return "Application not found."

    except Exception as e:
        print(e)
