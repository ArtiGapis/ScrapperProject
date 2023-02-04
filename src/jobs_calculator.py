from operator import itemgetter
import collections
import get_input
import json

'''Reading json file data'''
def read():
    with open('../docs/jobs.json', 'r') as people_json:
        data = json.load(people_json)
    return data

'''Grouping by highest starting salary offered'''
def highest_salary():
    newlist = sorted(read(), key=itemgetter('Salary'), reverse=True)
    return newlist
    # print('Įmonės kuriose yra didžiausios algos:')
    # print(newlist)

'''Grouping job offers by interestbo pasiū'''
def highest_intrest():
    newlist = sorted(read(), key=itemgetter('Acept'), reverse=True)
    return newlist
    # print('Įmonės kurias daugiausiai renkasi:')
    # print(newlist)

'''Cities with the most supply by user keyword'''
def best_cities():
    unique_counts = collections.Counter(e['City'] for e in read())
    print(f'Tinkamiausias {get_input.input_getter()} specialybės miestas:')
    print(unique_counts)
