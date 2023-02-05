from src.jobs_calculator import highest_salary as salary, \
    highest_intrest as intrest, best_cities as city
import src.writer as writer
import logging.config
import subprocess
import yaml
import os
import sys

with open('config/main.yml', 'r') as log_config:
    logging.config.dictConfig(yaml.safe_load(log_config)['logging'])

CRED, CEND = '\033[91m', '\033[0m'
main_logger = logging.getLogger('main')
console_logger = logging.getLogger('console')

def information_processing():
    writer.writer_to_json()

def choices_input():
    my_input = input(f'Choose one of the grouping options:\n\
    {CRED}salary{CEND} - Grouping by highest starting salary offered\n\
    {CRED}intrest{CEND} - Grouping job offers by interest\n\
    {CRED}city{CEND} - Cities with the most supply by user keyword\n')
    if my_input in ('salary','intrest','city'):
        return my_input.lower()
    else:
        print(f'This is not {CRED}salary{CEND}, {CRED}intrest{CEND} or {CRED}city{CEND} words\nTry again\n')
        main_logger.warning(f'{my_input} is not in (salary, intrest, city)')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

def saves_input(list_of_dict, choice, question):
    choise_input = input('Do you want to save the information or just view it?\n(answer: view/save)\n')
    if choise_input == 'view':
        print(question)
        for line in list_of_dict:
            print(line)
    elif choise_input == 'save':
        file_input = input('In which format do you want to save the document?\n1-csv, 2-xlsx\n')
        if int(file_input) == 1:
            writer.writer_to_csv(list_of_dict, choice)
        elif int(file_input) == 2:
            writer.write_to_xlsx(list_of_dict, choice)
        else:
            print(f'This is not {CRED}1{CEND} or {CRED}2{CEND} \nTry again\n')
            main_logger.warning(f'The value <{file_input}> is not from the given list')
            print_choices()
    else:
        print(f'This is not {CRED}view{CEND} or {CRED}save{CEND} words\nTry again\n')
        main_logger.warning(f'The value <{choise_input}> is not from the given list')
        print_choices()


def print_choices():
    list_of_dict = []
    question = str
    choise = choices_input()
    if choise == 'salary':
        question = 'Companies with the highest salaries:'
        for i in salary():
            list_of_dict.append(i)
    elif choise == 'intrest':
        question = 'Most preferred companies:'
        for i in intrest():
            list_of_dict.append(i)
    elif choise == 'city':
        question = f'The most suitable specialty city:'
        place = 1
        for i in city():
            list_of_dict.append({'Nr': place, 'City': i})
            place += 1
    saves_input(list_of_dict, choise, question)

if __name__ == '__main__':
    information_processing()
    print_choices()
