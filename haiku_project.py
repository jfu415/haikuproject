def get_menu_userinput():
    """Print a menu and asks the user to make a choice.

    Arguments:
    None
    Returns:
    int: the user's menu choice
    """

    print '    A) Introduction'
    print '    B) Generate a haiku'
    print '    C) Create my own haiku'
    print '    D) See all haikus'
    print '    E) Exit'


    choice = int(raw_input('Choose from the menu options: '))

    return choice

def main_menu_repl():

    while True:
        choice = get_menu_userinput().upper()
        if choice == "A":
        # introduction
            print
            "A haiku is

            When you prompt these questions to create your own haiku,
            choose the answer that best fits you."





        elif choice == "B":
            print "Okay! Let's begin!"

            # call function here to prompt series of questions

        elif choice == "C":

            # call function here to display all haikus that user has generated

        elif choice == "D":
        # quit program

            break

def display_all_haikus():
    print user_created_haiku
    print user_generated_haiku

        # displays all of the haikus that the user has generated or created


def question1_repl():
    while True:
        if question_choice == A:
            # function to add a line of haiku to Line 1
            user_created_haiku.appened("line of haiku here")

        elif question_choice == B:
            # function to add a line of haiku to Line 1
            user_created_haiku.appened("line of haiku here")
        elif question_choice == C:
            # function to add a line of haiku to Line 1
            user_created_haiku.appened("line of haiku here")
        elif question_choice == D:
            # function to add a line of haiku to Line 1
            user_created_haiku.appened("line of haiku here")


    def question2_repl():

        while True:

            if question_choice == A:
                # function to add a line of haiku to Line 1
                user_created_haiku.appened("line of haiku here")

            elif question_choice == B:
                # function to add a line of haiku to Line 1
                user_created_haiku.appened("line of haiku here")

            elif question_choice == C:
                # function to add a line of haiku to Line 1
                user_created_haiku.appened("line of haiku here")

            elif question_choice == D:
                # function to add a line of haiku to Line 1
                user_created_haiku.appened("line of haiku here")

def question3_repl():

    while True:

        if question_choice == A:
            # function to add a line of haiku to Line 1
            user_created_haiku.appened("line of haiku here")

        elif question_choice == B:
            # function to add a line of haiku to Line 1
            user_created_haiku.appened("line of haiku here")

        elif question_choice == C:
            # function to add a line of haiku to Line 1
            user_created_haiku.appened("line of haiku here")

        elif question_choice == D:
            # function to add a line of haiku to Line 1
            user_created_haiku.appened("line of haiku here")



user_created_haiku = []
user_generated_haiku = []
