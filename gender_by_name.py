import genderator
from get_fb_names import *
from collections import OrderedDict

def guess_gender_name(name, guesser):
    answer = guesser.guess_gender(name)
    if answer:
        return answer
    else:
        return OrderedDict([('names', name), ('gender', 'Unknown')])

def export_to_json(data_list):
    results = {'Female':0, 'Male':0, 'Unknown':0}

    for d in data_list:
        results[d['gender']] += 1

    return results


names = list(get_feed_names().keys())
guesser = genderator.Parser()
data_list = []

for name in names:
    data_list.append(guess_gender_name(name, guesser))

export_to_json(data_list)
