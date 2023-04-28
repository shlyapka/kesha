import os
import webbrowser
import random


def kesha():
    a = True
    commands = {"open Opera": "C:/Program Files/Google/Chrome/Application/chrome.exe",
                "open Telegram": "C:/Users/Dima/AppData/Roaming/Telegram Desktop/Telegram.exe"}
    print("Type 'help' if you need help.")
    print("Type 'Kesha' for more information about me.")
    print("Hello, I am parrot Kesha. How can I help you?")


    while a:
        random_jokes = random.SystemRandom().choice(["Колобок повесился", "Все лежат а Игорь почему то сел и работник морга сразу поседел.", "- Ты вообще огромная умница!\n - Я толстая?!"])
        b = True
        s = input()
        if s == 'help':
            print("Type 'open App' to apen the app.\n Type 'search' to use browser.\n Type 'jokes' to read a random joke.\n Type 'exit' to quit.")
            print('Kesha is listening to you\n')
        elif s == "exit":
            a = False
            print("bye")
        elif s == "Kesha":
            print("I am parrot Kesha. I am your own assistant.\n I was created to help you use Windows 10.\n Visit to my website 'kasha.com' to find out more about my creators.")
        elif s == "stop j":
            print('Kesha is listening to you\n')
        elif s == "search":
            s = input("What do you want to search?\n")
            webbrowser.open('https://www.google.com/search?q=' + s + '&oq=cats&aqs=chrome.0.0i271j46i340i512l3j0i512j46i175i199i512l2j0i512l3.2395j0j3&sourceid=chrome&ie=UTF-8', new=2)
            print('Kesha is listening to you\n')
        elif s == "jokes":
            print(random_jokes)
            while b:
                random_jokes = random.SystemRandom().choice(
                    ["Колобок повесился", "Все лежат а Игорь почему то сел и работник морга сразу поседел.",
                     "- Ты вообще огромная умница!\n - Я толстая?!"])
                j = input("More jokes?\n")
                if j == 'yes':
                    print(random_jokes)
                else:
                    b = False
                    print('Kesha is listening to you\n')
        else:
            os.startfile(commands[s])
            print('Kesha is listening to you\n')
