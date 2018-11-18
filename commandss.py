#
# trying to understand where this is being used if at all.
# commandss is being used in main2.py
#

def add(word, definition, destination=None):
    if destination is not None:
            try:
                destination.add(word, definition)
                print('{} added to {} dict'.format(word, destination.name))
            except NameError:
                print('Invalid Destination')
    else:
        active_dict.add(word, definition)
        print('{} added to the {} dict'.format(word, active_dict.name))
    
def delete(word, target):
    if target in list_of_dicts:     
        for i in list_of_dicts:
            if i == target:
                i.delete(word)
                print('{} removed from the {} dict'.format(word, i.name))
    else:
        print('Invalid Dictionary')
    
