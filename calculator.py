print("CALCULATOR")  # The below prints on screen calculation options to choose from
print("1. add two values")
print("2. subtract two values")
print("3. Multiply two values")
print("4. Divide two values")
print("0. Quit")
text = input("Enter one of the options (0-4): ")

# The while loop allows to iterate the calculator options if the user doesn't opt for 0 (i.e. to quit)
while text != "0":
    # This allows to proceed with the calculator options as long as the user enters a value between 1 and 4
    if text in ["1", "2", "3", "4"]:
        numOne = float(input("Enter first number: "))
        numTwo = float(input("Enter second number: "))

        if text == "1":
            sumOfVals = numOne + numTwo
            print("The sum is ", sumOfVals)

        elif text == "2":
            subtraction = numOne - numTwo
            print("The result is ", subtraction)

        elif text == "3":
            multiplication = numOne * numTwo
            print("The result is ", multiplication)

        elif text == "4":
            division = numOne / numTwo
            print("The result is ", division)

    else:
        # This shows on screen if the user enters a value other than 1, 2, 3 or 4.
        print("Option entered invalid.")

    # This reiterates the prompt to enter an option
    text = input("Enter one of the options (0-4): ")

print("Quitting... Goodbye!")  # This prints when the user opts for 0
