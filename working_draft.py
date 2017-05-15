# ---------------
# MENU FUNCTIONS
# ---------------


#global variables

user_created_haiku = ["sunny", "sunnyday", "sunnydaze"]
user_generated_haiku = []


# Main Menu

def main_menu():
    """Print a menu and asks the user to make a choice.

    Arguments:
    None
    Returns:
    int: the user's menu choice
    """
    user_options = """
    \n
    1 -- Introduction
    2 -- Generate a haiku
    3 -- Create my own haiku
    4 -- See all haikus
    5 -- Exit
    """

    print user_options
    choice = int(raw_input('Choose from the menu options: '))
    execute_main_menu(choice)


def execute_main_menu(choice):

    while True:
        choice = (raw_input(choice))
        if choice == '1':
            # introduction
            introduction()

        elif choice == "2":
            print "Okay! Let's begin!"
            begin_questionaire()
            # call function here to prompt series of questions to generate

        elif choice == "3":
            print "here ya go"
            # call function here to allow user to create own haiku

        elif choice == "4":
            # Displays user generated and created haikus
            display_all_haikus()

        elif choice == "5":
            # Exits program
            break

        else:
            print "Please select an option from 1-5."

        return

def introduction():
    # Brief introduction of what a Haiku is and how to create one

    print "A haiku is a poem with 3 lines that contains 5, 7 and 5 syllables respectively"
    user_input_go_back = raw_input("Press 0 to return to main menu >>>")

    if user_input_go_back == "0":
        main_menu()

    return

def begin_questionaire():
    print "\nQuestion here\n"
    print "A) _____"
    print "B) ______"
    print "C) ______"
    print "D) _______\n"
    question_1_input = str(raw_input("Which selection best fits you? >>").lower())
    return question_1_input
    question1_repl(question_1_input)

def display_all_haikus():
    # displays all of the haikus that the user has generated or created
    print "Haikus that you wrote:"
    #insert line break here
    for item in user_created_haiku:
        print item
    print "Haikus that you generated:"
    #insert line break here
    for item in user_generated_haiku:
        print item
    #insert line break here
    user_input_go_back = raw_input("Press 0 to return to main menu >>>")

    if user_input_go_back == "0":
        main_menu()
    else:
        print "please press 0 to go back to main menu"



    return


def question1_repl():
    while True:
        if question_1_input == A:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")

        elif question_1_input == B:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")
        elif question_1_input == C:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")
        elif question_1_input == D:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")
        else:
            print "Please select one of the above"
        return

def question2_repl():

    while True:
        if question_choice == A:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")

        elif question_choice == B:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")

        elif question_choice == C:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")

        elif question_choice == D:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")
        return

def question3_repl():

    while True:
        if question_choice == A:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")

        elif question_choice == B:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")

        elif question_choice == C:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")

        elif question_choice == D:
            # function to add a line of haiku to Line 1
            user_created_haiku.append("line of haiku here")
        return


main_menu()
