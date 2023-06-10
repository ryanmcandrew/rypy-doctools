
switch statements
=================
Introduction:

Switch statements are a popular way of handling multiple cases in programming. However, switch statements are not available in Python. But there are various ways to achieve the same functionality of switch statements in Python. In this course, we will cover some of the methods that allow us to simulate switch statements in Python 3.10.

Prerequisites:
- Python 3.10 installed on your system.

Method 1: Using If-elif statement

We can achieve the functionality of switch statements in Python using If-elif statements. Here are the steps to create a switch-like statement using If-elid statements:

Step 1: Create a dictionary that contains the cases as keys and their corresponding values as values.

Step 2: Take user input for the case, which will act as the switch case.

Step 3: Check each case in the dictionary using If-elif statements and perform the associated task.

Let's take an example, where we will switch between the weekdays and print the corresponding day's name.

Example code:

# Creating a dictionary with weekdays as keys and their name as values
weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

# Taking user input for the day
day = int(input("Enter a number between 0-6: "))

# Checking the day using If-elif statements
if day == 0:
    print("Today is", weekdays[0])
elif day == 1:
    print("Today is", weekdays[1])
elif day == 2:
    print("Today is", weekdays[2])
elif day == 3:
    print("Today is", weekdays[3])
elif day == 4:
    print("Today is", weekdays[4])
elif day == 5:
    print("Today is", weekdays[5])
elif day == 6:
    print("Today is", weekdays[6])
else:
    print("Not a valid input.")

Method 2: Using the Match statement

Python 3.10 has introduced a new way to handle multiple cases using the Match statement. The syntax of the match statement is similar to the switch statement in other programming languages. Here are the steps to create a switch-like statement using the Match statement:

Step 1: Create a function that will take the input and return the result based on the cases.

Step 2: Use the match statement in the function to handle multiple cases.

Let's take the previous example and implement it using the Match statement.

Example code:

# Defining a function that takes the day as input and returns the corresponding day of the week
def switch_cases(day: int) -> str:

    # Using the match statement to handle the cases
    case = match(day):
        case 0:
            return "Monday"
        case 1:
            return "Tuesday"
        case 2:
            return "Wednesday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"
        case _:
            return "Not a valid input."

# Taking user input for the day
day = int(input("Enter a number between 0-6: "))

# Printing the corresponding day of the week
print("Today is:", switch_cases(day))

Conclusion:

Switch statements are not supported in Python, but using If-elif statements and the new Match statement in Python 3.10, we can achieve the same functionality. Using these methods, we can handle multiple cases and execute the desired task based on user input.