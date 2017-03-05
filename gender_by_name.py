import genderator
from get_fb_names import *

def guess_gender_name(name, guesser):
    answer = guesser.guess_gender(name)
    if answer:
        print(answer)
    else:
        print('Name doesn\'t match')


names = list(get_feed_names().keys())
guesser = genderator.Parser()

for name in names:
    guess_gender_name(name, guesser)
