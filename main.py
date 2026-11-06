print("====== MYSTERY ISLAND ======")
print("You wake up on an island after a storm. Light the beacon to be rescued.")

name = input("Enter your name: ").strip()
print(f"Welcome, {name}!")

print("You stand on a beach. The lighthouse is dark in the distance.")

running = True
while running:
    print("\n1. Look around")
    print("2. Go to Jungle")
    print("3. Quit")
    choice = input("Choose an option (1-3): ").strip().lower()

    if choice == "1":
        print("Dry sand, a sunny afternoon, and waves.")
    elif choice == "2":
        print("You head into the jungle...")
    elif choice == "3":
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice. Please enter 1, 2 or 3.")