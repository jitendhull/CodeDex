import random

# Player stats and game state
health = 100
has_key = False
escaped = False
max_turns = 7
turn = 1
potion_used = False
monster_defeated = False
secret_code = str(random.randint(1, 3))

# Start screen
print("Welcome to Escape the Dark Castle!")
name = input("What is your name, brave adventurer? \n > ")
print(f"Hello, {name}! Your quest is to escape the dark castle. Good luck!")

# Story intro
print("You wake up in a dimly lit dungeon. The air is damp and you can hear distant screams.")
print("You must escape before sunrise, or the dark forces will find you!")

# Small countdown using a for loop
print("Sunrise is coming in...")
for count in range(3, 0, -1):
    print(count)
print("Move quickly!\n")

# Main game loop
while turn <= max_turns and health > 0 and not escaped:
    print(f"\n--- Turn {turn}/{max_turns} ---")
    print(f"Health: {health}")
    print(f"Key found: {'Yes' if has_key else 'No'}")
    print("Choose your action:")
    print("1. Enter the rusty iron door (monster room)")
    print("2. Enter the wooden door (treasure room)")
    print("3. Enter the stone door (escape room)")
    print("4. Search the dungeon corners")
    print("5. Rest for a moment")
    choice = input("> ").strip()

    if choice == "1":
        if monster_defeated:
            print("The monster room is now empty. You already defeated it.")
        else:
            print("A giant monster attacks you!")
            fight_choice = input("Do you want to fight? (yes/no) > ").strip().lower()
            if fight_choice == "yes":
                result = random.randint(1, 2)
                if result == 1:
                    print("You bravely fight and win! You found a key.")
                    has_key = True
                    monster_defeated = True
                    health -= 15
                else:
                    print("The monster injures you badly. You escape, but hurt.")
                    health -= 35
            elif fight_choice == "no":
                print("You run away in fear and lose some energy.")
                health -= 5
            else:
                print("Invalid answer. The monster scratches you while you hesitate.")
                health -= 10

    elif choice == "2":
        if not potion_used:
            heal = random.randint(20, 35)
            print(f"You find a glowing potion and recover {heal} health.")
            health += heal
            potion_used = True
        else:
            print("The treasure room is empty now. You trip on a broken chest.")
            health -= 10

    elif choice == "3":
        print("You enter the stone room. A chest blocks the final gate.")
        if has_key:
            print("You use the key, but a tiny number lock remains (1 to 3).")
            attempts = 0
            unlocked = False

            # Unlock mini-game using a while loop
            while attempts < 3 and not unlocked:
                guess = input("Guess the secret number (1/2/3): ").strip()
                if guess == secret_code:
                    unlocked = True
                else:
                    attempts += 1
                    if attempts < 3:
                        print("Wrong guess. Try again.")

            if unlocked:
                print("The lock opens! You found the escape map.")
                escaped = True
            else:
                print("The lock shocks you after 3 failed tries.")
                health -= 20
        else:
            print("The chest is locked. You need to find the key first.")

    elif choice == "4":
        print("You search carefully...")
        places = ["under old bones", "inside a cracked wall", "behind a dusty shelf"]
        found_something = False

        # Simple exploration loop
        for place in places:
            print(f"- You look {place}.")
            if not has_key and random.randint(1, 6) == 3:
                print("  You found a small rusty key!")
                has_key = True
                found_something = True

        if not found_something:
            print("You found nothing useful this time.")

    elif choice == "5":
        print("You take a deep breath and regain a little strength.")
        health += 5

    else:
        print("Invalid choice. You wasted time.")

    # Keep health in a clean range
    if health > 120:
        health = 120

    if health <= 0:
        break

    turn += 1

# Ending
print("\n===== Final Result =====")
if escaped and health > 0:
    print(f"Congratulations, {name}! You escaped the dark castle with {health} health left!")
elif health <= 0:
    print(f"{name}, your journey ends in the castle shadows. Game Over.")
else:
    print(f"Sunrise has arrived, {name}. You ran out of time. Game Over.")