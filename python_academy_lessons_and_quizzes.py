# ==========================================================
# PYTHON ACADEMY
# LESSON + TUTORIAL + QUIZ PROGRAM
# Prelims: 15 questions | Midterms: 15 questions | Finals: 15 questions
# Beginner-friendly: print, input, if/elif/else, nested if, and loops
# ==========================================================

while True:
    print("\n==============================================")
    print("              PYTHON ACADEMY")
    print("==============================================")
    print("[1] PRELIMS - Lesson and Quiz")
    print("[2] MIDTERMS - Lesson and Quiz")
    print("[3] FINALS - Lesson and Quiz")
    print("[4] EXIT")

    choice = input("\nChoose a lesson: ")

    # ======================================================
    # PRELIMS LESSON
    # ======================================================
    if choice == "1":
        print("\n==============================================")
        print("                 PRELIMS")
        print("             PYTHON BASICS")
        print("==============================================")

        print("\nLESSON 1: What is Programming?")
        print("Programming means giving instructions to a computer.")
        print("A programming language lets people write those instructions.")
        print("Python is a popular, beginner-friendly programming language.")
        print("Python was created by Guido van Rossum and first released in 1991.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 2: Python and Code Editors")
        print("You can write and run Python using tools such as:")
        print("- IDLE: Python's basic development environment")
        print("- VS Code: A code editor that supports Python")
        print("- PyCharm: An IDE used for Python development")
        print("- Jupyter Notebook: A tool for running code in cells")
        print("You need Python installed or an online Python environment.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 3: print() and Comments")
        print("The print() command displays information on the screen.")
        print('Example: print("Hello, World!")')
        print("A comment explains code and is ignored by Python.")
        print("Use # to write a single-line comment.")
        print('Example: # This is a comment')
        input("\nPress ENTER to continue...")

        print("\nLESSON 4: Variables and Constants")
        print("A variable stores a value that a program can use.")
        print('Example: name = "Alex"')
        print("The variable name stores the text Alex.")
        print("A variable name cannot begin with a number.")
        print("Use letters, numbers, and underscores; do not use spaces.")
        print("Python does not have a special constant keyword.")
        print("By convention, constant names are written in UPPERCASE.")
        print("Example: SCHOOL_NAME = 'Python Academy'")
        input("\nPress ENTER to continue...")

        print("\nLESSON 5: Basic Data Types")
        print("int   - whole numbers, such as 10")
        print("float - decimal numbers, such as 3.14")
        print("str   - text, such as 'Hello'")
        print("bool  - True or False")
        print("Use type(value) to check a value's data type.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 6: Arithmetic Operators")
        print("+  addition       Example: 5 + 2 = 7")
        print("-  subtraction    Example: 5 - 2 = 3")
        print("*  multiplication Example: 5 * 2 = 10")
        print("/  division       Example: 5 / 2 = 2.5")
        print("// floor division Example: 5 // 2 = 2")
        print("%  remainder      Example: 5 % 2 = 1")
        print("** exponent        Example: 2 ** 3 = 8")
        input("\nPress ENTER to continue...")

        print("\nLESSON 7: input() and Type Conversion")
        print("input() receives information typed by the user.")
        print('Example: name = input("Enter your name: ")')
        print("input() gives text (a string), even when the user types a number.")
        print("Use int() to convert to a whole number.")
        print("Use float() to convert to a decimal number.")
        print('Example: age = int(input("Enter age: "))')
        input("\nPress ENTER to continue...")

        print("\nLESSON 8: Output Formatting")
        print("An f-string lets you place variable values inside text.")
        print('Example: name = "Alex"')
        print('         print(f"Hello, {name}!")')
        print("The output will be: Hello, Alex!")
        print("Remember: Python is case-sensitive and indentation matters.")
        input("\nYou have finished the Prelims lesson. Press ENTER to start the quiz...")

        score = 0
        print("\n============= PRELIMS QUIZ =============")

        for question in range(1, 16):
            print("\nQuestion", question)

            if question == 1:
                print("What is Python?")
                print("A. A programming language")
                print("B. An operating system")
                print("C. A computer part")
                print("D. A web browser")
                answer = "A"
            elif question == 2:
                print("Who created Python?")
                print("A. Bill Gates")
                print("B. Guido van Rossum")
                print("C. Steve Jobs")
                print("D. Dennis Ritchie")
                answer = "B"
            elif question == 3:
                print("In what year was Python first released?")
                print("A. 1985")
                print("B. 1995")
                print("C. 1991")
                print("D. 2000")
                answer = "C"
            elif question == 4:
                print("Which command displays output?")
                print("A. input()")
                print("B. show()")
                print("C. display()")
                print("D. print()")
                answer = "D"
            elif question == 5:
                print("Which symbol starts a single-line comment?")
                print("A. #")
                print("B. //")
                print("C. <!--")
                print("D. **")
                answer = "A"
            elif question == 6:
                print("Python is a ______ language.")
                print("A. Case-insensitive")
                print("B. Case-sensitive")
                print("C. Machine-only")
                print("D. Markup")
                answer = "B"
            elif question == 7:
                print("Which is a valid variable name?")
                print("A. 2name")
                print("B. my-name")
                print("C. my_name")
                print("D. my name")
                answer = "C"
            elif question == 8:
                print("Which data type stores whole numbers?")
                print("A. str")
                print("B. float")
                print("C. bool")
                print("D. int")
                answer = "D"
            elif question == 9:
                print("Which data type stores text?")
                print("A. str")
                print("B. int")
                print("C. float")
                print("D. bool")
                answer = "A"
            elif question == 10:
                print("Which data type stores decimal numbers?")
                print("A. int")
                print("B. float")
                print("C. str")
                print("D. bool")
                answer = "B"
            elif question == 11:
                print("What is the result of 10 + 5?")
                print("A. 50")
                print("B. 15")
                print("C. 5")
                print("D. 105")
                answer = "B"
            elif question == 12:
                print("Which operator is used for multiplication?")
                print("A. +")
                print("B. /")
                print("C. *")
                print("D. -")
                answer = "C"
            elif question == 13:
                print("Which command gets information from the user?")
                print("A. print()")
                print("B. input()")
                print("C. type()")
                print("D. int()")
                answer = "B"
            elif question == 14:
                print("What does int('5') do?")
                print("A. Converts text to an integer")
                print("B. Converts a number to text")
                print("C. Prints 5")
                print("D. Deletes the value")
                answer = "A"
            else:
                print("What is indentation in Python?")
                print("A. A type of variable")
                print("B. A way to add comments")
                print("C. Spaces at the beginning of a code line")
                print("D. A mathematical operator")
                answer = "C"

            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer == answer:
                print("Correct!")
                score = score + 1
            else:
                print("Incorrect. The correct answer is", answer)

        print("\n============= PRELIMS RESULT =============")
        print("Your score:", score, "/ 15")
        if score >= 12:
            print("Excellent work!")
        elif score >= 9:
            print("Good job! Keep practicing.")
        else:
            print("Keep studying. Review the lesson and try again!")

    # ======================================================
    # MIDTERMS LESSON
    # ======================================================
    elif choice == "2":
        print("\n==============================================")
        print("                 MIDTERMS")
        print("          CONDITIONAL STATEMENTS")
        print("==============================================")

        print("\nLESSON 1: What are Conditional Statements?")
        print("Conditional statements allow a program to make decisions.")
        print("Python checks whether a condition is True or False.")
        print("The code inside a matching condition is then executed.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 2: The if Statement")
        print("Use if when you want code to run only when a condition is True.")
        print("Example:")
        print("age = 18")
        print("if age >= 18:")
        print("    print('You are an adult.')")
        print("The colon starts the block, and indentation marks the block.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 3: if-else Statement")
        print("Use else for the alternative when the if condition is False.")
        print("Example:")
        print("if score >= 75:")
        print("    print('Passed')")
        print("else:")
        print("    print('Failed')")
        input("\nPress ENTER to continue...")

        print("\nLESSON 4: if-elif-else Statement")
        print("Use elif to check another condition.")
        print("Example:")
        print("if grade >= 90:")
        print("    print('Excellent')")
        print("elif grade >= 75:")
        print("    print('Passed')")
        print("else:")
        print("    print('Failed')")
        input("\nPress ENTER to continue...")

        print("\nLESSON 5: Relational Operators")
        print("==  equal to")
        print("!=  not equal to")
        print(">   greater than")
        print("<   less than")
        print(">=  greater than or equal to")
        print("<=  less than or equal to")
        print("Remember: = assigns a value, while == compares two values.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 6: Logical Operators")
        print("and - True only when BOTH conditions are True.")
        print("or  - True when AT LEAST ONE condition is True.")
        print("not - Reverses a Boolean result.")
        print("Example: if age >= 18 and has_id == True:")
        print("             print('You may enter.')")
        input("\nPress ENTER to continue...")

        print("\nLESSON 7: Nested if Statements")
        print("A nested if is an if statement inside another if statement.")
        print("Example:")
        print("if age >= 18:")
        print("    if has_id == True:")
        print("        print('Access granted')")
        print("    else:")
        print("        print('ID required')")
        print("else:")
        print("    print('You are too young')")
        print("The inner if is checked only when the outer if is True.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 8: Boolean Values and Indentation")
        print("A Boolean value is either True or False.")
        print("Conditions produce Boolean results.")
        print("Indentation shows which statements belong to an if or else.")
        print("Use consistent indentation, commonly four spaces.")
        input("\nYou have finished the Midterms lesson. Press ENTER to start the quiz...")

        score = 0
        print("\n============= MIDTERMS QUIZ =============")

        for question in range(1, 16):
            print("\nQuestion", question)

            if question == 1:
                print("Which statement is used to make a decision?")
                print("A. if")
                print("B. print")
                print("C. input")
                print("D. import")
                answer = "A"
            elif question == 2:
                print("Which statement runs when the if condition is False?")
                print("A. for")
                print("B. else")
                print("C. while")
                print("D. input")
                answer = "B"
            elif question == 3:
                print("Which keyword checks another condition?")
                print("A. break")
                print("B. continue")
                print("C. elif")
                print("D. return")
                answer = "C"
            elif question == 4:
                print("Which operator means equal to?")
                print("A. =")
                print("B. !=")
                print("C. >")
                print("D. ==")
                answer = "D"
            elif question == 5:
                print("Which operator means not equal to?")
                print("A. !=")
                print("B. ==")
                print("C. =")
                print("D. >=")
                answer = "A"
            elif question == 6:
                print("What does > mean?")
                print("A. Less than")
                print("B. Greater than")
                print("C. Equal to")
                print("D. Not equal to")
                answer = "B"
            elif question == 7:
                print("What does <= mean?")
                print("A. Greater than")
                print("B. Equal only")
                print("C. Less than or equal to")
                print("D. Not equal to")
                answer = "C"
            elif question == 8:
                print("Which logical operator requires both conditions to be True?")
                print("A. or")
                print("B. not")
                print("C. if")
                print("D. and")
                answer = "D"
            elif question == 9:
                print("Which logical operator needs at least one condition to be True?")
                print("A. or")
                print("B. and")
                print("C. not")
                print("D. ==")
                answer = "A"
            elif question == 10:
                print("What does the not operator do?")
                print("A. Adds two values")
                print("B. Reverses a Boolean result")
                print("C. Repeats a loop")
                print("D. Displays output")
                answer = "B"
            elif question == 11:
                print("What is the result of 5 > 3?")
                print("A. False")
                print("B. 0")
                print("C. True")
                print("D. None")
                answer = "C"
            elif question == 12:
                print("Which data type has only True or False values?")
                print("A. int")
                print("B. str")
                print("C. float")
                print("D. bool")
                answer = "D"
            elif question == 13:
                print("What is a nested if statement?")
                print("A. An if statement inside another if statement")
                print("B. An if statement without a condition")
                print("C. A loop inside print()")
                print("D. A comment")
                answer = "A"
            elif question == 14:
                print("What happens if an if condition is True?")
                print("A. The program always stops")
                print("B. The indented block runs")
                print("C. The program deletes a variable")
                print("D. The condition becomes a string")
                answer = "B"
            else:
                print("Which symbol starts a conditional block in Python?")
                print("A. ;")
                print("B. ,")
                print("C. :")
                print("D. #")
                answer = "C"

            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer == answer:
                print("Correct!")
                score = score + 1
            else:
                print("Incorrect. The correct answer is", answer)

        print("\n============= MIDTERMS RESULT =============")
        print("Your score:", score, "/ 15")
        if score >= 12:
            print("Excellent work!")
        elif score >= 9:
            print("Good job! Keep practicing.")
        else:
            print("Keep studying. Review the lesson and try again!")

    # ======================================================
    # FINALS LESSON
    # ======================================================
    elif choice == "3":
        print("\n==============================================")
        print("                  FINALS")
        print("             LOOPS / ITERATION")
        print("==============================================")

        print("\nLESSON 1: What is Iteration?")
        print("Iteration means repeating a set of instructions.")
        print("Loops help avoid writing the same code many times.")
        print("Python has for loops and while loops.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 2: The for Loop")
        print("A for loop repeats code for each item in a sequence.")
        print("Example:")
        print("for number in range(5):")
        print("    print(number)")
        print("This displays 0, 1, 2, 3, and 4.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 3: The range() Function")
        print("range(5) produces numbers from 0 up to, but not including, 5.")
        print("range(1, 6) produces 1, 2, 3, 4, 5.")
        print("range(2, 11, 2) produces 2, 4, 6, 8, 10.")
        print("The third value is the step or interval.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 4: The while Loop")
        print("A while loop repeats as long as its condition is True.")
        print("Example:")
        print("count = 1")
        print("while count <= 3:")
        print("    print(count)")
        print("    count = count + 1")
        print("The counter changes so the condition eventually becomes False.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 5: while True")
        print("while True creates a loop whose condition is always True.")
        print("It keeps repeating until you stop it, often with break.")
        print("Example:")
        print("while True:")
        print("    choice = input('Type exit to stop: ')")
        print("    if choice == 'exit':")
        print("        break")
        input("\nPress ENTER to continue...")

        print("\nLESSON 6: break and continue")
        print("break immediately ends the loop.")
        print("continue skips the rest of the current repetition")
        print("and moves to the next repetition.")
        input("\nPress ENTER to continue...")

        print("\nLESSON 7: Loop Counters and Indentation")
        print("A counter variable keeps track of repetitions.")
        print("Example: count = count + 1 increases count by one.")
        print("Statements inside a loop must be indented.")
        print("Be careful: a loop that never reaches a stopping condition")
        print("can become an infinite loop.")
        input("\nYou have finished the Finals lesson. Press ENTER to start the quiz...")

        score = 0
        print("\n============= FINALS QUIZ =============")

        for question in range(1, 16):
            print("\nQuestion", question)

            if question == 1:
                print("What is a loop used for?")
                print("A. Repeating code")
                print("B. Deleting code")
                print("C. Creating a comment")
                print("D. Renaming Python")
                answer = "A"
            elif question == 2:
                print("Which loop is commonly used when the number of repetitions is known?")
                print("A. if")
                print("B. for")
                print("C. else")
                print("D. elif")
                answer = "B"
            elif question == 3:
                print("Which loop repeats while a condition is True?")
                print("A. for")
                print("B. if")
                print("C. while")
                print("D. print")
                answer = "C"
            elif question == 4:
                print("What numbers are produced by range(5)?")
                print("A. 1, 2, 3, 4, 5")
                print("B. 0, 1, 2, 3, 4, 5")
                print("C. 5 only")
                print("D. 0, 1, 2, 3, 4")
                answer = "D"
            elif question == 5:
                print("How many times does for x in range(3) repeat?")
                print("A. 3 times")
                print("B. 2 times")
                print("C. 4 times")
                print("D. 1 time")
                answer = "A"
            elif question == 6:
                print("Which keyword immediately exits a loop?")
                print("A. pass")
                print("B. break")
                print("C. continue")
                print("D. stop")
                answer = "B"
            elif question == 7:
                print("Which keyword skips to the next loop repetition?")
                print("A. break")
                print("B. exit")
                print("C. continue")
                print("D. skip")
                answer = "C"
            elif question == 8:
                print("What does while True create?")
                print("A. A condition that is always False")
                print("B. A one-time statement")
                print("C. A variable")
                print("D. A loop that continues until it is stopped")
                answer = "D"
            elif question == 9:
                print("Which keyword can stop a while True loop?")
                print("A. break")
                print("B. print")
                print("C. input")
                print("D. int")
                answer = "A"
            elif question == 10:
                print("What is an infinite loop?")
                print("A. A loop that runs once")
                print("B. A loop that does not stop on its own")
                print("C. A loop with no code")
                print("D. A loop that always gives an error")
                answer = "B"
            elif question == 11:
                print("What numbers are produced by range(1, 6)?")
                print("A. 0 to 6")
                print("B. 1 to 6")
                print("C. 1 to 5")
                print("D. 2 to 6")
                answer = "C"
            elif question == 12:
                print("Where is the code placed inside a loop?")
                print("A. Before the program")
                print("B. Inside quotation marks")
                print("C. After the loop ends only")
                print("D. In an indented block")
                answer = "D"
            elif question == 13:
                print("What happens if a while condition becomes False?")
                print("A. The loop stops")
                print("B. The loop repeats forever")
                print("C. Python restarts")
                print("D. The condition becomes True")
                answer = "A"
            elif question == 14:
                print("Which loop is useful for going through each item in a sequence?")
                print("A. while True")
                print("B. for")
                print("C. if")
                print("D. else")
                answer = "B"
            else:
                print("What is the purpose of a counter variable in a loop?")
                print("A. To display pictures")
                print("B. To create comments")
                print("C. To keep track of repetitions")
                print("D. To change Python's name")
                answer = "C"

            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer == answer:
                print("Correct!")
                score = score + 1
            else:
                print("Incorrect. The correct answer is", answer)

        print("\n============= FINALS RESULT =============")
        print("Your score:", score, "/ 15")
        if score >= 12:
            print("Excellent work!")
        elif score >= 9:
            print("Good job! Keep practicing.")
        else:
            print("Keep studying. Review the lesson and try again!")

    elif choice == "4":
        print("\nThank you for using Python Academy!")
        break

    else:
        print("\nInvalid choice. Please choose 1, 2, 3, or 4.")
        continue

    print("\nWhat would you like to do next?")
    print("[1] Return to main menu")
    print("[2] Exit")
    next_choice = input("Choose: ")

    if next_choice == "2":
        print("\nThank you for studying with Python Academy!")
        break
    elif next_choice == "1":
        print("\nReturning to the main menu...")
    else:
        print("\nInvalid choice. Returning to the main menu...")
