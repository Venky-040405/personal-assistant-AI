#speech to text import
from friday.io.stt import Recognize, calibrate_microphone

#tts import
from friday.io.tts import speak

#open application, close application import
from friday.skills.apps import open_application, close_application

#general skills import
from friday.skills.general import process_text

#file manager import
from friday.skills.files import file_manager_open

#traceback import
import traceback
from friday.skills.Routines import Daily_routine, battery_status, cpu, memory




name = "Friday"
def respond(reply):
    if reply:
        print(f"Friday: {reply}")
        speak(reply)


def main():
    respond(f"Hello, sir {name} is ready")
    calibrate_microphone()
    while True:
        try:
            commands = Recognize()
            print(commands)
            if "friday" in commands:
                command = commands.replace("friday","").strip()
                print(f"You said:{command}")
                if command == "exit":
                    respond("Exiting the program.")
                    break
                elif command.startswith("open"):
                    commands = command.replace("open","").strip()
                    respond(open_application(commands))   
                elif "close" in command:
                    commands = command.replace("close","").strip()    
                    respond(close_application(commands))
                elif command.startswith("folder"):
                    commands = command.replace("folder","").strip()
                    respond(file_manager_open(commands))
                elif command.startswith("start coding mode"):
                    commands = command.replace("start coding mode","").strip()
                    respond(Daily_routine())    
                elif command.startswith("battery status"):
                    commands = command.replace("battery status","").strip()
                    respond(battery_status())
                elif command.startswith("cpu usage"): 
                    commands = command.replace("cpu usage","").strip()
                    respond(cpu())
                elif command.startswith("memory usage"):
                    commands = command.replace("memory usage","").strip()
                    respond(memory())
                else:
                    respond(process_text(command))

        except KeyboardInterrupt:
            respond("good bye.")
            exit()

        except Exception as e:
            traceback.print_exc()
            print(e)


if __name__ == "__main__":
    main()


""" elif command.startswith("closes"):
    commands = command.replace("closes","").strip()
    file_manager_close(commands) """

       