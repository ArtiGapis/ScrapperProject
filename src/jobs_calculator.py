from operator import itemgetter
import collections
import json
import sys


'''Reading json file data'''
def read_json(json_file, config):
    try:
        with open(json_file, 'r') as jobs_json:
            data = json.load(jobs_json)
        return data
    except FileNotFoundError:
        config.main_logger.error(f'Function "read_json" error. JSON file not found')
        sys.exit(f'JSON file not found. check the file "{json_file}" and restart the program')


'''Grouping by highest starting salary '''
def highest_salary(json_db, config):
    h_salary_lst = sorted(json_db, key=itemgetter('Salary'), reverse=True)
    config.main_logger.info(f'Gets grouping by highest starting salary')
    config.console_logger.info(f'Gets grouping by highest starting salary')
    return h_salary_lst


'''Grouping job offers by interest'''
def highest_interest(json_db, config):
    h_interest_lst = sorted(json_db, key=itemgetter('Acept'), reverse=True)
    config.main_logger.info(f'Gets grouping job offers by interest')
    config.console_logger.info(f'Gets grouping job offers by interest')
    return h_interest_lst


'''Cities with the most supply by user keyword'''
def best_cities(json_db, config):
    best_city_lst = collections.Counter(e['City'] for e in json_db)
    config.main_logger.info(f'Gets cities with the most supply by user keyword')
    config.console_logger.info(f'Gets cities with the most supply by user keyword')
    return best_city_lst
