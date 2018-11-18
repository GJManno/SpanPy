import timeit

print(timeit.timeit('''import random
dictionary ={'hello':'there', 'booyah':'shaka'}
questions = random.shuffle(list(dictionary.keys()))''', number=100000))

