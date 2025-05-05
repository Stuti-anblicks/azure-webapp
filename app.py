# Simple Voting App in Python

# Initialize vote counts
votes = {'Option 1': 0, 'Option 2': 0, 'Option 3': 0}

def display_results():
    print("\nCurrent Vote Counts:")
    for option, count in votes.items():
        print(f"{option}: {count}")

def vote():
    while True:
        print("\nVote for your favorite option:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. View results")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            votes['Option 1'] += 1
            print("You voted for Option 1.")
        elif choice == "2":
            votes['Option 2'] += 1
            print("You voted for Option 2.")
        elif choice == "3":
            votes['Option 3'] += 1
            print("You voted for Option 3.")
        elif choice == "4":
            display_results()
        elif choice == "5":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    vote()
