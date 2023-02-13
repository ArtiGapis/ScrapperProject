import sys

CRED, CEND = '\033[91m', '\033[0m'
'''System gets selected keyword by the user'''
def input_getter(config):
    my_input = input(f'What kind of work area are you interested in?\n').lower().replace(' ', '+')
    config.main_logger.info(f'Aggregated user data : {my_input}')
    config.console_logger.info(f'Aggregated user data : {my_input}')
    return my_input

def choices_input(config):
    my_input = input(f'Choose one of the grouping options:\n\
    {CRED}salary{CEND} - Grouping by highest starting salary\n\
    {CRED}interest{CEND} - Grouping job offers by number of candidates\n\
    {CRED}city{CEND} - Cities with the most supply by user keyword\n').lower()
    if my_input in ('salary', 'interest', 'city'):
        return my_input.lower()
    else:
        print(f'This is not {CRED}salary{CEND}, {CRED}interest{CEND} or {CRED}city{CEND} words')
        config.main_logger.warning(f'{my_input} is not salary, interest, city words')
        sys.exit('EXIT')
