import pyttsx3

engine = pyttsx3.init()

if __name__ == '__main__':
    print("Welcome to Robo Speaker!")
    while True:
        x = input("Enter what you want to pronounce: ")
        if x.lower() == "exit":
            print("Exiting Robo Speaker. Goodbye!")
            engine.say("Exiting Robo Speaker. Goodbye!")
            break
        engine.say(x)
        engine.runAndWait()