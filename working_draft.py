
#global variables

from GetSylly import CountSyllables

user_created_haiku = []
user_generated_haiku = []


######## Main Menu ##########

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

    execute_main_menu()


def execute_main_menu():
    this_loop = True
    while this_loop:
        choice = raw_input('Choose from the menu options: ')
        if choice == "1":
            # introduction
            introduction()

        elif choice == "2":
            print "Okay! Let's begin!"
            question_1()
            # call function here to prompt series of questions to generate

        elif choice == "3":
            print "Take a shot at writing your own haiku!"
            # call function here to allow user to create own haiku
            create_own_haiku_instructions()

        elif choice == "4":
            # Displays user generated and created haikus
            display_all_haikus()

        elif choice == "5":
            # Exits program
            break

        else:
            this_loop = False
            print "Please select an option from 1-5."
            execute_main_menu()

####### MENU PROMPTS ########

def introduction():
    # Brief introduction of what a Haiku is and how to create one
    print "\n"
    print "A haiku is a poem with 3 lines that contains 5, 7 and 5 syllables respectively"
    print "\n"
    user_input_go_back = raw_input("""\nPress 0 to return to main menu \nPress 1 to see an example of a haiku >>>""")


    while True:
        if user_input_go_back == "0":
            main_menu()
        elif user_input_go_back == "1":
            print " INSERT HAIKU EXAMPLES HERE"
            print " EXAMPLE"
            print "EXAMPLE"
            break
        else:

            print "Please select either 0 or 1."
            break

def display_all_haikus():

    # displays all of the haikus that the user has generated or created

    while True:
        Chaiku_length = len(user_created_haiku)
        Ghaiku_length = len(user_generated_haiku)

        if (Chaiku_length == 0 and Ghaiku_length == 0):
            print "You haven't written any haikus yet!"
            break

        if Chaiku_length < 3:
            for item in user_created_haiku:
                print item
            print "\nYou've only written {} lines of haiku so far. Keep writing!".format(Chaiku_length)
            break

        if Ghaiku_length < 3:
            print "You've only generated {} lines of haiku so far. Answer a few more questions to get your haiku!".format(Ghaiku_length)
            break

        else:
            break
            print "Haikus that you wrote:"
            print "\n"
            for item in user_created_haiku:
                print item
                print "\n"
                print "Haikus that you generated:"
                print "\n"
            for item in user_generated_haiku:
                print item
                print "\n"

    user_input_go_back = raw_input("Press 0 to return to main menu")

    if user_input_go_back == "0":
        main_menu()

    else:
        user_input_go_back = raw_input("Press 0 to return to main menu >>>")
        return

def question_1():
    print "\nIn your honest opinion....\n"
    print "A) I have no opinions on this issue. "
    print "B) The common good of all people depends on a unifying effort to defend the civil rights of every human being."
    print "C) I believe we should all worry about our own lives and successes. We get what we deserve."
    print "D) None of these options describe how I feel\n"
    question_1_input = str(raw_input("Which selection best fits you? >>").upper())
    question1_repl(question_1_input)

    return

def question_2():
    print "\nQuestion 2 here\n"
    print "A) _____"
    print "B) ______"
    print "C) _______"
    print "D) _______\n"
    question_2_input = str(raw_input("Which selection best fits you? >>").upper())
    question2_repl(question_2_input)

    return

def question1_repl(question_1_input):
    # 5 SYLLABLE LINE
    loop = True
    while loop:
        if question_1_input == "A":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("No, I haven't heard")
                question_2()
        elif question_1_input == "B":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("If not now, then when?")
                question_2()
        elif question_1_input == "C":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("White picket fences")
                question_2()
        elif question_1_input == "D":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("Do not speak for me")
                question_2()
        else:
            loop = False
            print "Please select one of the above"
    return






def question2_repl(input):
    # 7 SYLLABLE LINE
    while True:
        if input == "A":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku")
            question_3()
        elif input == "B":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku")
            question_3()
        elif input == "C":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku")
            question_3()
        elif input == "D":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku")
            question_3()
    return



def question3_repl(input):
    #5 SYLLABLE LINE
    while True:
        if input == "A":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")

        elif input == "B":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")

        elif input == "C":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")

        elif input == "D":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")

    return

def question_3():

    print "\nQuestion 3 here\n"
    print "A) _____"
    print "B) ______"
    print "C) ______"
    print "D) _______\n"
    question_3_input = str(raw_input("Which selection best fits you? >>").upper())
    question3_repl(question_3_input)

    return



def write_line_2():

    user_input_go_back = raw_input("Press 0 to return to main menu")

#function to continue writing haiku

    if user_input_go_back == "0":
        main_menu()
    elif user_input_go_back == "1":
        line1 = str(raw_input("Begin writing here -------->> "))

    #Adds line1 to user_created_haiku list.

def add_line_to_list(line):
    if line not in user_created_haiku:
        user_created_haiku.append(line)


def create_own_haiku_instructions():

    print "~*~*~Create Your Own Haiku~*~*~"
    print "\n"
    print "A haiku contains 3 lines."
    print "The first and third lines should contain 5 syllables"
    print "while the second line contains 7 syllables."
    print "\n"

# Write haiku Instructions here

    line1 = str(raw_input("Begin writing here -------->> "))

    #pass line1 through CountSyllables function imported from Get-Sylly module and print syllables + line.
    print "\n"

    line1_syl = CountSyllables(line1)

    while True:
        line1_syl = CountSyllables(line1)

        if line1_syl != 5:
            print "The line you entered has {0} syllables, when you need 5 for your first line. Try again!".format(line1_syl)
            print "\n"
            line1 = str(raw_input("Begin writing here -------->> "))

        elif line1_syl == 5:
            print "Great! 5 syllables. Adding this to your haiku now..... *beep*.... ..... *beepboop*..... *beep!*... one moment!"
            add_line_to_list(line1)
            break

    write_line_2()
#    else:
#print "You entered a line containing [syllable_count] syllables. Try again!"


    #line1 = str(raw_input("begin writing here -------->> "))

    #syllable_count(line1)


def progress(haiku):

    if user_created_haiku:
        print user_created_haiku

    elif user_generated_haiku:
        print user_generated_haiku




main_menu()



######
######
######
######      TO DO LIST:
######                   **** finish writing haiku lines
######                   **** questions for haiku generator
######                   **** Would it be simpler to create a dictionary to store functions & user input options (ex. 0 - main menu, 4 - display all haikus)  ???
######
######                     ** stylistic nice-to-haves
######                     ** combine generated haiku lines + user written lines
######                      * if there's time, think of more questions to increase possibilities for user to generate a unique haiku.
######
