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
    while True:
        min_val = readInt("Enter the minimum value: ")
        max_val = readInt("Enter the maximum value: ")

        while min_val > max_val:
            print("minimum can't be higher than maximum, try again: ")
            min_val = readInt("Enter the minimum value: ")
            max_val = readInt("Enter the maximum value: ")

        count = readInt("How many numbers do you want to generate?: ")
        while count <= 0:
            count = readInt("You can't select negative options, try again: ")

        nums = [random.randint(min_val, max_val) for _ in range(count)]
        print("Your random numbers are: ", nums)

        choice = input("Would you like to generate more numbers? (y/n): ").strip().lower()
        if choice not in ("y", "Y"):
            break

        print("Closing")
if __name__ == "__main__":
    main()