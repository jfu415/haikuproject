def get_menu_userinput():
    """Print a menu and asks the user to make a choice.

    Arguments:
    None
    Returns:
    int: the user's menu choice
    """
    user_options = """
    \nChoose from the options below:
    A) Introduction
    B) Generate a haiku
    C) Create my own haiku
    D) See all haikus
    E) Exit
    >>> """

    print user_options
    user_input = str(raw_input('Choose from the menu options: '))


    while True:
        user_input = (raw_input(user_options)).upper()
        if user_input == "A":
            # introduction
            haiku_intro()

        elif user_input == "B":
            print "Okay! Let's begin!"

            # call function here to prompt series of questions to generate

        elif user_input == "C":
            print "here ya go"
            # call function here to allow user to create own haiku

        elif user_input == "D":
            #
            display_all_haikus()

        elif user_input == "E":
            break
def haiku_intro():
    print "A haiku is just \\n a 3 lined poem \\n that containes 5 7 and 5 syllables respectively \\n"
    user_input_go_back = raw_input("Press 0 to return to main menu >>>")

    if user_input_go_back == "0":
        get_menu_userinput()

def display_all_haikus():
    # Option D
    print user_created_haiku
    print user_generated_haiku

        # displays all of the haikus that the user has generated or created


def question1_repl():
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



get_menu_userinput()

user_created_haiku = []
user_generated_haiku = []
