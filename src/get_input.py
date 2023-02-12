# from src.get_configs import all_configs
import subprocess
import os
import sys

CRED, CEND = '\033[91m', '\033[0m'
# config = all_configs
'''Retrieves the search keyword selected by the user'''
def input_getter(config):
    my_input = input(f'What field of work are you interested in\n').lower()
    my_input = 'python'
    config.main_logger.info(f'Aggregated user data : {my_input}')
    config.console_logger.info(f'Aggregated user data : {my_input}')
    return my_input

def choices_input(config):
    my_input = input(f'Choose one of the grouping options:\n\
    {CRED}salary{CEND} - Grouping by highest starting salary offered\n\
    {CRED}intrest{CEND} - Grouping job offers by interest\n\
    {CRED}city{CEND} - Cities with the most supply by user keyword\n').lower()
    if my_input in ('salary', 'intrest', 'city'):
        return my_input.lower()
    else:
        print(f'This is not {CRED}salary{CEND}, {CRED}intrest{CEND} or {CRED}city{CEND} words\nTry again\n')
        config.main_logger.warning(f'{my_input} is not in (salary, intrest, city)')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
