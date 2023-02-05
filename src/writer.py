import src.jobs_info_cleaner as jic
import src.jobs_class as jobs_class
from xlsxwriter import Workbook
import unicodecsv as csv
import logging.config
import yaml
import json

with open('config/main.yml', 'r') as log_config:
    logging.config.dictConfig(yaml.safe_load(log_config)['logging'])
with open('config/main.yml', encoding='utf8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

main_logger = logging.getLogger('main')
console_logger = logging.getLogger('console')

'''All processed information is placed in .json'''
def writer_to_json():
    jobs_json = []
    for job in jic.salary_clean():
        jobs = jobs_class.Jobs(*job)
        jobs_json.append({'Company' : jobs.company_fix, 'Position': jobs.position, 'City': jobs.city, \
                          'Salary': jobs.salary, 'Intrest' : int(jobs.intrest), 'Acept' : int(jobs.acept)})
    with open(config['json_file'], "w", encoding='utf8') as write_file:
        json.dump(jobs_json, write_file, indent=4, default=vars)
    main_logger.info(f'The information is saved in a json file')
    console_logger.info(f'The information is saved in a json file')


'''All processed information is placed in .csv'''
def writer_to_csv(list_of_dict, choice):
    try:
        with open(f'docs/{choice}.csv', 'wb') as output_file:
            dict_writer = csv.DictWriter(output_file, list_of_dict[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(list_of_dict)
        main_logger.info(f'All write to CSV file')
        console_logger.info(f'All write to CSV file')
    except FileNotFoundError:
        console_logger.error('Something is wrong with the document or directory')
        main_logger.error('Writer_to_csv give FileNotFoundError')


'''All processed information is placed in Excel file'''
def write_to_xlsx(list_of_dict, choice):
    try:
        wb = Workbook(f'docs/{choice}.xlsx')
        ws = wb.add_worksheet(choice)
        row, first_row = 1, 0
        ordered_list = []
        for head in list_of_dict[0].keys():
            ordered_list.append(head)
        for header in list_of_dict[0].keys():
            col = ordered_list.index(header)
            ws.write(first_row, col, header)
        for job in list_of_dict:
            for _key, _value in job.items():
                col = ordered_list.index(_key)
                ws.write(row, col, _value)
            row += 1
        wb.close()
        main_logger.info(f'All write to Excel file')
        console_logger.info(f'All write to Excel file')
    except FileNotFoundError:
        console_logger.error('Something is wrong with the document or directory')
        main_logger.error('Writer_to_csv give FileNotFoundError')
