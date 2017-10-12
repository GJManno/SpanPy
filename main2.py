# check out pybook pg451


from dictionaries import dictionaries

def main():
    show_title()
    list_dicts()
    show_menu()

def show_title():
    print('Welcome Back Garret!')
    print('~' * 80)

def show_menu():
    print('COMMAND MENU')
    print('~' * 80)
    print('add - add a word to dictionary')
    print('delete - delete a word from dictionary')
    print('flash - flaschard through words')

    
def list_dicts():
    print('CURRENT DICTS')
    print('~' * 80)
    dicts = dictionaries
    line_format = "{:<7s} {:<15s} {:>7s} {:>12s} {:>25s}"
    line_format2 = "{:<7d} {:<15s} {:>7d} {:>12s} {:>25s}"
    print(line_format.format('Index', 'Name', 'Count', 'Score', 'Last Flash'))
    for i, name in enumerate(dicts):
        print(line_format2.format(i+1, name, 420, 'A+','10/11/17'))
    print('~' * 80)




if __name__ == "__main__":
    main()
