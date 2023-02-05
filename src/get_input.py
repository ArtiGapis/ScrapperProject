import logging.config
import yaml

with open('config/main.yml', 'r') as config:
    logging.config.dictConfig(yaml.safe_load(config)['logging'])

main_logger = logging.getLogger('main')
console_logger = logging.getLogger('console')

'''Retrieves the search keyword selected by the user'''
def input_getter():
    my_input = input(f'What field of work are you interested in\n')
    main_logger.info(f'Aggregated user data : {my_input}')
    console_logger.info(f'Aggregated user data : {my_input}')
    return my_input
