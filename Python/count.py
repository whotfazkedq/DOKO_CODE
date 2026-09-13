import random
import time

times_reached = 0
max_objectives = int(input("Enter the maximum number of objectives to reach: "))
while True:
    objective_time = random.randint(1, 10)
    counter = 0

    print(f"New Objective: {objective_time} seconds")

    while counter < objective_time:
        print(f"Counter: {counter} seconds")
        time.sleep(1)
        counter += 1

    times_reached += 1
    print(f"Objective time reached, {times_reached} times\n")
    if times_reached >= max_objectives:
        print(f"Objective time reached, {max_objectives} times")
        break