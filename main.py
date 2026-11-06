print("       ====== MYSTERY ISLAND =======")
print("Any player that wakes up on an island must light the beacon")
name = input("Enter your name: ")
print(f"{name} you are welcome! ")
print("A beach is a dry land close to or in line with an ocean, river or sea")
print("1. Look around")
print("2. Go to Jungle")
print("3. Quit.")
choice = input("choose from option (1-3): ").strip().lower()
if choice == "1":
    print("Dry sand, sunny afternoon, waves")
elif choice == "2":
    print("Head into the jungle")
elif choice == "3":
    print("Goodbye")
else:
    print("choose from option (1-3)")