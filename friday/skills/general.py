import pywhatkit as kit
import os 
import datetime
import pygetwindow as gw


name = "Friday"
def process_text(text):
    if "hello" in text or "hi" in text or "hey" in text:
        return "hello Venkat! How can I assist you today?"
    elif "how are you" in text:
        return "I'm doing well, thank you! How about you?"
    elif "what is your name" in text:
        return f"I am your voice assistant. You can call me {name}."
    elif "what time is it" in text or "time" in text:
        current = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current}."
    elif "what is the date" in text:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."
    elif "what day is today" in text:
        current_day = datetime.datetime.now().strftime("%A")
        return f"Today is {current_day}."

    elif "create folder" in text:
        folder = text.replace("create folder", "").strip()
        try:
            path = os.path.join(os.getcwd(), folder)
            os.mkdir(path)
            return f"Folder '{folder}' created successfully."
        except FileExistsError:
            return f"Folder '{folder}' already exists."
        except Exception as e:
            print(e)
            return "I couldn't create that folder."

    elif "play" in text or "search" in text:
        if "play" in text:
            texts = text.replace("play", "").strip()
            kit.playonyt(texts)
            return f"Playing {texts} on YouTube."
        else:
            texts = text.replace("search", "").strip()
            kit.search(texts)
            return f"Searching for {texts}."
    elif "what application am i using" in text:
        window = gw.getActiveWindow()
        if window:
            return f"You are currently using: {window.title}"
        else:
            return "I couldn't detect an active window"

    elif text.startswith("maximized"):
        try:
           app_name = text.replace("maximized", "").strip()
           for window in gw.getAllWindows():
            if app_name.lower() in window.title.lower():
                if window.isMinimized:
                    window.restore()
                    return f"maximize {app_name}"    
                    break
                else:
                    return f"{app_name} is already maximized"    
         
        except Exception as e:
            return f"An error occurred: {e}"

    elif text.startswith("minimise"):
        try:
            app_name = text.replace("minimise", "").strip()
            window = gw.getWindowsWithTitle(app_name)[0]
            if window.isMinimized:
                return f"{app_name} is already minimized"
            else:
                window.minimize()
                return f"minimize {app_name}"

        except Exception as e:
            return f"An error occurred: {e}"

    elif "close the" in text:
        try:
            app_name = text.replace("close the", "").strip()
            window = gw.getWindowsWithTitle(app_name)[0]
            if window.isActive:
                window.close()
                return f"closing {app_name}"
            else:
                return f"{app_name} is not active"
        except Exception as e:
            return f"An error occurred: {e}"

    elif "give activated window" in text:
        try:
            window = gw.getAllTitles()
            return f"Active window: {window}"
        except Exception as e:
            return f"An error occurred: {e}"

    elif "help" in text:
        try:
            help_text = """
            You can ask me to perform the following tasks:
            1. Open applications like Notepad, Calculator, Paint, Command Prompt, VS Code, Brave Browser.
            2. Close applications.
            3. Open folders like Desktop, Documents, Downloads, Videos, Pictures.
            4. Close open windows.
            5. Play videos on YouTube or search for information online.
            6. Get the current time, date, and day.
            7. Create folders in the current directory.
            8. Minimize or maximize application windows.
            9. Get the name of the currently active application window.
            """
            print(help_text)
            return "I have provided a list of tasks I can perform. Please check the console for details."
        except Exception as e:
            return f"An error occurred: {e}"
