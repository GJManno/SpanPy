import random
from collections import OrderedDict
from init import EASY_DEFS_FILE, read_easy_defs

####################  body_test() ###################################################################

BODY_SCORES = 'tests/scores/body_scores.txt'

def write_score(test_scores,):
    with open(BODY_SCORES, 'w')as file:
        for score in test_scores:
            file.write(str(score)+ "\n")
    print("This score has been recorded...")
    
    
def read_scores():
    test_scores = []
    print("Checking high score...")
    with open(BODY_SCORES, 'r')as file:
          for line in file:
              line = line.replace("\n", "")
              test_scores.append(float(line)) # scores are not whole numbers
    return test_scores


def body_test():

    word_bank = {'Tobillo':'Ankle','Patas':'Feet','Pie':'Foot','Dedos':'Digits','Piernas':'Legs',
                 'Terneros':'Calves','Rodilla':'Kneee','Muslo':'Thigh','Cadera':'Hip','Panza':'Belly',
                 'Pecho':'Chest','Pulgar':'Thumb','Hombros':'Shoulders','Orejas':'Ears',
                 'Nariz':'Nose','Ceja':'Eyebrow','Pestaña':'Eyelash','Frente':'Forehead','Barbilla':'Chin',
                 'Mejilla':'Cheek','Cráneo':'Skull','Labios':'Lips','Dientes':'Teeth',
                 'Lengua':'Tounge','Cara':'Face','Pelo':'Hair','Codo':'Elbow','Cuello':'Neck','Brazo':'Arm',
                 'Muñeca':'Wrist','Cintura':'Waist','Ombligo':'Belly Button','Espinilla':'Shin / Pimple',
                 'Talón':'Heel','Huesos':'Bones', 'Piel':'Skin','Uñas':'Nails','Arrugas':'Wrinkles',
                 'Pezón':'Nipple','Pecas':'Freckles','Cerumen':'Earwax','Pulmón':'Lung','Hígado':'Liver',
                 'Cerebro':'Brain','Garganta':'Throat','Párpado':'Eyelid','Nudillos':'Knuckles','Costilla':'Rib'}    
    body_count = len(word_bank)
    print("Total Test Questions = ", body_count,)
    print()
    score = 0
    questions = (list(word_bank.keys()))
    random.shuffle(questions)
    for word in questions:
        print("The Word is: ", word)
        print("=" * 25)
        a = input("Do You Know It? (y/n):\t")
        if a.lower() == "y":
            score += 1
            print()
            print("Answer:\t", word_bank[word])
            print()
        elif a.lower() == "n":
            print()
            print("Answer:\t", word_bank[word])
            print()
        else:
            print()
            print("No Score Recorded For \t", word,"-",word_bank[word])
    print("========== END OF TEST ==========")
    letter_grade = round((score/body_count)* 100, 2)
    print("Your Score is:", score, "out of ", body_count)
    if letter_grade >= 90:
        print("You got an A", "(", letter_grade, "%)")
    elif letter_grade < 90 and letter_grade >= 80:
        print("You got a B", "(", letter_grade, "%)")
    elif letter_grade < 80 and letter_grade >= 70:
        print("You got a C", "(", letter_grade, "%)")
    elif letter_grade < 70 and letter_grade >= 60:
        print("You got a D", "(", letter_grade, "%)")
    elif letter_grade < 60:
        print("You got an F", "(", letter_grade, "%)")
    print()
    test_scores = read_scores()
    test_scores.append(letter_grade) # format to string for write output
    write_score(test_scores)        #record score
    high_score = max(test_scores)
    print("Highest Score =", high_score)
    
    

############################# flash_mode() ##########################################################

def flash_mode(words,defs, easy_words, med_words, hard_words):
    
    print("Select a Difficulty (e,m,h,a)")
    difficulty = input("What Difficulty:/t")
    if difficulty.lower() == "e":
        flash_list = list(easy_words)
        flash_defs = list(easy_defs)
    elif difficulty.lower() == "m":
        flash_list = list(med_words)
        flash_defs = list(med_defs) # needs creating like easy_defs
    elif difficulty.lower() == "h":
        flash_list = list(hard_words)
        flash_defs = list(hard_defs) # needs creating like easy_defs
    elif difficulty.lower() == "a":
        flash_list = list(words)
        flash_defs = list(defs)

    
    r_list = []                 #too many list let us reduce...
    r_defs = []
    zipped_r = list(zip(r_list, r_defs))
    zipped_list = list(zip(flash_list, flash_defs)) # to preserve the order on shuffle
    print()
    print("Entering Random Flashcard Mode")
    print("=" * 25)
    print("Press Enter To Flip")
    print("Press X To Stop")
    print("Press R To Recycle") #still needs implementation
    print("Press D To Delete")   #still needs implementation
    print()
    random.shuffle(zipped_list) 
    flash_list, flash_defs = zip(*zipped_list) #unzip shuffled word/defs back into lists
    for item in flash_list:
        index = flash_list.index(item)
        print(item) 
        go = input("===== FLIP CARD =====")
        print(flash_defs[index])
        print()
        if go.lower() == "x":
            break
        if go.lower() == "r":
            r_list.append(item)
            r_defs.append(flash_defs[index])
    print()
    print("Recycle list:")          #temp and will only show at end of flash
    for i, x in enumerate(zip(*zipped_r)):
        print(i,x)
            
            
############################################################### log_parser() #######################
#
#  Fix most recent log slice when you want (-7) 
# one solution is to (30x) month DATE add to day then subtract from last log (you will want to do for year also) (365x)-(30x)
#        

def log_parser(log_file):     #improve by turning into generator and yielding last result only
    log_list= []                          # oaky for now... but long log files wont work.
    with open(log_file) as f:
        for line in f:
            log_list.append(line)
        last_log_date = log_list[-1][:10]        # get most recent log and slice to get DATE 
    x = int(last_log_date[-2:])                       # get day of the month
    second_last_log = log_list[-2][:10]
    y = int(second_last_log[-2:])                   # get last login day of month
    z = x - y 
    if z == 0:
        print ("You\'ve Been Logged In Today, Great Work!".rjust(70))
    elif z == 1:
        print ("You Were Logged In Yesterday, Keep It Up!".rjust(70))
    else:
        print ("It has been".rjust(41), z, "days since your last login")# cannot be on end when split up

    # add 30 day buffer HERE

########################################## test_mode() ##############################################

def test_mode():
    # OrderedDict constructor does not preserve order. kwags used and passed thru normal dictionary
    # 1 SOLUTION = pass in a single list of tuples (seperated by commas not colons)
    test_bank = OrderedDict([('Body', body_test), ('Weekly Words',weekly_test)])
    
    for n, e in enumerate(list(test_bank.keys())):
        print(n, "-", e, "Test")
    print()
    while True:
        index = int(input("Select An Index To Run A Test...")) # DO NOT FORGET INT() b/c input ALWAYS returns a string
        print('='* 35)
        if index in range(len(test_bank)):
            # take user defined index and call associated function stored in Dict value
            test_bank[list(test_bank.keys())[index]]()
            break
        else:
            print('Index Not In List.. Try Again')
            print()

################ weekly_test ########################################################################

            #
            #
                # This is not really a test, all it does is accept words and defs to be saved into a txt file
                # which can then be used for a test, however this is not a test function, its an editing function.
            #
            #



            

        # scheduler module to import to master weekly list and clear this list every 7 days
        # master list should be a list of lists and should be indexed by week (1,2,3,etc.)
        # we should also check working dict to see if words not already included, if so add.
        # can possibly add xx days till reset notifaction
        # parse and split by .startswith ("-") for definition
        # do we want to enumerate this?

def weekly_test():
    WEEKLY_WORDS = 'weekly_words.txt'
    WEEKLY_DEFS = 'weekly_defs.txt'
    
    def read_words():
        weekly_words = []
        with open(WEEKLY_WORDS) as file:
            for line in file:
                line = line.replace("\n", "")
                weekly_words.append(line)
        return weekly_words                     
        
            
    def read_defs():
        weekly_defs = []
        with open(WEEKLY_DEFS) as file:
            for line in file:
                line = line.replace("\n", "")
                weekly_defs.append(line)
        return weekly_defs

    weekly_words = read_words()
    weekly_defs = read_defs()
    print("Enter Your Weekly Words, \n (press x to stop & save)")
    print()
    while True:
        word = input("w---> ")
        defin = input("d---> ")
        if word.lower() == 'x': 
            break
        else:
            weekly_words.append(word)
            weekly_defs.append(defin)
    print("saving to file...")
    with open(WEEKLY_WORDS, 'w') as file:    # newline= ""    is for CSV ONLY
        for words in weekly_words:
            file.write(words + "\n")
    with open(WEEKLY_DEFS, 'w') as file:    # newline= ""    is for CSV ONLY
        for defin in weekly_defs:
            file.write(defin + "\n")
    print("done....")
    


# this function clears the active weekly list every Sunday at 11:55pm and moves all words from the active
# weekly list into a permanent master list of weekly lists. This function also checks current working dict and 


##def weekly_refresh(weekly_list):
    
## schedule.every().sunday.at("23:55").do(weekly_refresh)

# maybe u wanna do a simple schedule first...


        
