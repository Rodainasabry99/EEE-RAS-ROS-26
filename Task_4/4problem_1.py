def safe_divide():
    while True:
        try:
            x = input("Enter first number (or q to quit): ")
            if x == "q":
                break

            y = input("Enter second number: ")

            x = float(x)
            y = float(y)

            result = x / y
            print("Result:", result)

        except ZeroDivisionError:
            print("Cannot divide by zero!")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

safe_divide()