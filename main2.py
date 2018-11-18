## CHECKLIST TO SUCCESS

# check out pybook pg451, make an actionable plan, segregate responsbilities
# convert accented letters to UTF-8
# simplify calls. animals, not dict_ofdicts['animals']




# consider getting rid on command line and commandss
# look in argparse...? maybe thats better ^
# add works... but delete?
# save(i) <json> & save_csv()





from dict_class import list_of_dicts, Dictionary
## from commandss import add, delete

def main():
    print('Welcome Back Garret!')
    print('~' * 80)
    show_menu()
    init_load = int(input("Load #"))
    load(index=init_load)
    for i in list_of_dicts:
        if i.isActive == True:
            active_dict = i
    while True:
        action = input("\nCommand:\t")
        if action.lower() == "add":
            while True:
                print()
                w = input('Word:\t')
                d = input('Definition:\t')
                print()
                if w == 'x' or d == 'x':
                    break
                else:
                    active_dict.add(w,d)
        elif action.lower() == "delete":
                w = input('Word:\t')
                f = input('From:\t')
                if w == 'x' or f == 'x':
                    break
                else:
                    if f in list_of_dicts:
                        f.delete(w)
                    elif f == 'self':
                        active_dict.delete(w)
                    else:
                        print(f, 'is not a dictionary')
        elif action.lower() == "def":
            define_word(words,defs)
        elif action.lower() == "show": 
            show_dict() # show contents, need to create show_dict()
        elif action.lower() == "flash":
            active_dict.test()
        elif action.lower() == "exit":
            print("Way To Learn... See You Soon!")
            #save()
            break
        elif action.lower() == "menu":
            show_menu()
            show_commands()
        else:
            print("Invalid Command... see menu")



def active(): # prints current active dict
    print(active_dict.name, ' is currently active')

def show_menu(): #reusable
    print('CURRENT DICTS')
    print('~' * 80)
    line_format = "{:<7s} {:<15s} {:>7s} {:>12s} {:>25s}"
    line_format2 = "{:<7d} {:<15s} {:>7d} {:>12d} {:>25s}"
    print(line_format.format('Index', 'Name', 'Count', 'Score', 'Last Flash'))
    for i, j in enumerate(list_of_dicts):
        print(line_format2.format(i+1, j.name, j.count, j.high_score,'10/11/17'))
    print('~' * 80)

def show(index=None): # show words/defs for index
    line_format = '{:<17s} - {}'
    if index is not None and type(index) == int:
        index -= 1
        i = list_of_dicts[index]
        for k, v in i.dictionary.items():
            print(line_format.format(k,v))
    # load by name
    elif index is not None and type(index) == str:
        for i in list_of_dicts:
            if i.name == index:
                for k, v in i.dictionary.items():
                    print(line_format.format(k,v))
    else:
        show_menu()
        index = int(input('Show #'))
        try:
            index -= 1
            i = list_of_dicts[index]
            for k, v in i.dictionary.items():
                print(line_format.format(k,v))
        except Exception as e:
            print(type(e))
        
def load(index=None):

# no need to unload if index = loaded dict
    
    # unload any active dicts
    for i in list_of_dicts:
        if i.isActive == True:
            i.isActive = False
            print('Unloading', i.name)
    # load by index
    if index is not None and type(index) == int:
        index -= 1
        i = list_of_dicts[index]
        i.isActive = True
        print()
        print(i.name, 'was successfully loaded!')
    # load by name
    elif index is not None and type(index) == str:
        for i in list_of_dicts:
            if i.name == index:
                i.isActive = True
                print()
                print(i.name, 'was successfully loaded!')
            else:
                print('not a valid index')
    else:
        show_menu()
        index = int(input('Load #'))
        try:
            index -= 1
            i = list_of_dicts[index]
            i.isActive = True
            print()
            print(i.name, 'was successfully loaded!')
        except Exception as e:
            print(type(e))

def unload():
    for i in list_of_dicts:
        if i.isActive == True:
            i.isActive = False
            print(i.name, 'was successfully unloaded!')
    index = int(input('Load #'))
    load(index=index)
        


def show_commands():
    print('COMMAND MENU')
    print('~' * 80)
    print('add - enter an add loop for loaded dict')
    print('delete - delete a word from dictionary')
    print('flash - flaschard through words')
            
        
    # unload any working dict and load dict with given index
##            for key in self.dictionary:
##                print("{:<12s} {:<5s} {}".format(key, "-",self.dictionary[key]))


if __name__ == "__main__":
    main()
