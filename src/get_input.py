import logging.config
import yaml

with open('..\config\main.yml', 'r') as config:
    logging.config.dictConfig(yaml.safe_load(config)['logging'])

main_logger = logging.getLogger('main')
error_logger = logging.getLogger('error')

'''Retrieves the search keyword selected by the user'''
def input_getter():
    my_input = input(f'What field of work are you interested in\n')
    # my_input = 'python'
    main_logger.info(f'Aggregated user data : {my_input}')
    return my_input


if __name__ == '__main__':
    print(input_getter())