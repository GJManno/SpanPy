# save() needs to update self.dictionary, push() needs to send to master_dict <needs self.name check>

# check option 1 = list of self.names and zip with master_dict[]

import json

class Dictionary(object):

    def __init__(self, name):
        self.name = name
        self.isWorking = False
        self.dictionary = {}

###############################################################################
##        
## consolidate() takes 2 txt files of words & defs and creates self.dictionary
##
###############################################################################

    def consolidate(self,word_file, def_file):
        # pass in 2 text files of words & defs, create class attributes
        self.word_file = word_file
        self.def_file = def_file
        # create lists to store words & defs
        word_list = []
        def_list = []
        # populate word_list from word_file
        with open(self.word_file, 'r') as file:
            for line in file:
                line = line.replace("\n", "")
                word_list.append(line)
        # populate def_list from def_file
        with open(self.def_file, 'r') as file:
            for line in file:
                line = line.replace("\n", "")
                def_list.append(line)
        # zip word_list and def_list 2 preserve order
        zipper = list(zip(word_list, def_list))
        # create dictionary from zipped list
        self.dictionary = dict(zipper)

###############################################################################
##        
## save() takes self.dictionary and appends to 'master_dict.txt'
##
###############################################################################
           
    def push(self):
        # create a list to store all dicts
        master_dict = []
        # read in all dicts stored in master
        with open('master_dict.txt', 'r') as file:
            for line in file:
                master_dict.append(json.loads(line))
        with open('master_dict.txt', 'w') as file:
            # re-write current master_dict
            for line in master_dict:
                json.dump(line, file)
                file.write('\n')
            # add new dict to master_dict
            json.dump(self.dictionary, file)
            file.write('\n')

###############################################################################
##        
## add() & delete() manipulates self.dictionary, define() prints a definition
##
###############################################################################
            
    def add(self, word, definition):
        if word.title() not in self.dictionary:
            self.dictionary[word.title()]= definition.title()
        else:
            print(word, " already in dictionary")

    def delete(self, word):
        if word.title() in self.dictionary:
            del self.dictionary[word.title()]
        else:
            print(word, " not in dictionary, cannot delete")

    def define(self, word):
        if word.title() in self.dictionary:
            print(self.dictionary[word.title()])








            

        
##    def test(self):
##        print(self.word_list)
##        print(self.def_list)
##        print(self.zipper[0][0])
##        print(self.zipper[0][1])
##        print(self.zipper[1][0])
##        print(self.zipper[1][1])
##        for items in self.zipper:
##            print(items[0])
##            print(items[1])
##        print(self.dictionary)
##        print(len(self.dictionary))
##        print(len(self.word_list))
##        print(len(self.def_list))
##        for x in self.def_list:
##            if x in self.dictionary.values():
##                print("here  ",x)
##            else:
##                print("not here!!!!!!!  ",x)
##            print(len(self.master_dict[0]))          <-- will need to recreate attribute to run
##            print(len(self.master_dict[1]))












        

#  used as reference // tester
#  https://stackoverflow.com/questions/18067334/passing-a-file-to-a-class
#
##        >>> span_dict = Dictionary('first_dict')
##        >>> span_dict.consolidate('spanish_words.txt', 'spanish_defs.txt')
##        >>> span_dict.test()
        
