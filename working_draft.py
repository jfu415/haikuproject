
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
    \n
    """

    print user_options

    execute_main_menu()


def execute_main_menu():
    this_loop = True
    while this_loop:
        choice = raw_input('\nChoose from the menu options: ')
        if choice == "1":
            # introduction
            introduction()

        elif choice == "2":
            print "\n~~~~Okay! Let's begin!~~~~"
            print "\nAnswer the following questions based on how you feel about each political context."
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
            exit()

        else:
            try:
    			execute_main_menu()
    			print "\n"

            except ValueError:
                this_loop = False
                print "Invalid input. Please select an option from 1-5"
                continue



####### MENU PROMPTS ########

def introduction():
    # Brief introduction of what a Haiku is and how to create one
    print "\n~~~~Introduction~~~~"
    print "\n"
    print "A haiku is a traditional form of Japanese poetry"
    print "with 3 lines that do not have to rhyme."
    print "The first and last lines contain 5 syllables,"
    print "while the second line contains 7 syllables."
    print "\n"
    user_input_go_back = raw_input("""\nPress 0 to return to main menu \nPress 1 to see examples of a haiku >>>""")

    if user_input_go_back == "0":
        main_menu()
    elif user_input_go_back == "1":
        print "\nHaikus are easy"
        print "But sometimes they don't make sense"
        print "Refrigerator\n"
        print "\n "
        print "Advice for those"
        print "in a difficult position:"
        print "First, be flexible.\n"
        print "\n"

    else:
        print "Please select either 0 or 1."



    return
def display_all_haikus():

    # displays all of the haikus that the user has generated or created
    Chaiku_length = len(user_created_haiku)
    Ghaiku_length = len(user_generated_haiku)

    if (Chaiku_length < 3 and Ghaiku_length == 0):
        for item in user_created_haiku:
            print item
            print "\nYou've only written {} lines of haiku so far and you haven't generated any haikus either!!".format(Chaiku_length)

    elif (Chaiku_length == 0 and Ghaiku_length == 0):
        print "View what?!?!?! You haven't written or generated anything yet!! Go back to the main menu! "

    elif (Ghaiku_length == 0 and Chaiku_length < 3):
        print "You've only written {} lines of haiku so far, and you haven't generated any haikus either! What are you doing!!!??".format(Chaiku_length)


    # elif (Chaiku_length == 3 and Ghaiku_length == 3):
    else:
        print "\nHaikus that you wrote:"
        print "\n"
        for item in user_created_haiku:
            print item
        print "\n"
        print "Haikus that you generated:"
        print "\n"

        for item in user_generated_haiku:
            print item



    user_input_go_back = raw_input("\nPress 0 to return to main menu")

    if user_input_go_back == "0":
        main_menu()

    else:
        user_input_go_back = raw_input("Press 0 to return to main menu >>>")
        return

def question_1():
    print "\nIn your honest opinion, do you think the government should work with the people to"
    print "ensure every person's basic needs are met in order to survive?\n"
    print "A) I have no opinions about this issue. "
    print "B) The common good of all people depends on a unifying effort to defend the civil rights of every human being."
    print "C) I believe we should all worry about our own lives and successes. We get what we deserve."
    print "D) None of these options describe how I feel\n"
    question_1_input = str(raw_input("Which selection best fits you? >>").upper())
    question1_repl(question_1_input)

    return

def question_2():
    print "\nDo you think the U.S. military should be involved in all international affairs?\n"
    print "A) None of these options describe how I feel"
    print "B) No, it is hypocritical to engage in international affairs when we have not resolved the harrowing issues at home."
    print "C) I don't have an opinion on this issue. "
    print "D) Yes, it is our duty and obligation to fight for less fortunate countries.\n"
    question_2_input = str(raw_input("Which selection best fits you? >>").upper())
    question2_repl(question_2_input)

    return

def question_3():

    print "\nHow did you feel on the evening of November 8th, 2016 (election day)?\n"
    print "A) Angry, helpless, confused, sad "
    print "B) I have no opinions on this issue"
    print "C) Relieved, hopeful, determined, glad"
    print "D) Wasn't angry, excited or upset. Didn't bother me at all.\n"
    question_3_input = str(raw_input("Which selection best fits you? >>").upper())
    question3_repl(question_3_input)

    return

def question1_repl(input):
    # 5 SYLLABLE LINE
    loop = True
    while loop:
        if input == "A":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("No, I haven't heard")
                question_2()
        elif input == "B":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("If not now, then when?")
                question_2()
        elif input == "C":
                # function to add a line of haiku to Line 1
                user_generated_haiku.append("White picket fences")
                question_2()
        elif input == "D":
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
            user_generated_haiku.append("insert line here")
            question_3()
        elif input == "B":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("What about the war at home?")
            question_3()
        elif input == "C":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("Doesn't matter anyway")
            question_3()
        elif input == "D":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("Fighting hard in the trenches")
            question_3()
    return

def finished_generating():

    user_input_view_gen = raw_input("Press 1 to see your generated Haiku >>>")

    while True:

        if user_input_view_gen == "1":
            for item in user_generated_haiku:
                print item
        break

    return_to_mm = raw_input("\nPress 0 to return to main menu to create more haikus!! >>>")

    while True:

        if return_to_mm == "0":
            main_menu()


def question3_repl(input):
    #5 SYLLABLE LINE

    while True:
        if input == "A":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("There goes my freedom")
            finished_generating()
        elif input == "B":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("What does this mean, then?")
            finished_generating()
        elif input == "C":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("Make it great again.")
            finished_generating()
        elif input == "D":
            # function to add a line of haiku to Line 1
            user_generated_haiku.append("I really don't care")
            finished_generating()




def view_created_haiku():

    for item in user_created_haiku:
        print item

    print "\n~~~Are you happy with your haiku?~~~"
    user_input_whatnow = str(raw_input("\nType YES or NO >>")).lower()

    if user_input_whatnow == "yes":
        print "Great! "
        main_menu()
    elif user_input_whatnow == "no":
        print "Oh no! I'm so sorry to hear that. Would you like to rewrite the whole haiku or just a specific line?"
        print "\n 1 -- Delete this haiku and write a new one"
        print "\n 2 -- Remove a specific line"
        print "\n 3 -- Just kidding I do like it. Take me back to the main menu"

    user_input_edit = raw_input("Enter here>>>")

    if user_input_edit == "1":
        print "delete"
    elif user_input_edit == "2":
        pass #insert function to .pop
    elif user_input_edit == "3":
        main_menu()

def write_line_3():
    #asks user if they would like to continue writing their haiku

    user_input_cont = raw_input("Ready to keep writing?! Press 1!!>>")
    if user_input_cont == "1":
        line3 = str(raw_input("Begin writing your third line here -------->> "))

    #passes user created line3 into CountSyllables function

    line3_syl = CountSyllables(line3)

    #while loop to check if user has met syllable requirements
    while True:

        if line3_syl != 5:
            print "The line you entered has {0} syllables, when you need 5 for your third line. Try again!".format(line3_syl)
            write_line_3()

    #if yes, add to list containing haiku lines

        elif line3_syl == 5:
            print "Great! 5 syllables. Adding this to your haiku now..... *beep*.... ..... *beepboop*..... *beep!*... one moment!\n"
            add_line_to_list(line3)
            break

    print "Would you like to see your haiku?"
    wanna_see = raw_input("\nPress 1 to view your haiku.\n Press 2 to return to main menu >>>")
    if wanna_see == "1":
        view_created_haiku()
    elif wanna_see == "2":
            main_menu()

def write_line_2():


    line2 = str(raw_input("Begin writing your second line here -------->> "))

    line2_syl = CountSyllables(line2)

#function to check syllables/continue writing haiku

    while True:
        #line2_syl = CountSyllables(line2)
        if line2_syl != 7:
            print "The line you entered has {0} syllables, when you need 7 for your second line. Try again!".format(line2_syl)
            write_line_2()


        elif line2_syl == 7:
            print "\nGreat! 7 syllables. Adding this to your haiku now..... *beep*.... ..... *beepboop*..... *beep!*... one moment!\n"
            add_line_to_list(line2)
            break

    write_line_3()




def add_line_to_list(line):
    if line not in user_created_haiku:
        user_created_haiku.append(line)


def create_own_haiku_instructions():

    print "\n~*~*~Create Your Own Haiku~*~*~"
    print "\n"
    print "A haiku contains 3 lines."
    print "The first and third lines should contain 5 syllables"
    print "while the second line contains 7 syllables."
    print "\n"

# Write haiku Instructions here

    line1 = str(raw_input("Begin writing your first line here -------->> "))

    #pass line1 through CountSyllables function imported from Get-Sylly module and print syllables + line.
    print "\n"

    line1_syl = CountSyllables(line1)

    while True:
        line1_syl = CountSyllables(line1)

        if line1_syl != 5:
            print "The line you entered has {0} syllables, when you need 5 for your first line. Try again!".format(line1_syl)
            print "\n"
            line1 = str(raw_input("Begin writing your first line here -------->> "))

        elif line1_syl == 5:
            print "Great! 5 syllables. Adding this to your haiku now..... *beep*.... ..... *beepboop*..... *beep!*... one moment!\n"
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
