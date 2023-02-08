from src.jobs_calculator import highest_salary as salary, \
    highest_intrest as intrest, best_cities as city, read_json
from src.jobs_info_cleaner import all_jobs_list_clean
from src.get_configs import all_configs
from src.get_input import choices_input
import src.writer as writer


config = all_configs
CRED, CEND = '\033[91m', '\033[0m'


def information_processing(jobs_list):
    writer.writer_to_json(jobs_list)


def saves_input(list_of_dict, choice, question):
    choise_input = input('Do you want to save the information or just view it?\n(answer: view/save)\n').lower()
    if choise_input == 'view':
        print(question)
        for line in list_of_dict:
            print(line)
    elif choise_input == 'save':
        file_input = input('In which format do you want to save the document?\n1-csv, 2-xlsx\n').lower()
        if int(file_input) == 1:
            writer.writer_to_csv(list_of_dict, choice)
        elif int(file_input) == 2:
            writer.write_to_xlsx(list_of_dict, choice)
        else:
            print(f'This is not {CRED}1{CEND} or {CRED}2{CEND} \nTry again\n')
            config.main_logger.warning(f'The value <{file_input}> is not from the given list')
            print_choices(choices_input, read_json)
    else:
        print(f'This is not {CRED}view{CEND} or {CRED}save{CEND} words\nTry again\n')
        config.main_logger.warning(f'The value <{choise_input}> is not from the given list')
        print_choices(choices_input, read_json)


def print_choices(choices_input, json_db):
    list_of_dict = []
    question = str
    choise = choices_input
    if choise == 'salary':
        question = 'Companies with the highest salaries:'
        for i in salary(json_db):
            list_of_dict.append(i)
    elif choise == 'intrest':
        question = 'Most preferred companies:'
        for i in intrest(json_db):
            list_of_dict.append(i)
    elif choise == 'city':
        question = f'The most suitable specialty city:'
        place = 1
        for i in city(json_db):
            list_of_dict.append({'Nr': place, 'City': i})
            place += 1
    saves_input(list_of_dict, choise, question)


if __name__ == '__main__':
    information_processing(all_jobs_list_clean)
    print_choices(choices_input(), read_json(config.json_file))
