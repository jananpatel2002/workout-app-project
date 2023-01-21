from workouts import workouts_dict  # imports the dictionary (workouts) from workouts.py

sName = input("What is your name?").title()

try:
    sChoice = input("Would you like to workout today? ").lower()  # Gets the input for the yes or no
    if sChoice == 'yes':
        for category in workouts_dict:
            print(category.title())
        category = input("What workout category would you like to do? ").lower()
        exercises = workouts_dict[category]

except KeyError:
    print("Workouts for this section is unavailable for our application ")

else:
    for exercise in exercises:
        print(exercise)

# if sChoice != " Yes" and sChoice != " yes" and sChoice != " No" and sChoice != " no":
# print("Enter yes or no to continue.")
# exit()
