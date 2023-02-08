import src.classes_wrapper as jobs_class
from src.get_configs import all_configs
from xlsxwriter import Workbook
import unicodecsv as csv
import json

config = all_configs
'''All processed information is placed in .json'''
def writer_to_json(jobs_list):
    jobs_json = []
    for job in jobs_list:
        jobs = jobs_class.Jobs(*job)
        jobs_json.append({'Company' : jobs.company_fix, 'Position': jobs.position, 'City': jobs.city, \
                          'Salary': jobs.salary, 'Intrest' : int(jobs.intrest), 'Acept': int(jobs.acept)})
    with open(config.json_file, "w", encoding='utf8') as write_file:
        json.dump(jobs_json, write_file, indent=4, default=vars)
    config.main_logger.info(f'The information is saved in a json file')
    config.console_logger.info(f'The information is saved in a json file')


'''All processed information is placed in .csv'''
def writer_to_csv(list_of_dict, choice):
    try:
        with open(f'docs/{choice}.csv', 'wb') as output_file:
            dict_writer = csv.DictWriter(output_file, list_of_dict[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(list_of_dict)
        config.main_logger.info(f'All write to CSV file')
        config.console_logger.info(f'All write to CSV file')
    except FileNotFoundError:
        config.console_logger.error('Something is wrong with the document or directory')
        config.main_logger.error('Writer_to_csv give FileNotFoundError')


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
        config.main_logger.info(f'All write to Excel file')
        config.console_logger.info(f'All write to Excel file')
    except FileNotFoundError:
        config.console_logger.error('Something is wrong with the document or directory')
        config.main_logger.error('Writer_to_csv give FileNotFoundError')
