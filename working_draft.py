
#global variables

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
    choice = int(raw_input('Choose from the menu options: '))
    execute_main_menu(choice)


def execute_main_menu(choice):
    this_loop = True
    while this_loop:
        choice = (raw_input(choice))
        if choice == '1':
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

        #else:
            #this_loop = False
            #print "Please select an option from 1-5."

####### MENU PROMPTS ########

def introduction():
    # Brief introduction of what a Haiku is and how to create one

    print "A haiku is a poem with 3 lines that contains 5, 7 and 5 syllables respectively"
    user_input_go_back = raw_input("Press 0 to return to main menu >>>")

    if user_input_go_back == "0":
        main_menu()

    return

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



def question1_repl(question_1_input):
    # 5 SYLLABLE LINE
    loop = True
    while loop:
        if question_1_input == "A":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("line(conservative) of haiku here")
                question_2()
        elif question_1_input == "B":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("line(liberal) of haiku here")
                question_2()
        elif question_1_input == "C":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("line(liberal_conserv) of haiku here")
                question_2()
        elif question_1_input == "D":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("line(apathetic) of haiku here")
                question_2()
        else:
            loop = False
            print "Please select one of the above"
    return

def question_1():
    print "\nQuestion 1 here\n"
    print "A) _____"
    print "B) ______"
    print "C) ______"
    print "D) _______\n"
    question_1_input = str(raw_input("Which selection best fits you? >>").upper())
    question1_repl(question_1_input)

    return





def question2_repl():
    # 7 SYLLABLE LINE
    while True:
        if question_choice == "A":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")
            question_3()
        elif question_choice == "B":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")
            question_3()
        elif question_choice == "C":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")
            question_3()
        elif question_choice == "D":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")
            question_3()
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

def question3_repl():
    #5 SYLLABLE LINE
    while True:
        if question_choice == "A":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")

        elif question_choice == "B":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")

        elif question_choice == "C":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("line of haiku here")

        elif question_choice == "D":
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
    user_input_go_back = raw_input("Press 0 to return to main menu >>>")

    if user_input_go_back == "0":
            main_menu()
    else:
        print "please press 0 to go back to main menu"



def create_own_haiku_instructions():

    print "~~~Create Your Own Haiku~~~"
    #instructions



    #line1=user_input  + syllable_count()  <---- import function from another file?


    #syllable_count(line1)

    #return syllable_count
    #return line1
    #for syllable in line1:
    #    if syllable_count(line1) == 5:
    #        print "Great! You entered 5 syllables!"

    line1 = str(raw_input("Begin writing here -------->> "))
    if line1 not in user_created_haiku:
        user_created_haiku.append(line1)


    write_line_2()
#    else:
#print "You entered a line containing [syllable_count] syllables. Try again!"


    #line1 = str(raw_input("begin writing here -------->> "))

    #syllable_count(line1)





main_menu()



######
######
######
######      TO DO LIST:
######                   **** finish writing haiku lines
######                   **** questions for haiku generator
######                   **** Would it be simpler to create a dictionary to store functions & user input options (ex. 0 - main menu, 4 - display all haikus)  ???
######                  ***** figure out how to use syllable_count()/import from https://github.com/akkana/scripts/blob/master/countsyl
######                     ** stylistic nice-to-haves
######                    *** combine generated haiku lines + user written lines
######                      * if there's time, think of more questions to increase possibilities for user to generate a unique haiku.
######
