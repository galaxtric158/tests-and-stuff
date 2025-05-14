import time
import random

def toppercentofhumans(time_taken):
    if time_taken < 0.2:
        return "in the top 5% of humans!"
    elif time_taken < 0.25:
        return "in the top 25% of humans!"
    elif time_taken < 0.3:
        return "about average compared to others."
    elif time_taken < 0.4:
        return "below average for most humans. skill issue, ngl."
    else:
        return "in the bottom 25% of humans. you're cooked. its over ngmi :C"

print("Welcome to galaxtric158's reaction time test!")

while True:

    print("When you see 'NOW!', press Enter as quickly as possible.\n")
    input("Press Enter to begin...")

    print("Get ready..")
    wait_time = random.uniform(1, 5)
    time.sleep(wait_time)

    print("NOW!")

    start_time = time.time()

    input()

    end_time = time.time()

    reaction_time = end_time - start_time
    reaction_time = round(reaction_time, 3)

    print(f"Your reaction time was {reaction_time} seconds.")
    print(f"You are {toppercentofhumans(reaction_time)}")
    input("Press Enter to start another test.\n")