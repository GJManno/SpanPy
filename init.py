WORD_FILE = 'spanish_words.txt'
DEF_FILE = 'spanish_defs.txt'

EASY_WORDS_FILE = 'words/easy_words.txt'
MED_WORDS_FILE = 'words/med_words.txt'
HARD_WORDS_FILE = 'words/hard_words.txt'

EASY_DEFS_FILE = 'defs/easy_defs.txt'

def read_words():
    word_list = []
    with open(WORD_FILE) as file:
        for line in file:
            line = line.replace("\n", "")
            word_list.append(line)
    return word_list                     
     
def read_defs():
    def_list = []
    with open(DEF_FILE) as file:
        for line in file:
            line = line.replace("\n", "")
            def_list.append(line)
    return def_list                     
    
def write_words(words):
    with open(WORD_FILE, 'w') as file:    # newline= ""    is for CSV ONLY
        for items in words:
            file.write(items + "\n")
    
def write_defs(defs):
    with open(DEF_FILE, 'w') as file:        # newline= ""    is for CSV ONLY
        for items in defs:
            file.write(items + "\n")


# Functions below read in words that have been seperated into lists by difficulty

def read_easy_words():
    easy_words = []
    with open(EASY_WORDS_FILE) as file:
        for line in file:
            line = line.replace("\n", "")
            easy_words.append(line)
    return easy_words

def read_med_words():
    med_words = []
    with open(MED_WORDS_FILE) as file:
        for line in file:
            line = line.replace("\n", "")
            med_words.append(line)
    return med_words

def read_hard_words():
    hard_words = []
    with open(HARD_WORDS_FILE) as file:
        for line in file:
            line = line.replace("\n", "")
            hard_words.append(line)
    return hard_words

def read_easy_defs():
    easy_defs = []
    with open(EASY_DEFS_FILE) as file:
        for line in file:
            line = line.replace("\n", "")
            easy_defs.append(line)
    return easy_defs
        
# Functions bdelow write words to be seperated into 1 of 3 lists by difficulty

def write_easy_words(words):
    with open(EASY_WORDS_FILE, 'w') as file:
        for items in words:
            file.write(items + "\n")
            
def write_med_words(words):
    with open(MED_WORDS_FILE, 'w') as file:
        for items in words:
            file.write(items + "\n")
            
def write_hard_words(words):
    with open(HARD_WORDS_FILE, 'w') as file:
        for items in words:
            file.write(items + "\n")

def write_easy_defs(defs):
    with open(EASY_DEFS_FILE, 'w') as file:
        for items in defs:
            file.write(items + "\n")

