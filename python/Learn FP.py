import random
from functools import reduce

# ===== usage of map =====
# 1.
# name_lengths = map(len, ["Mary", "Isla", "Sam"])
# print(*name_lengths, sep=',')

# 2.
# squares = map(lambda x: x*x, [0, 1, 2, 3, 4])
# print(*squares)

# 3.
# names = ['Mary', 'Isla', 'Sam']
# code_names = ['Mr.Pink', 'Mr,Orange', 'Mr.Blonde']

# ex_names = map(lambda x: random.choice(code_names), names)
# hash_names = map(hash, names)
# print(*ex_names)
# print(*hash_names)

# ===== usage of reduce =====
# 1.
# sum = reduce(lambda a, x: a+x, [0, 1, 2, 3, 4], -2)
# print(sum)

# 2.
# sentences = ['Mary read a story to Sam and Isla.',
#              'Isla cuddled Sam.',
#              'Sam chortled.']
# sam_count = reduce(lambda a, x: a+x.count('Sam'), sentences, 0)
# print(sam_count)

# 3.
# people = [{'name': 'Mary', 'height': 160},
#     {'name': 'Isla', 'height': 80},
#     {'name': 'Same'}]
# heights = map(lambda x: x['height'],
#               filter(lambda x: 'height' in x, people))

# data = list(heights)
# if len(data) > 0:
#     from operator import add
#     average_height = reduce(add, data) / len(data)
#     print(average_height)


# ===== fp pattern =====
# from random import random

# def move_cars(car_positions):
#     return map(lambda x: x+1, car_positions)

# def run_step_of_race(state):
#     return {'time': state['time'] - 1,
#             'car_positions': move_cars(state['car_positions'])}

# def output_car(car_position):
#     return '-' * car_position

# def draw(state):
#     state_str = map(output_car, state['car_positions'])
#     print(*state_str, sep='\n')

# def race(state):
#     draw(state)
#     # something wrong with the code, 
#     # so that it becomes abnormal when state['time'] <= 3
#     if state['time'] > 3:
#         race(run_step_of_race(state))

# race({'time': 5,
#       'car_positions': [1, 1, 1]})


# ===== pipeline =====
bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

# common use
def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def call(fn, key):
    def apply_fn(record):
        return assoc(record, key, fn(record.get(key)))
    return apply_fn

# 1. one way
# def set_canada_as_country(band):
#     return assoc(band, 'country', "Canada")

# def strip_punctuation_from_name(band):
#     return assoc(band, 'name', band['name'].replace('.', ''))

# def capitalize_names(band):
#     return assoc(band, 'name', band['name'].title())

#2. another way
set_canada_as_country = call(lambda x: 'Canada', 'country')
strip_punctuation_from_name = call(lambda x: x.replace('.', ''), 'name')
capitalize_names = call(str.title, 'name')

def pipeline_each(data, fns):
    return reduce(lambda a, x: map(x, a),
                  fns,
                  data)

fns = [set_canada_as_country, strip_punctuation_from_name, capitalize_names]
print(*pipeline_each(bands, fns))

# Notice:
# Higher order function:
# takes a function as an argument, or returns a function.
# just like 'call' function declared before

