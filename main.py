from workouts import workouts_dict  # imports the dictionary (workouts) from workouts.py

workout_str = ""

print("Hello! Welcome to Gym Bro! This is a program designed to help you find a workout routine. \n")
name = input("What is your name? ").title()

try:
    choice = input("\nWould you like to workout today? ").lower()  # Gets the input for the yes or no
    if choice == 'yes':

        for exercise_type in workouts_dict:
            workout_str += exercise_type.title() + ", "
        workout_str = workout_str[:-2]
        print(f"\n{workout_str}")
        category = input(f"Welcome {name}! What workout category would you like to do from the list above? ").lower()
        exercises = workouts_dict[category]
    else:
        print("Have a nice day!")
        exit()

except KeyError:
    print("Workouts for this section is unavailable for our application ")

else:
    for exercise in exercises:
        print(f"\n{exercise}")

# if sChoice != " Yes" and sChoice != " yes" and sChoice != " No" and sChoice != " no":
# print("Enter yes or no to continue.")
# exit()
