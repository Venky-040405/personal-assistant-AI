import os

def file_manager_open(command):
    for folder in Folders:
        if folder in command:
            try:
                folder_path = os.path.join(os.path.expanduser("~"), folder)
                os.startfile(folder_path)
                return f"Opening {folder} folder."
            except Exception as e:
                return f"An error occurred: {e}"
        
    return "I couldn't recognize the folder you want to open."

def file_manager_close(command):
    try:
        window = gw.getWindowsWithTitle(command)
        if window:
            window[0].close()
            return f"Closing {command} window."
        else:
            return "I couldn't find that window open."
    except Exception as e:
        print(e)       