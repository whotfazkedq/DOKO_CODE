import random

def readInt(prompt):
    while True:
        raw = input(prompt)
        try:
            return int(raw)
        except ValueError:
            print("Invalid input, enter numbers only")

def main():
    print("Random Number Generator")
    min_val = readInt("Enter the minimum value: ")
    max_val = readInt("Enter the maximum value: ")

    num = random.randint(min_val, max_val)
    print(f"Your random number is: {num}")
    while True:
        choice = input("Would you like to generate another random number? (y/n): ")
        if choice in ("y", "Y"):
            main()
            return
        elif choice in ("n", "N"):
            print("Closing")
            return
        else:
            print("Invalid choice, select yes or no")

if __name__ == "__main__":
    main()
