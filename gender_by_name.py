"""
This file is part of The-Spyder-Girl.

    The-Spyder-Girl is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    The-Spyder-Girl is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with The-Spyder-Girl.  If not, see <http://www.gnu.org/licenses/>.
"""

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
