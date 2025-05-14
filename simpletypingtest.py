import time
import random

try:
    with open(r"phrases.txt", "r") as file:
        phrases = file.read().splitlines()
except FileNotFoundError:
    print("\n")
    print("Error: 'phrases.txt' not found. Make sure it's in the same folder as this script.")
    print("Using local list for phrases instead.")
    phrases = ["programming is such a tedious task",
                "tests are a terrible thing",
                "coding in python is super fun",
                "roblox games are made using lua",
                "hey thats quite a mean thing to say",
                "the quick brown fox jumps over the lazy dog",
                "coding coding coding",]
    print("\n")

text_to_type = random.choice(phrases)

print("welcome to galax's simple typing speed test!")

while True:
    print("Type the following sentence exactly as it appears:\n")
    print(f">>> {text_to_type}\n")  # newline char
    checkend = input("Press enter when you're ready. ")

    for i in range(3):
        print(i + 1)
        time.sleep(1)

    start_time = time.time()
    user_input = input("\nStart typing:\n")  # newline
    end_time = time.time()

    timetaken = end_time - start_time
    words = len(text_to_type.split())
    speed = words / (timetaken / 60)  # words per minute

    if user_input == text_to_type:
        print("\nYou typed it correctly.")
    else:
        print("\nThere were some mistakes.")
        print("Phrase:", text_to_type)
        print("You typed:", user_input)

    speed = round(speed, 1)
    timetaken = round(timetaken, 1)

    print(f"\nTime taken: {timetaken} seconds")
    print(f"Typing speed: {speed} WPM (Words Per Minute)")
    input("Press enter for the next random phrase.")
    text_to_type = random.choice(phrases)  # new phrase for next round
