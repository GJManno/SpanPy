# find a way to implement accents on this LINUX machine (menu -> character map)

# fix index 1 of test mode - "weekly words test" 

# enumerate instead of for loop w/ counter variable

# make command line interface with argparse 

# use an else statement after except "if no exception occurs", also use finally

# create logging for funcion calls / test runs, def and add counts

# add justified numbers and use for del / del index

# flash mode - implement MOVER to extra help list

# when using flashcards make a + and - (know or not) & count for specific words

# read and write scores loop for flashcard mode

# possible features to add 'check' (defs) + check_count looper

# def error multi word same def

# multiflash - enter score (5 of6), then enter failed word 4 recycle, reflip, save scores

# list2 = shows all defs with words

# possible for multiple modes (alter display, def check loop, move mode

# clean up and import diff modules 

# NEXT PROJECTS... web scrape weather

# USE timeit module to improve speed somewhere

# on load use main.log to print the last time logged in and how many days its been

# fix log_parser by changing to generator

# replace rjust with '{:>12}'  .format(x,y,z)

# utilize somewhere a var = false boolean and while not loop 

# add 30 day buffer to log_parser()

# use scheduler to clear log files every 20 days

# utilzie a decorater or functools.wrap for logging

# a way to create a new folder or file from command line

# move command verbs out of main.py and into command.py

# use OOP class to replicate a simple format (template = body_test)

# utilize from copy import deepcopy (maybe to conncat all words into master dict list)

# scheduled weeky test 

# imporve weekly test module for speed

# reuse 1 read and 1 write module by passing in FILENAME as param

# join word and def txt files into one file by adding a delimter within mmaybe '-' or ','

# fix negative day count on last login func

# change add_word exit keyword from 'break' to 'q'  (in commands.py) change all 'x' to 'q'

# make a list of ASCII codes used for common accented letters

# find a way to handle words with "otro nombres" or "otro significado"

# nice to have feature - adjustable bars when adding/subt words from current working dict

# I should automate the adding of words and defs but not to my current dict, scrape to a seperate file that can then be used to
# delegate the new words to the approriate test or dictionary.

###########################Where I left off last time################################
#             I have created virtualenv (spanPy) and need to pip install? schedule for weekly_refresh()                                                                                                         
#                     last left off trying to recycle flash list                                                                                           
#
# 
#
#
#   RE-explore = dict_class.py (stable)
#
#
#   10/12/18 - created move_word() and tested at E,M,H difficulty (stable)
#              started on flash feature (e,m,h,a)  in span_func.py (broken * needs def files)
#               think this thru before going further... might break everythin
#               if I make words and defs obselte and move to easy,med,hard
#               need to make words/defs the master, and never pop even when moving
#               to easy list. You also need to use git once this is fixed up
#######################################################################################

#######################Prioritized fix list######################################
#
 #
  # 0) add a command to show either easy, medium, or hard list on flash
  # 1) recycle / delete feature for flash cards
  # 2) new word automation / delegation
 #
#
#############################################################

import random, logging

LOGFILE = "main.log"

from span_funcs import body_test, flash_mode, log_parser, test_mode
from init import read_words, read_defs, write_words, write_defs, read_easy_words, read_med_words, read_hard_words, write_easy_words, write_med_words, write_hard_words
from commands import print_commands, print_words, print_defs, add_word, delete_word, define_word, clear, move_word 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def main():
    logger.info("RUN")
    print("WELCOME BACK, GARRET!".rjust(110))
    log_parser(LOGFILE)
    print_commands() # need to add move_word()
    words = read_words()
    defs = read_defs()
    easy_words = read_easy_words()
    med_words = read_med_words()
    hard_words = read_hard_words()
    # above init needed for parameters
    print("CURRENT WORKING DICTIONARY:")
    print_words(words)
    while True:
        action = input("\nCommand:\t")
        if action.lower() == "add":
            add_word(words, defs)
        elif action.lower() == "list":
            print_words(words)
        elif action.lower() == "flash":
            flash_mode(words,defs)
        elif action.lower() == "dict":   #change name & make justified
            print_defs(words, defs)
        elif action.lower() == "del":
            delete_word(words, defs)
        elif action.lower() == "def":
            define_word(words,defs)
        elif action.lower() == "commands":
            print_commands()
        elif action.lower() == "body":
            body_test()
        elif action.lower() == "clear":
            clear()
        elif action.lower() == "test":
            test_mode()
        elif action.lower() == "move":
            move_word(words, defs, easy_words, med_words, hard_words, easy_defs)
        elif action.lower() == "exit":
            print("Way To Learn... See You Soon!")
            break
        else:
            print("Invalid Command... see menu")

if __name__ == "__main__":
    main()
