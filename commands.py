from init import read_words, read_defs, write_words, write_defs, read_easy_words, read_med_words, read_hard_words, write_easy_words, write_med_words, write_hard_words, read_easy_defs, write_easy_defs

words = read_words()
defs = read_defs()

easy_words = read_easy_words()
med_words = read_med_words()
hard_words = read_hard_words()

easy_defs = read_easy_defs()

def print_commands():
    print()
    print("COMMAND LIST")
    print("=" *113)
    print(" \'add\' - add word to list".ljust(52), " ||", "\'del\' - delete word from list".ljust(53), "||\n",
          "\'def\' - define a word".ljust(52), "||", "\'list\' - show word list".ljust(53), "||\n",
          "\'dict\' - show word list w/ definitions".ljust(52), "||", "\'flash\' - enter flashcard mode".ljust(53), "||\n",  
          "\'clear\' - clear shell, whitespace".ljust(52), "||", "\'commands\' - display command menu".ljust(53), "||\n",
          "\'exit\' - save & exit program".ljust(52), "||", "\'test\' - take a test".ljust(53), "||")
    print("=" *113)
    print()

def print_words(words):
    print("=" *113)
    i = iter(words)          #creating an iterator object, for use of next()
    try:                     #prints line ONLY if no exception occurs (6 words)
        for items in i:
            print(items.ljust(15), "||",next(i).ljust(15), "||",
                next(i).ljust(15), "||",next(i).ljust(15), "||",
                next(i).ljust(15), "||",next(i).ljust(15), "||")
        print("=" * 113)
        print()
        print("Word Count = ", len(words))
    except StopIteration:
            print("=" * 113)
            lineCount= len(words)%6          
            print("X  " * lineCount)
            print("Word Count = ", len(words))

def print_defs(words, defs):
    x = 1
    for items in words:
        index = words.index(items)
        print(str(x),"." , items.title().ljust(15), "-", defs[(index)])
        x += 1

def add_word(words, defs):
    while True:
        new_word = input("Word To Add:\t")
        if new_word.lower() == "break":
            break
        new_def = input("Definition:\t")
        if new_def.lower() == "break":
            break
        if new_word not in words:
            words.append(new_word.title())
            print()
# ADD a difficulty filter here -> needs to be assigned (E,M, or H)
            print(new_word, "- Added Successfully")
            print()
            write_words(words)
        else:
            print()
            print(new_word, "- Already In List")
        if new_def not in defs:
            defs.append(new_def.title())
            write_defs(defs)
        else:
            print(new_def,  "- Definition Exists")

def delete_word(words, defs):
    axe = input("Word To Remove:\t")
    if axe.title() in words:
        defs.pop(words.index(axe.title()))
        words.remove(axe.title())
        print()
        print(axe, "-  Has Been Removed")
        write_words(words)                 #changes implemented immediately
        write_defs(defs)
    else:
        print()
        print(axe, "- Is Not In List")

def define_word(words, defs):
    word = input("Word To Define:\t")
    if word.title() in words:
        index = words.index(word.title())
        print()
        print("TRANSLATION:")
        print("\"",word.title(), "\"", "-", defs[(index)])
    else:
        print("\nWord Not In List\n")
        
def clear():
    print('\n' * 50)

# this function moves words to easy (reserves, not in current working dict)
# medium, or hard

def move_word(words, defs, easy_words, med_words, hard_words, easy_defs):
    while True:
        move_word = input("Word To Move:\t")
        if move_word.lower() == "break":
            break
        if move_word not in easy_words and move_word not in med_words and move_word not in hard_words:
            print()
            print("Word Currently Not Assigned, PLZ assign a diifuclty")
            print()
            print("Easy = E")
            print("Medium = M")
            print("Hard = H")
            print()
            difficulty = input("Desired Difficulty:\t")
            # add a check to see if move_word even exists in words
            if difficulty.lower() == "e":
                index = words.index(move_word.title())
                easy_words.append(move_word.title()) # add to easy word list
                easy_defs.append(defs[move_word.title()]) # add to easy def list * needs creating
                words.pop(index) # removes word from current working dict because its too easy
                defs.pop(index) # remove def also
                write_easy_words(easy_words)    # updates easy word list
                print()
                print(move_word, "- Removed from Current Working Dict and Added to Easy Word List")
                print()
                write_words(words)
                write_defs(defs)
            elif difficulty.lower() == "m":
                med_words.append(move_word.title())
                write_med_words(med_words)
                print()
                print(move_word, "- Added to Medium Word List")
                print()
            elif difficulty.lower() == "h":
                hard_words.append(move_word.title())
                write_hard_words(hard_words)
                print()
                print(move_word, "- Added to Hard Word List")
                print()
            else:
                print("Invalid Input Word not assigned")
                break

    
    
    
