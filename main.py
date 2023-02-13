import sys
from src.jobs_calculator import highest_salary as salary, \
    highest_interest as interest, best_cities as city, read_json
import src.jobs_info_cleaner as jobs_info_cleaner
from src.get_configs import all_configs
import src.get_input as get_input
import src.writer as writer
import src.get_job_pages_url  as get_job_pages_url


configer = all_configs
CRED, CEND = '\033[91m', '\033[0m'

all_jobs_list = get_job_pages_url.jobs_loader(
    get_job_pages_url.job_pages_get(
        get_job_pages_url.url_check(
            configer.url, get_input.input_getter(configer), configer), configer), configer)

all_jobs_list_clean = jobs_info_cleaner.salary_clean(
    jobs_info_cleaner.job_clean(
        all_jobs_list, configer), configer)

def information_processing(jobs_list, config):
    writer.writer_to_json(jobs_list, config)


def saves_input(list_of_dict, choice, question, config):
    choise_input = input('Do you want to save or just view the information?\n(answer: view/save)\n').lower()
    if choise_input == 'view':
        print(question)
        for line in list_of_dict:
            print(line)
    elif choise_input == 'save':
        file_input = input('In which format do you want to save the document?\n1-csv, 2-xlsx\n').lower()
        if int(file_input) == 1:
            writer.writer_to_csv(list_of_dict, choice, config)
        elif int(file_input) == 2:
            writer.write_to_xlsx(list_of_dict, choice, config)
        else:
            print(f'This is not {CRED}1{CEND} or {CRED}2{CEND} ')
            config.main_logger.warning(f'The value <{file_input}> is not from the given list')
            print_choices(get_input.choices_input(config), read_json, config)
            sys.exit('EXIT')
    else:
        print(f'This is not {CRED}view{CEND} or {CRED}save{CEND} words')
        config.main_logger.warning(f'The value <{choise_input}> is not from the given list')
        print_choices(get_input.choices_input, read_json, config)
        sys.exit('EXIT')


def print_choices(choices_input, json_db, config):
    list_of_dict = []
    question = str
    choise = choices_input
    if choise == 'salary':
        question = 'Companies with the highest salaries:'
        for i in salary(json_db, config):
            list_of_dict.append(i)
    elif choise == 'interest':
        question = 'Most preferred companies:'
        for i in interest(json_db, config):
            list_of_dict.append(i)
    elif choise == 'city':
        question = f'The most suitable city by selected word:'
        place = 1
        for i in city(json_db, config):
            list_of_dict.append({'Nr': place, 'City': i})
            place += 1
    saves_input(list_of_dict, choise, question, config)


if __name__ == '__main__':
    information_processing(all_jobs_list_clean, configer)
    print_choices(get_input.choices_input(configer), read_json(configer.json_file, configer), configer)
