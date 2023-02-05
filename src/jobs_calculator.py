from operator import itemgetter
import logging.config
import collections
import yaml
import json


with open('config/main.yml', 'r') as log_config:
    logging.config.dictConfig(yaml.safe_load(log_config)['logging'])

main_logger = logging.getLogger('main')
console_logger = logging.getLogger('console')

'''Reading json file data'''
def read():
    with open('docs/jobs.json', 'r') as people_json:
        data = json.load(people_json)
    return data


'''Grouping by highest starting salary offered'''
def highest_salary():
    newlist = sorted(read(), key=itemgetter('Salary'), reverse=True)
    main_logger.info(f'Get grouping by highest starting salary offered')
    console_logger.info(f'Get grouping by highest starting salary offered')
    return newlist


'''Grouping job offers by interest'''
def highest_intrest():
    newlist = sorted(read(), key=itemgetter('Acept'), reverse=True)
    main_logger.info(f'Get grouping job offers by interest')
    console_logger.info(f'Get grouping job offers by interest')
    return newlist


'''Cities with the most supply by user keyword'''
def best_cities():
    unique_counts = collections.Counter(e['City'] for e in read())
    main_logger.info(f'Get cities with the most supply by user keyword')
    console_logger.info(f'Get cities with the most supply by user keyword')
    return unique_counts
