import time
import os

global name_len
global min_age

def info_collect():
    print("Welcome to QuintaCode! Please enter your name.")
    global submitted_name
    submitted_name = input()
    name_len = len(submitted_name)
    if name_len < 2:
        clear_cons()
        print("Name must be of 2 or more characters!")
        time.sleep(1)
        clear_cons()
        info_collect()
    else:
        clear_cons()
        age_collect()
        
def age_collect():
    global entry_age
    entry_age = int(input(f"Hey there {submitted_name}! Enter your age here! "))
    if entry_age < min_age:
        clear_cons()
        print("Sorry, you're not old enough for here")
    else:
        clear_cons()
        display_menu()

def sing_me_smth():
    clear_cons()
    print("So, you want a song? Okay enter the number for your song!")
    time.sleep(1)
    print("Song 1\n Song 2")
    req_song = int(input())
    if req_song == 1:
        clear_cons()
        song_1()
        time.sleep(5)
        repetition_song()

    elif req_song == 2:
        clear_cons()
        song_2()
        time.sleep(5)
        repetition_song()
    else:
        clear_cons()
        print("Enter a valid option!")
        time.sleep(2)
        sing_me_smth()

def tell_me_a_joke():
    clear_cons()
    print("So, you requested a joke? Choose joke number!")
    time.sleep(1)
    print("Joke 1")
    time.sleep(1)
    print('Joke 2')
    req_joke = int(input())
    if req_joke == 1:
        clear_cons()
        joke_1()
    elif req_joke == 2:
        clear_cons()
        joke_2()
    else:
        print("Enter a valid option")
        time.sleep(2)
        clear_cons()
        tell_me_a_joke()

def profile_make():
    global inp_country
    clear_cons()
    print("To start making your profile, please comply with the instructions that will be displayed below:\n")
    time.sleep(1.5)
    print(f"This is your current profile:")
    time.sleep(2)
    print(f"\nName: {submitted_name}")
    time.sleep(1.5)
    print(f"Age: {entry_age}")
    time.sleep(4)
    clear_cons()
    time.sleep(0.5)
    inp_country = input("Please enter your country here: ")
    print(f"Entered country: {inp_country}")
    time.sleep(2)
    clear_cons()
    inp_gender = int(input("Gender time!\nEnter 1 for man, 2 for woman, 3 for other: "))
    if inp_gender == 1:
        global true_gender
        true_gender = "Man"
        print(f"You are a {true_gender}")
        time.sleep(2)
        clear_cons()
    elif inp_gender == 2:
        true_gender = "Woman"
        print(f"You are a {true_gender}")
        time.sleep(2)
        clear_cons()
    elif inp_gender == 3:
        true_gender = "Chair"
        print(f"You are a goddamn {true_gender} please f#$k off.")
        time.sleep(2)
        clear_cons()
    else:
        print("Wrong input, try again.")
        time.sleep(1)
        profile_make()
    inp_religion = input("Please enter your religion: ")
    print(f"Entered religion: {inp_religion}")
    time.sleep(2)
    clear_cons()
    pref_music = input("Enter your favourite music genre: ")
    print(f"Entered genre: {pref_music}")
    time.sleep(2)
    clear_cons()
    info_part_2 = profile_display(inp_country, true_gender, inp_religion, pref_music)
    print(f"Your current profile:\n\nName: {submitted_name}\nAge: {entry_age}")
    print(info_part_2)
    time.sleep(5)
    print("\n(PS: The profile will reset once you leave this command)")
    time.sleep(5)
    repetition_profile()

def clone_text():
    clear_cons()
    give_text = input("Give the text to clone: ")
    clear_cons()
    time_clone = int(input("How many times will the text be cloned: "))
    clear_cons()
    print("Cloning...")
    time.sleep(time_clone)
    for i in range(time_clone):
        print(give_text)
    print("\nCloning complete, please copy the text if you wish to save it.")
    time.sleep(6)
    repetition_clone()

def cap_or_low():
    clear_cons()
    print("What would you like to do?\n")
    time.sleep(1)
    print("Capitalize text - 1\nMinimalize text - 2")
    time.sleep(0.5)
    text_format = int(input())
    if text_format == 1:
        clear_cons()
        text = input("Enter text to capitalize: ")
        length = len(text)
        load_time = length/2
        print("Capitalizing...")
        time.sleep(load_time)
        print(f"Capitalized text: {text.upper()}")
        time.sleep(1)
        print("Please copy the text if you want it saved.")
        time.sleep(5)
        clear_cons()
        repetition_size()
    if text_format == 2:
        clear_cons()
        text = input("Enter text to minimize: ")
        length = len(text)
        load_time = length/2
        print("Minimalizing...")
        time.sleep(load_time)
        print(f"Capitalized text: {text.lower()}")
        time.sleep(1)
        print("Please copy the text if you want it saved.")
        time.sleep(5)
        clear_cons()
        repetition_size()

def calculate():
    print("Enter the serial number of what you want mathematical function you want to perform!")
    time.sleep(2)
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square\n6. Cube")
    req_function = int(input("Function "))
    if req_function == 1:
        time.sleep(1)
        clear_cons()
        num_func = int(input("How many additions to do:"))
        time.sleep(1)
        if num_func > 0:
            clear_cons()
            time.sleep(1)
            add_num = int(input("How many numbers to add (Max 5):"))
            if add_num <= 1:
                print("You can't 'calculate' with only one number...")
                time.sleep(2)
                clear_cons()
                calculate()
            if add_num == 2:
                for j in range(num_func):
                     A, B = map(int, input("Enter only the two digits to add:").split())
                     compute_value2(A, B)
                     time.sleep(2)
                     repetition_maths()
            elif add_num == 3:
                for j in range(num_func):
                     A, B, C = map(int, input("Enter only the three digits to add:").split())
                     compute_value3(A, B, C)
                     time.sleep(2)
                     repetition_maths()
            elif add_num == 4:
                for j in range(num_func):
                     A, B, C, D = map(int, input("Enter only the four digits to add:").split())
                     compute_value4(A, B, C, D)
                     time.sleep(2)
                     repetition_maths()
            elif add_num == 5:
                for j in range(num_func):
                     A, B, C, D, E = map(int, input("Enter only the five digits to add:").split())
                     compute_value5(A, B, C, D, E)
                     time.sleep(2)
                     repetition_maths()
            elif add_num > 5:
                print("Unable to compute more than 5 digits")
                time.sleep(1)
                clear_cons()
                calculate()
            else:
                print("Invalid Input")
                time.sleep(2)
                clear_cons()
                calculate()
        else:
            print("Wrong Input")
            time.sleep(2)
            clear_cons()
            calculate()
    if req_function == 2:
        time.sleep(1)
        clear_cons()
        num_func = int(input("How many subtractions to do:"))
        time.sleep(1)
        if num_func > 0:
            clear_cons()
            time.sleep(1)
            add_num = int(input("How many numbers to subtract (Max 5):"))
            if add_num <= 1:
                print("You can't 'calculate' with only one number...")
                time.sleep(2)
                clear_cons()
                calculate()
            if add_num == 2:
                for j in range(num_func):
                    A, B = map(int, input("Enter only the two digits to subtract:").split())
                    compute_sub2(A, B)
                    time.sleep(2)
                    repetition_maths()
            elif add_num == 3:
                for j in range(num_func):
                    A, B, C = map(int, input("Enter only the three digits to subtract:").split())
                    compute_sub3(A, B, C)
                    time.sleep(2)
                    repetition_maths()
            elif add_num == 4:
                for j in range(num_func):
                    A, B, C, D = map(int, input("Enter only the four digits to subtract:").split())
                    compute_sub4(A, B, C, D) 
                    time.sleep(2)
                    repetition_maths()
            elif add_num == 5:
                for j in range(num_func):
                    A, B, C, D, E = map(int, input("Enter only the five digits to subtract:").split())
                    compute_sub5(A, B, C, D, E)
                    time.sleep(2)
                    repetition_maths()
            elif add_num > 5:
                print("Unable to compute more than 5 digits")
                time.sleep(1)
                clear_cons()
                calculate()
            else:
                print("Invalid Input") 
                time.sleep(2)
                clear_cons()
                calculate()
        else:
            print("Wrong Input")
            time.sleep(2)
            clear_cons()
            calculate()
    if req_function == 3:
        time.sleep(1)
        clear_cons()
        num_func = int(input("How many multiplications to do: "))
        time.sleep(1)
        if num_func > 0:
            clear_cons()
            time.sleep(1)
            add_num = int(input("How many numbers to multiply (Max 5): "))
            if add_num <= 1:
                print("You can't 'calculate' with only one number...")
                time.sleep(2)
                clear_cons()
                calculate()
            if add_num == 2:
                for j in range(num_func):
                    A, B = map(int, input("Enter only the two digits to multiply:").split())
                    compute_mult2(A, B)
                time.sleep(2)
                repetition_maths()
            if add_num == 3:
                for j in range(num_func):
                    A, B, C = map(int, input("Enter only the three digits to multiply:").split())
                    compute_mult3(A, B, C)
                time.sleep(2)
                repetition_maths()
            if add_num == 4:
                for j in range(num_func):
                    A, B, C, D = map(int, input("Enter only the four digits to multiply:").split())
                    compute_mult4(A, B, C, D)
                time.sleep(2)
                repetition_maths()
            if add_num == 5:
                for j in range(num_func):
                    A, B, C, D, E = map(int, input("Enter only the five digits to multiply:").split())
                    compute_mult5(A, B, C, D, E)
                time.sleep(2)
                repetition_maths()
            elif add_num > 5:
                print("Unable to compute more than 5 digits")
                time.sleep(1)
                clear_cons()
                calculate()
            else:
                clear_cons()
                print("Invalid Input")
                time.sleep(2)
                clear_cons()
                calculate()
        else:
            print("Wrong Input")
            time.sleep(2)
            clear_cons()
            calculate()
    if req_function == 4:
        time.sleep(1)
        clear_cons()
        num_func = int(input("How many divisions will be done:"))
        time.sleep(1)
        if num_func > 0:
            clear_cons()
            time.sleep(1)
            for i in range(num_func):
                A, B = map(int, input("Only enter 2 numbers to divide: ").split())
                compute_div2(A, B)
            time.sleep(2)
            repetition_maths()
        else:
            clear_cons()
            print("Incorrect input")
            time.sleep(2)
            clear_cons()
            calculate()
    if req_function == 5:
        clear_cons()
        sq_num = int(input("Enter the amount of numbers to be squared: "))
        if sq_num > 0:
            time.sleep(1)
            clear_cons()
            for i in range(sq_num):
                sq_digit = int(input("Enter one number to square: "))
                square = compute_sq(sq_digit)
                print(square)
            time.sleep(2)
            repetition_maths()
        else:
            clear_cons()
            print("Incorrect input")
            time.sleep(2)
            clear_cons()
            calculate()
    if req_function == 6:
        clear_cons()
        cube_num = int(input("Enter the amount of numbers to be cubed: "))
        if cube_num > 0:
            clear_cons()
            time.sleep(1)
            for i in range(cube_num):
                cube_digit = int(input("Enter one number to be cubed: "))
                cube = compute_cube(cube_digit)
                print(cube)
            time.sleep(2)
            repetition_maths()
        else:
            clear_cons()
            print("Incorrect input")
            time.sleep(2)
            clear_cons()
            calculate()
    if req_function == 0:
        clear_cons()
        print("Aye bro watchu doing?? Wrong input!")
        time.sleep(2)
        clear_cons()
        calculate()
    if req_function > 6:
        clear_cons()
        print("Wrong input. Try again")
        time.sleep(2)
        clear_cons()
        calculate()
def count_characters():
    clear_cons()
    text = input("Enter the text that needs counting: ")
    text_length = len(text)
    print("Length of this text:", text_length)
    time.sleep(2)
    repetition_count()

def clear_cons():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("Here is a list of all the things you can do here!")
    time.sleep(2)
    print("1. Ask for a song(Only two (':)")
    time.sleep(1)
    print("2. Ask for a joke (There are only two so yeah it might get boring.)")
    time.sleep(1)
    print("3. Count the number of characters in your given input(Spaces included).")
    time.sleep(1)
    print("4. Do some calculations")
    time.sleep(1)
    print("5. Create a profile and ask for your profile to show.")
    time.sleep(1)
    print("6. Show the same message a given number of times.")
    time.sleep(1)
    print("7. Capitalize or minimize given text")
    time.sleep(1)
    print("Now enter the serial number of what you want to do")
    req_menu = int(input())
    if req_menu == 1:
        clear_cons()
        sing_me_smth()
    elif req_menu == 2:
        clear_cons()
        tell_me_a_joke()
    elif req_menu == 3:
        clear_cons()
        count_characters()
    elif req_menu == 4:
        clear_cons()
        calculate()
    elif req_menu == 5:
        clear_cons()
        profile_make()
    elif req_menu == 6:
        clear_cons()
        clone_text()
    elif req_menu == 7:
        clear_cons()
        cap_or_low()
    else:
        clear_cons()
        print("Invalid Input, type an option from above.")
        time.sleep(2)
        clear_cons()
        display_menu()

def song_1():
        print("Song: Never Gonna Give You Up")
        time.sleep(2)
        print("By Rick Astley\n")
        time.sleep(3)
        print("We're no strangers to love")
        time.sleep(2)
        print("You know the rules and so do I (do I)")
        time.sleep(2)
        print("\nA full commitment's what I'm thinking of")
        time.sleep(2)
        print("You wouldn't get this from any other guy\n")
        time.sleep(2)
        print("I just wanna tell you how I'm feeling")
        time.sleep(2)
        print("Gotta make you understand\n")
        time.sleep(2)
        print("Never gonna give you up")
        time.sleep(2)
        print('Never gonna let you down')
        time.sleep(2)
        print("Never gonna run around")
        time.sleep(2)
        print("and desert you.")
        time.sleep(2)
        print("\nNever gonna make you cry")
        time.sleep(2)
        print("Never gonna say goodbye")
        time.sleep(2)
        print("Never gonna tell a lie")
        time.sleep(2)
        print("and hurt you...")
        time.sleep(2)
        print("\n(Shortened for the sake of the coder's hands.)")

def song_2():
    print("Sonq: Waiting For Love")
    time.sleep(2)
    print("By Avicii\n")
    time.sleep(3)
    print("Where there's a will, there's a way, kind of beautiful")
    time.sleep(1.5)
    print("And every night has its day, so magical")
    time.sleep(1.5)
    print("And if there's love in this life, there's no obstacle")
    time.sleep(1.5)
    print("That can't be defeated\n")
    time.sleep(1.5)
    print("For every tyrant, a tear for the vulnerable")
    time.sleep(1.5)
    print("In every lost soul, the bones of a miracle")
    time.sleep(1.5)
    print("For every dreamer, a dream, we're unstoppable")
    time.sleep(1.5)
    print("With something, to believe in\n")
    time.sleep(1.5)
    print("Monday left me broken")
    time.sleep(1.5)
    print("Tuesday, I was through with hoping")
    time.sleep(1.5)
    print("Wednesday, my empty arms were open")
    time.sleep(1.5)
    print("Thursday, waiting for love, waiting for love\n")
    time.sleep(1.5)
    print("Thank the stars, it's Friday")
    time.sleep(1.5)
    print("I'm burning like a fire gone wild on Saturday")
    time.sleep(1.5)
    print("Guess I won't be coming to church on Sunday,")
    time.sleep(1.5)
    print("I'll be waiting for love, waiting for love")
    time.sleep(1.5)
    print("To come around...")
    time.sleep(5)
    print("\nWe are one of a kind, irreplaceable,")
    time.sleep(1.5)
    print("How did I become so blind and so cynical?")
    time.sleep(1.5)
    print("When there's love in this life, we're unstoppable,")
    time.sleep(1.5)
    print("No we can't be, defeated...")
    time.sleep(2)
    print("\nMonday left me broken")
    time.sleep(1.5)
    print("Tuesday, I was through with hoping")
    time.sleep(1.5)
    print("Wednesday, my empty arms were open")
    time.sleep(1.5)
    print("Thursday, waiting for love, waiting for love\n")
    time.sleep(1.5)
    print("Thank the stars, it's Friday")
    time.sleep(1.5)
    print("I'm burning like a fire gone wild on Saturday")
    time.sleep(1.5)
    print("Guess I won't be coming to church on Sunday,")
    time.sleep(1.5)
    print("I'll be waiting for love, waiting for love")
    time.sleep(1.5)
    print("To come around...")

def joke_1():
    print("Once, 5 Million dollars went missing from the office of a mafia boss.\nHe called his deaf accountant and a translator. The boss told the translator,\n'Ask that son of a b#@$h where my money went.' The translator asked the accountant, and replied,\n 'Boss, he says he doesn't know.' The boss replied, 'Tell him that he gets one\nmore chance to answer.' The two communicated, and the translator said, 'He\n still doesn't know.' The boss became angry and yelled, 'Well he better\nknow or I'll blow his f#@$king head off.' Then the accountant told the translator it is under the\ndesk. The boss asked, 'What'd he say?'\nThe translator replied, 'He told you to go f&%k yourself'")
    repetition_joke()
def joke_2():
    print("An American, an Indian, and a Russian go to hell. There, they\nmeet with the devil. He tells them 'I will give you three a chance to\ngo to Heaven. If you can survive 3 hits from my whip without screaming, you're free'\nThe American picks up a heavy concrete slab. The devil lands his whip on the slab, and it breaks\nin half. He lands another whip on the American, and he screams out in pain and is sent down. He\nthen heads to the Indian. The Indian says, 'Finally! My 10 years of meditation will come to use!' The devil lands\na whip on him. He gives a muffled groan, but nothing more. The devil lands another whip, but again a groan and nothing more. Another\nwhip, and the Indian passes the test. The devil gets frustrated and says, 'No one ever survived my whip test before!\nYou can go up' The Indian said, 'No, I wanna stay and see what the Russian does! They always win in this type of things!' The devil\ngoes up to the Russian and asks him, 'What will you defend yourself with?'\nThe Russian says, 'Why of course, the Indian!")
    repetition_joke()
def compute_value2(a, b):
    d = a + b
    print("Result:", d)

def compute_value3(a, b, c):
    d = a + b + c
    print("Result:", d)

def compute_value4(a, b, c, d):
    d = a + b + c + d
    print("Result:", d)

def compute_value5(a, b, c, d, e):
    d = a + b + c + d + e
    print("Result:", d)

def compute_sub2(a, b):
    d = a - b
    print("Result:", d)

def compute_sub3(a, b, c):
    d = a - b - c
    print("Result:", d)

def compute_sub4(a, b, c, d):
    d = a - b - c - d
    print("Result:", d)

def compute_sub5(a, b, c, d, e):
    d = a - b - c - d - e
    print("Result:", d)

def compute_mult2(a, b):
    d = a*b
    print("Result:", d)

def compute_mult3(a, b, c):
    d = a*b*c
    print("Result:", d)

def compute_mult4(a, b, c, d):
    d = a*b*c*d
    print("Result:", d)

def compute_mult5(a, b, c, d, e):
    d = a*b*c*d*e
    print("Result:", d)
def compute_div2(a, b):
    d = a/b
    e = a%b
    print("Result:", d, "\nRemainder:", e)
def compute_sq(a):
    d = a*a
    return("Result:", d)
def compute_cube(a):
    d = a**3
    return("Result:", d)

def repetition_clone():
    clear_cons()
    print("\nType 1 to do this again\nType 2 to do something else\nType 3 to finish")
    decision_input = int(input("\nChoice - "))
    if decision_input == 1:
        clear_cons()
        clone_text()
    elif decision_input == 2:
        clear_cons()
        display_menu()
    elif decision_input == 3:
        clear_cons()
        byee()
    else:
        print("Bro actually do it correctly.")
        time.sleep(2)
        repetition_clone()

def repetition_song():
    clear_cons()
    print("Type 1 to do this again\nType 2 to do something else\nType 3 to finish")
    decision_input = int(input("Choice - "))
    if decision_input == 1:
        clear_cons()
        sing_me_smth()
    elif decision_input == 2:
        clear_cons()
        display_menu()
    elif decision_input == 3:
        clear_cons()
        byee()
    else:
        print("Bro actually do it correctly.")
        time.sleep(2)
        repetition_song()

def repetition_count():
        print("Would you like to try another command?\nYes - 1\nNo - 2")
        decision_input = int(input("Input your chosen number: "))
        if decision_input == 1:
            clear_cons()
            display_menu()
        elif decision_input == 2:
            clear_cons()
            print("Do you wanna do this command again?\nYes - 1\nNo - 2")
            time.sleep(2)
            dec2 = int(input("Enter new decision: "))
            if dec2 == 1:
                count_characters()
            elif dec2 == 2:
                byee()
            else:
                clear_cons
                print("Because you typed something wrong, you're gonna have to do it again.\nNext time, actually type something.")
                time.sleep(2)
                count_characters()
        else:
            print("Nice try, but you didn't give anything...try again by actually inputting something.")
            time.sleep(2)
            count_characters()

def repetition_maths():
    time.sleep(10)
    clear_cons()
    print("Type 1 to do this again\nType 2 to do something else\nType 3 to finish")
    decision_input = int(input("Choice - "))
    if decision_input == 1:
        clear_cons()
        calculate()
    elif decision_input == 2:
        clear_cons()
        display_menu()
    elif decision_input == 3:
        clear_cons()
        byee()
    else:
        print("Bro actually do it correctly.")
        time.sleep(2)
        repetition_maths()

def repetition_joke():
    time.sleep(20)
    clear_cons()
    print("Type 1 to do this again\nType 2 to do something else\nType 3 to finish")
    decision_input = int(input("Choice - "))
    if decision_input == 1:
        clear_cons()
        tell_me_a_joke()
    elif decision_input == 2:
        clear_cons()
        display_menu()
    elif decision_input == 3:
        clear_cons()
        byee()
    else:
        print("Bro actually do it correctly.")
        time.sleep(2)
        repetition_joke()

def repetition_profile():
    clear_cons()
    print("Type 1 to do this again\nType 2 to do something else\nType 3 to finish")
    decision_input = int(input("Choice - "))
    if decision_input == 1:
        clear_cons()
        profile_make()
    elif decision_input == 2:
        clear_cons()
        display_menu()
    elif decision_input == 3:
        clear_cons()
        byee()
    else:
        print("Bro actually do it correctly.")
        time.sleep(2)
        repetition_profile()

def repetition_size():
    clear_cons()
    print("Type 1 to do this again\nType 2 to do something else\nType 3 to finish")
    decision_input = int(input("Choice - "))
    if decision_input == 1:
        clear_cons()
        cap_or_low()
    elif decision_input == 2:
        clear_cons()
        display_menu()
    elif decision_input == 3:
        clear_cons()
        byee()
    else:
        print("Bro actually do it correctly.")
        time.sleep(2)
        repetition_size()

def byee():
    print(farewell_text)
    time.sleep(2)
    print(farewell_text2)

min_age = 13
farewell_text = "Thanks for trying this code out!\n"
farewell_text2 = "QuintaCode, made by GitHub @YewTiubAr534.\nIf you have any ideas or any suggestions to add to this code,\nhit him up on GitHub or violince.itzme2965@gmail.com.\nHe also has a youtube channel @YewTiubAr. Check him out!"

def profile_display(country, gender, religion, music):
    return(f"Gender: {gender}\nReligion: {religion}\nCountry: {country}\nPreferred music genre: {music}")

clear_cons()
info_collect()